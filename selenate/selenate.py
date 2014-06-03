from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType 
from selenium.webdriver.common.keys import Keys

import socket
from os import path, devnull
import subprocess

from .exceptions import SeleniumServerError, BrowserDeathError
from .elements import SelenateElement

from urllib2 import URLError
import time
import signal

import pydoc

def _server_started():
    try: # check if the selenium server has been started locally
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return sock.connect_ex(("127.0.0.1", 4444)) == 0
    except:
        return True # Assume it's started if sock errors out

class _Selenium():
    def __init__(self, server):
        with open(devnull, "w") as fnull:
            self.selenium = subprocess.Popen(["java", "-jar", server],
                stdout=fnull, stderr=fnull)
        while not _server_started():
            time.sleep(0.5) # still not the best but better than before.
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

    def kill(self):
        self.selenium.terminate()
        self.selenium.kill()

    def _signal_handler(self, signum, frame):
        self.kill()
        raise KeyboardInterrupt

class Selenate():
    ''' Initiate a Selenate Object which is secretly a selenium object, A proxy
    can be supplied if so desired otherwise will run locally. Also unless 
    specified Selenate will be a firefox browser.'''
    def __init__(self, host="127.0.0.1", server="./selenium-server.jar"):
        if server and path.isfile(server) and not _server_started():
            self.selenium = _Selenium(server)

        proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': host,
            'ftpProxy': host,
            'sslProxy': host,
            'noProxy': host 
        })
        caps = webdriver.DesiredCapabilities.FIREFOX
        proxy.add_to_capabilities(caps)
        try:
            self.driver = webdriver.Remote(desired_capabilities=caps)
        except URLError:
            raise SeleniumServerError

    ''' Find an element by a variety of locators, using the format
    "type=locator" (ie "id=some_identifier") ''' 
    def find_element_by_locator(self, locator):
        try:
            element = SelenateElement(self.driver, locator)
        except Exception as e:
            self.quit()
            raise e
        return SelenateElement(self.driver, locator)

    ''' Have the browser go to some url '''
    def get(self, link):
        try:
            self.driver.get(link)
        except Exception as e:
            self.quit()
            raise e

    ''' Wait for a locator to be displayed before continuing, or timeout if this
    takes more than timeout seconds '''
    def wait_for(self, locator, timeout=10):
        try:
            w = WebDriverWait(self.driver, timeout)
            w.until(lambda driver: 
                self.driver.find_element_by_locator(locator).is_displayed())
        except Exception as e:
            self.quit()
            raise e

    ''' Click on an element identified by locator on the page '''
    def click(self, locator):
        try:
            self.find_element_by_locator(locator).click()
        except Exception as e:
            self.quit()
            raise e

    ''' Exit the browser '''
    def quit(self):
        try:
            self.driver.quit()
        except:
            raise BrowserDeathError
        if hasattr(self, "selenium"):
            self.selenium.kill()
