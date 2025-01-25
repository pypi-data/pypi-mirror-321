"""
Exceptions personnalisées pour l'API Lulu Print.
"""

class LuluAPIError(Exception):
    """Exception levée lors d'une erreur avec l'API Lulu."""
    pass

class LuluAuthError(LuluAPIError):
    """Exception levée lors d'une erreur d'authentification avec l'API Lulu."""
    pass
