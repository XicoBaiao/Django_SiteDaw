# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


# Create your models here.
class SignUp(models.Model):#Registo
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #__str__ in python 3
		return self.email


DEVICES_CHOICES = (
	('1', 'Smartphone'),
	('2', 'Tablet'),
	('3', 'Portátil'),
	('4', 'Televisor'),
	('5', 'Câmara Fotográfica'),
	('6', 'Outros'),
	)

PRICES_CHOICES = {
	('1', '0-200'),
	('2', '200-400'),
	('3', '400-600'),
	('4', '600+'),
}

class simulation(models.Model):
	Categoria = models.CharField(max_length=25,choices=DEVICES_CHOICES, blank=False, null=False, default='Tipo de aparelho')
	Nome = models.CharField(max_length=120, blank=True, null=True)
	Valor = models.CharField(max_length=25,choices=PRICES_CHOICES, blank=False, null=False, default='Valor do aparelho')
	

	def __unicode__(self):
		return self.Nome


