from django.contrib import admin
from .models import Sitio, Foto, SitioCategoria
from plataforma.models import Categoria

class FotoInline(admin.TabularInline):
    model = Foto


class CategoriaInline(admin.TabularInline):
    model = SitioCategoria


class SiteAdmin(admin.ModelAdmin):
	ordering = ('nombre', )
	filter_horizontal = ('tags', )
	inlines = [FotoInline,CategoriaInline]

	def get_queryset(self, request):
		qs = super(SiteAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		municipio_id= request.user.sitios.filter(tipo_sitio='M')[0].municipio_id
		return qs.filter(municipio_id=municipio_id)



admin.site.register(Sitio,SiteAdmin)





