class B2BAPIError(Exception):
    """Base class for B2B API errors."""
    pass

class AuthenticationError(B2BAPIError):
    pass

class ResourceNotFoundError(B2BAPIError):
    pass
