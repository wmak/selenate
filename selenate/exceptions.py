class SelenateException(Exception):
    pass

class SeleniumServerError(SelenateException):
    def __init__(self):
        self.msg = "Please start the selenium server"

class BrowserDeathError(SelenateException):
    def __init__(self):
        self.msg = "The browser died before you could complete that action"

class NonFormError(SelenateException):
    def __init__(self):
        self.msg = "Element was not in a form so couldn't submit"

class UnknownLocatorError(SelenateException):
    def __init__(self):
        self.msg = "Unknown locator type"
