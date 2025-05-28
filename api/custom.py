from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission

class CustomAuthentication(TokenAuthentication):
    """
    Change user request header authorization from "Token" to "Bearer"
    """
    
    keyword = "Bearer"

class IsUnAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated