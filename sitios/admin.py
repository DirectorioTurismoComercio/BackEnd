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



admin.site.register(Sitio,SiteAdmin)





