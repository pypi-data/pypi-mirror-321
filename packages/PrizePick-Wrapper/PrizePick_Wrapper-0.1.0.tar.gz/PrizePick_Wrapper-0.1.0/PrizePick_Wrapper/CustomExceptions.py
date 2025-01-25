
class RateLimit(Exception):
    """Exception raised for rate limiting errors"""
    def __init__(self, message="Rate Limited - Try again in 20 seconds"):
        self.message = message
        super().__init__(self.message)
