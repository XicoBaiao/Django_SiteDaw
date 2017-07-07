from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify
# Create your models here.

class SimulacoesQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)


class SimulacoesManager(models.Manager):
	def get_queryset(self):
		return SimulacoesQuerySet(self.model, using=self._db)

	def all(self, *args, **kwargs):
		return self.get_queryset().active()


class Simulacoes(models.Model):
	Categoria = models.CharField(max_length=120)
	Nome = models.CharField(max_length=120)
	Valor = models.IntegerField()
	ValorSeguro = models.IntegerField(default='')
	active = models.BooleanField(default=True)

	objects = SimulacoesManager()


	def __unicode__(self):
		return self.Nome

	def get_absolute_url(self):
		return reverse("simulacoes_detail", kwargs={"pk": self.pk})


class Variation(models.Model):
	Simulacoes = models.ForeignKey(Simulacoes)
	Nome = models.CharField(max_length=120)
	Seguro = models.CharField(max_length=120)
	ValorSeguro = models.IntegerField()
	Valor = models.IntegerField(null=True, blank=True)
	active = models.BooleanField(default=True)



	def __unicode__(self):
		return self.Seguro


	def get_price(self):
		if self.ValorSeguro is not None:
			return self.ValorSeguro
		else:
			return self.Valor


	def get_absolute_url(self):
		return self.simulacoes.get_absolute_url()

	def add_to_cart(self):
		return "%s?simulacoes=%s&qty=1" %(reverse("cart"), self.id)

	def remove_from_cart(self):
		return "%s?simulacoes=%s&qty=1&delete=True" %(reverse("cart"), self.id)

	def get_Nome(self):
		return "%s - %s" %(self.Simulacoes.Nome, self.Nome)
	

def simulacoes_post_saved_receiver(sender, instance, created, *args, **kwargs):
	Simulacoes = instance
	variations = Simulacoes.variation_set.all()
	if variations.count() == 0:
		new_var = Variation()
		new_var.Simulacoes = Simulacoes 
		new_var.Nome = "Default"
		new_var.ValorSeguro = Simulacoes.ValorSeguro
		new_var.save()


post_save.connect(simulacoes_post_saved_receiver, sender=Simulacoes)



# Simulacoes images

def image_upload_to(instance, filename):
	Nome = instance.Simulacoes.Nome
	slug = slugify(Nome)
	basename, file_extension = filename.split(".")
	new_filename = "%s-%s.%s" %(basename, instance.id, file_extension)
	return "Simulacoes/%s/%s" %(slug, new_filename)


class SimulationImage(models.Model):
	Simulacoes = models.ForeignKey(Simulacoes)
	image = models.FileField(upload_to=image_upload_to)

	def __unicode__(self):
		return self.Simulacoes.Nome