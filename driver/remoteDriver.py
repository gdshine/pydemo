from common.elements import Element,WebElement
from driver.driver import Driver
from typing import Any
from selenium import webdriver
import os


class RemoteDriver(Driver):

    def __init__(self, url: str, browser: str) -> None:

        driver = webdriver.Remote(url, desired_capabilities=browser)
        self.driver = driver

    def get(self, url: str) -> None:
        self.driver.get(url)

    def set_page_load_timeout(self, time_to_wait: int) -> None:
        self.driver.set_page_load_timeout(time_to_wait)

    def implicitly_wait(self, time_to_wait: int) -> None:
        self.driver.implicitly_wait(time_to_wait)

    def find_element(self, by_: str, value: str) -> Element:
        return WebElement(self.driver.find_element(by_, value))

    def maximize_window(self) -> None:
        self.driver.maximize_window()

    def close(self) -> None:
        self.driver.close()
        self.driver.quit()

    def get_screenshot_as_file(self, name: str) -> None:
        self.driver.get_screenshot_as_file(name)

    def getPath(self):
        return os.getcwd()