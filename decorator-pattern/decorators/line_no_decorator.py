from .decorator import Decorator

class LineDecorator(Decorator):
    def __init__(self, component):
        self.component = component 

    def draw(self):
        self.component.draw()
        self.draw_line()

    def draw_line(self):
        print("Adding line functionality")