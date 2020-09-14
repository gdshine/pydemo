from abc import ABC, abstractmethod
from common.elements import Element


class Driver(ABC):

    @abstractmethod
    def get(self, url: str) -> None:
        pass

    @abstractmethod
    def set_page_load_timeout(self, time_to_wait: int) -> None:
        pass

    @abstractmethod
    def implicitly_wait(self, time_to_wait: int) -> None:
        pass

    @abstractmethod
    def find_element(self, by_: str, value: str) -> Element:
        pass

    @abstractmethod
    def maximize_window(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def get_screenshot_as_file(self,name: str) ->None:
        pass
