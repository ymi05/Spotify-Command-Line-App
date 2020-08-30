class Error(Exception):
    """Base class for other exceptions"""
    pass

class ExpiredToken(Error):
    def __init__(self):
        self.message = "401: The access token expired"
        super().__init__(self.message)

