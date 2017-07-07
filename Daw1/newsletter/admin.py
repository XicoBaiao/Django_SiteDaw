from django.contrib import admin

# Register your models here.

from .forms import SignUpForm, SimulationForm
from .models import SignUp, simulation

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm
	#class Meta:
	#	model = SignUp

class SimularAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "Categoria", "Nome", "Valor"]
	form = SimulationForm


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(simulation, SimularAdmin)