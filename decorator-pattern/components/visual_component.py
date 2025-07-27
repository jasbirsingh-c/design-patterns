from abc import ABC, abstractmethod

class VisualComponent(ABC):
    @abstractmethod
    def draw():
        pass
