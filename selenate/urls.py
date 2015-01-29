from .exceptions import UnknownLocatorError, NonFormError

class SelenateUrl():
    def __init__(self, driver):
        self.cookies = driver.get_cookies()
        self.source = driver.page_source
        self.title = driver.title
        self.url = driver.current_url
        self.driver = driver
    
