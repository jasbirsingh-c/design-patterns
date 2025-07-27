from .decorator import Decorator

class ScrollDecorator(Decorator):
    def __init__(self, component):
        super().__init__(component)

    def draw(self):
        super().draw()
        self._scroll()

    def _scroll(self):
        print("Adding scrolling functionality")