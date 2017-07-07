from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404


# Create your views here.
from .mixins import StaffRequiredMixin, LoginRequiredMixin
from .models import Simulacoes



class SimulacoesListView(ListView):
	model = Simulacoes
	queryset = Simulacoes.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(SimulacoesListView, self).get_context_data(*args, **kwargs)
		print context
		return context


class SimulacoesDetailView(DetailView):
	model = Simulacoes
	#template_name = "<appname>/<modelname>_detail.html"





def simulacoes_detail_view_func(request, id):
		#simulacoes_instance = simulacoes.objects.get(id=id)
		simulacoes_instance = get_object_or_404(simulacoes, id=id)
		try:
			simulacoes_instance = simulacoes.objects.get(id=id)
		except simulacoes.DoesNotExist:
			raise Http404
		except:
			raise Http404

		template = "simulacoes/simulacoes_detail.html"
		context = {
			"object": simulacoes_instance
		}
		return render(request, template, context)