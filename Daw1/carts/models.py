from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete


from simulacoes.models import Variation
# Create your models here.

class CartSimulation(models.Model):
	cart = models.ForeignKey("Cart")
	simulacoes = models.ForeignKey(Variation)
	quantity = models.PositiveIntegerField(default=1)
	line_simulacoes_total = models.IntegerField()

	def __unicode__(self):
		return self.simulacoes.Nome

	def remove(self):
		return self.simulacoes.remove_from_cart()


def cart_simulacoes_pre_save_receiver(sender, instance, *args, **kwargs):
	qty = instance.quantity
	if qty >= 1:
		ValorSeguro = instance.simulacoes.get_price()
		line_simulacoes_total = Decimal(qty) * Decimal(ValorSeguro)
		instance.line_simulacoes_total = line_simulacoes_total


pre_save.connect(cart_simulacoes_pre_save_receiver, sender=CartSimulation)


def cart_simulacoes_post_save_receiver(sender, instance, *args, **kwargs):
	instance.cart.update_subtotal()

post_save.connect(cart_simulacoes_post_save_receiver, sender=CartSimulation)

post_delete.connect(cart_simulacoes_post_save_receiver, sender=CartSimulation)



class Cart(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
	simulacoes = models.ManyToManyField(Variation, through=CartSimulation)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	subtotal = models.IntegerField(null=True)

	
	def __unicode__(self):
		return str(self.id)

	def update_subtotal(self):
		print "updating..."
		subtotal = 0
		simulacoes = self.cartsimulation_set.all()
		for simulacoes in simulacoes:
			subtotal += simulacoes.line_simulacoes_total
		self.subtotal = subtotal
		self.save()

	#subtotal price
	#taxes total
	#discounts
	#total price


