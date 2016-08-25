from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin


from .models import AppUser


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = AppUser
        fields = ("username", "email", "password", "first_name", "last_name")


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = AppUser

class AppUserAdmin(UserAdmin):
    form = AppUserChangeForm
    add_form = AppUserCreationForm
    list_display = ('username', 'first_name', 'last_name', 'gender', 'phone', 'verified', 'age')
    readonly_fields = ('age', 'last_login', 'date_joined', )
    fieldsets = (
        ('Authorization', {
            'fields': ('username', 'password')
        }),
        ('Personal Info', {
            'fields': (('first_name', 'last_name'), 'email', 'gender', 'phone', 'birthday', 'verified',)
        }),
        ('Activity', {
            'fields': ('last_login', 'date_joined')
        }),
    )

admin.site.register(AppUser, AppUserAdmin)