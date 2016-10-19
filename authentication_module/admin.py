from django.contrib import admin
from .models import CustomUser
from plataforma.emails import enviar_correo
from plataforma.models import Correo
from sitios.models import Sitio


class UserAdmin(admin.ModelAdmin):
	ordering = ('email', )
	list_display = ('email', 'es_cuenta_activa')
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()
		if change:
			if "es_cuenta_activa" in form.changed_data:
				if obj.es_cuenta_activa:
					correo = Correo.objects.filter(identificador='MCA')[0]	
				else:
					correo = Correo.objects.filter(identificador='MCI')[0]
					
				enviar_correo(obj.email,{"contenido":correo.cuerpo},correo.asunto,'correo_base.html')

	def get_queryset(self, request):
		qs = super(UserAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		municipio_id= request.user.sitios.filter(tipo_sitio='M')[0].municipio_id
		sitios=Sitio.objects.filter(municipio_id=municipio_id)		
		return qs.filter(id__in = [sitio.usuario_id for sitio in sitios])

admin.site.register(CustomUser, UserAdmin)
