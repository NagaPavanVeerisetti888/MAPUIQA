class ElementNotFoundException(Exception):
    """Exception raised when an element is not found on a page."""
    def __init__(self, locator, message="Element not found"):
        self.locator = locator
        self.message = f"{message}: {locator}"
        super().__init__(self.message)


class NavigationException(Exception):
    """Exception raised for navigation error."""
    def __init__(self, message="Navigation error."):
        self.message = message
        super().__init__(self.message)

class LoginPageException(Exception):
    """Exception raised for error in the login page."""
    def __init__(self, message="Login page error."):
        self.message = message
        super().__init__(self.message)


# TODO write custom exception for welcomepage not visible