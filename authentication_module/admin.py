from django.contrib import admin
from .models import CustomUser



class UserAdmin(admin.ModelAdmin):
	ordering = ('email', )
	list_display = ('email', 'es_cuenta_activa')


admin.site.register(CustomUser, UserAdmin)