from rest_framework.authentication import TokenAuthentication

class CustomAuthentication(TokenAuthentication):
    """
    Change user request header authorization from "Token" to "Bearer"
    """
    
    keyword = "Bearer"