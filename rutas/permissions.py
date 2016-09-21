from rest_framework import permissions

class IsRouteOwner(permissions.BasePermission):
    
	def has_object_permission(self, request, view, route):
		return route.sitio.usuario == request.user