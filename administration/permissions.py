from rest_framework.permissions import BasePermission

class IsRole(BasePermission):
    def __init__(self, role):
        self.role = role

    def has_permission(self, request, view):
        return request.user.role == self.role
from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    """
    Generic permission class that checks if the user role
    is in the allowed_roles list defined on the view.
    """
    def has_permission(self, request, view):
        allowed_roles = getattr(view, 'allowed_roles', [])
        return request.user.is_authenticated and request.user.role in allowed_roles

