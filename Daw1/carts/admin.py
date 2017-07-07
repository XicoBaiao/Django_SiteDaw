from django.contrib import admin

# Register your models here.


from .models import Cart, CartSimulation



class CartSimulationInline(admin.TabularInline):
	model = CartSimulation

class CartAdmin(admin.ModelAdmin):
	inlines = [
		CartSimulationInline
	]
	class Meta:
		model = Cart

admin.site.register(Cart, CartAdmin)