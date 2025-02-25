from rest_framework import permissions

class IsAdminOrSuperuserForPost (permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff)

class IsOwnerOrSuperuser (permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Superusers have full access
        if request.user.is_superuser:
            return True

        # Only allow access if user is creator of list
        return obj.owner == request.user


class IsOwnerOrProjectOwnerOrSuperuser (permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # allow access if superuser
        if request.user.is_superuser:
            return True

        # allow access if user created pledge
        if obj.supporter == request.user:
            return True

        # allow access if user is owner of the pledged project 
        if obj.project.owner == request.user:
            return True

        # deny access to all other users
        return False