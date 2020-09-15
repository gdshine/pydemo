from abc import ABC, abstractmethod
from typing import Any
from selenium.webdriver.support.wait import WebDriverWait
from driver.driver import Driver
from common.elements import Element
from selenium.webdriver.support.expected_conditions import presence_of_element_located as PresenceOfElement
from common.conditions import Condition


class Wait(ABC):
    """Wait for element abstraction."""

    @abstractmethod
    def until_presence_of_element_located(self, method: Condition, message: str = "") -> Element:
        pass

    @abstractmethod
    def until_not_presence_of_element_located(self, method: Condition, message: str = "") -> Element:
        pass

    @abstractmethod
    def presence_of_element_located(self) -> PresenceOfElement:
        pass


class WebDriverWaitOf(Wait):
    """Represent web driver wait object."""

    def __init__(self, driver: Driver, timeout: int = 10, poll_freq: float = 0.5, ign_exc: Any = None) -> None:
        self._wait: WebDriverWait = WebDriverWait(driver, timeout, poll_freq, ign_exc)

    def until_presence_of_element_located(self, method: Condition, message: str = "") -> Element:
        return self._wait.until(method.presence_of_element_located(), message)

    def until_not_presence_of_element_located(self, method: Condition, message: str = "") -> Element:
        return self._wait.until_not(method.presence_of_element_located(), message)