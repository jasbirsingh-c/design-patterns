from .visual_component import VisualComponent

class Window(VisualComponent):
    def __init__(self):
        self.component = None

    def set_contents(self, component):
        self.component = component

    def draw(self):
        self.component.draw()
