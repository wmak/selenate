from .exceptions import UnknownLocatorError, NonFormError

class SelenateElement():
    def __init__(self, driver, locator):
        if "=" in locator:
            locator_type = locator[:locator.find("=")].lower()
            locator_value = locator[locator.find("=") + 1:]
        else:
            locator_type = 'css'
            locator_value = locator

        if locator_type == 'class':
            self.element = driver.find_element_by_class_name(locator_value)
        elif locator_type == 'css':
            self.element = driver.find_element_by_css_selector(locator_value)
        elif locator_type == 'id':
            self.element = driver.find_element_by_id(locator_value)
        else:
            raise UnknownLocatorError

    def attribute(self, value):
        return self.element.get_attribute(value)
    
    def click(self):
        self.element.click()

    def css(self, value):
        return self.element.value_of_css_property(value)

    @property
    def visible(self):
        return self.element.is_displayed()

    @property
    def enabled(self):
        return self.element.is_enabled()

    @property
    def id(self):
        return self.element.id

    @property
    def location(self):
        return self.element.location

    @property
    def scrolled_location(self):
        location = self.element.location_once_scrolled_into_view
        return {"x" : location.get("x"), "y" : location.get("y")}

    @property
    def size(self):
        return self.element.size

    @property
    def selected(self):
        return self.element.is_selected()

    def submit(self):
        try:
            self.element.submit()
        except NoSuchElementException:
            raise NonFormError

    @property
    def tag(self):
        return self.element.tag_name

    @property
    def text(self):
        return self.element.text

    @text.setter
    def text(self, value):
        self.element.send_keys(value)
