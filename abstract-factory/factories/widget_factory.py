from abc import ABC, abstractmethod

class WidgetFactory(ABC):
    @abstractmethod
    def create_scrollbar():
        pass

    @abstractmethod
    def create_window():
        pass