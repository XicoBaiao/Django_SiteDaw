from django.contrib import admin

# Register your models here.



from .models import Simulacoes, Variation, SimulationImage

class simulacoesImageInline(admin.TabularInline):
	model = SimulationImage
	extra = 0

class VariationInline(admin.TabularInline):
	model = Variation
	extra = 0

class SimulationAdmin(admin.ModelAdmin):
	list_display = ["Nome"]
	inlines = [
		VariationInline,
		simulacoesImageInline
	]
	class Meta:
		model = Simulacoes

class VariationAdmin(admin.ModelAdmin):
	list_display = ["Nome"]

	class Meta:
		model = Variation

admin.site.register(Simulacoes, SimulationAdmin)

admin.site.register(Variation, VariationAdmin)

admin.site.register(SimulationImage)




