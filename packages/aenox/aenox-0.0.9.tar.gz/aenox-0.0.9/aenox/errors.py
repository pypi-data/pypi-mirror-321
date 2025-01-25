class AenoXError(Exception):
    """Base exception class for all AenoX exceptions."""
    pass


class InvalidAPIKey(AenoXError):
    """Raised when an invalid API key is provided.
    """

    def __init__(self):
        super().__init__("Invalid API key provided.")


class NotFound(AenoXError):
    """Raised when an object is not found."""
    pass


class UserNotFound(NotFound):
    """Raised when the given user ID is not found."""

    def __init__(self):
        super().__init__("Could not find the user ID.")
        
        
class CooldownError(AenoXError):
    """Raised when the cooldown is not ended."""
    
    def __init__(self):
        super().__init__("Cooldown for query.")


class NoMoreCreditsAvailable(AenoXError):
    """Raised when you do not have enough credits for this operation."""

    def __init__(self):
        super().__init__("No more credits. Check /api on Discord.")
