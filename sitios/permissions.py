from rest_framework import permissions

class IsSiteOwner(permissions.BasePermission):
    
	def has_object_permission(self, request, view, site):
		return site.usuario == request.user