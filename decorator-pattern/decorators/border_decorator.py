from .decorator import Decorator

class BorderDecorator(Decorator):
    def __init__(self, component):
        super().__init__(component)

    def draw(self):
        super().draw()
        self._add_border()

    def _add_border(self):
        print("Adding border functionality")