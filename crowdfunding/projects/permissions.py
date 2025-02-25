from rest_framework import permissions

CERTAIN_PERMISSIONS = ('HEAD', 'OPTIONS')

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsSupporterOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in CERTAIN_PERMISSIONS:
            return True
        return obj.supporter == request.user

class IsCreatorOrSuperuserOrAdmin(permissions.BasePermission):
    """custom permission to allow only the creator of a list to view and modify it,
    except superusers who can access and modify all lists"""
    def has_object_permission(self, request, view, obj):
        # Superusers have full access
        if request.user.is_superuser or request.user.is_staff:
            return True

        # Only allow access if user is creator of list
        return obj.owner == request.user

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