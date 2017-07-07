from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin, DetailView


# Create your views here.

from simulacoes.models import Variation
from carts.models import Cart, CartSimulation


class CartView(SingleObjectMixin, View):
	model = Cart
	template_name = "carts/view.html"
	
	def get_object(self, *args, **kwargs):
		self.request.session.set_expiry(0) #300 =5 minutes
		cart_id = self.request.session.get("cart_id")
		if cart_id == None:
			cart = Cart()
			cart.save()
			cart_id = cart.id
			self.request.session["cart_id"] = cart_id
		cart = Cart.objects.get(id=cart_id)		
		if self.request.user.is_authenticated():
			cart.user = self.request.user
			cart.save()
		return cart
	

	def get(self, request, *args, **kwargs):
		cart = self.get_object()
		simulacoes_id = request.GET.get("simulacoes")
		delete_simulacoes = request.GET.get("delete", False)
		simulacoes_added = False
		if simulacoes_id:
			simulacoes_instance = get_object_or_404(Variation, id=simulacoes_id)
			qty = request.GET.get("qty", 1)
			try:
				if int(qty) < 1:
					delete_simulacoes = True
			except:
				raise Http404
			cart_simulacoes, created = CartSimulation.objects.get_or_create(cart=cart, simulacoes=simulacoes_instance)
			if created:
				simulacoes_added = True
			if delete_simulacoes:
				cart_simulacoes.delete()
			else:
				cart_simulacoes.quantity = qty
				cart_simulacoes.save()
		if request.is_ajax():
			return JsonResponse({"deleted": delete_simulacoes, "simulacoes_added": simulacoes_added})

		context = {
			"object": self.get_object()
		}
		template = self.template_name
		return render(request, template, context)



class CheckoutView(DetailView):
	model = Cart
	template_name = "carts/checkout_view.html"

	def get_object(self, *args, **kwargs):
		cart_id = self.request.session.get("cart_id")
		if cart_id == None:
			return redirect("cart")
		cart = Cart.objects.get(id=cart_id)	
		return cart

	def get_context_data(self, *args, **kwargs):
		context = super(CheckoutView, self).get_context_data(*args, **kwargs)
		user_can_continue = False
		if not self.request.user.is_authenticated(): # or if request.user.is_guest
			context["user_auth"] = False
			context["login_form"] = AuthenticationForm()
			context["next_url"] = self.request.build_absolute_uri()
 		if self.request.user.is_authenticated():
 			user_can_continue = True
 		context["user_can_continue"] = user_can_continue
 		return context




