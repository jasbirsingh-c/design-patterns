from ..components.visual_component import VisualComponent

class Decorator(VisualComponent):
    def __init__(self, component):
        self._component = component

    def draw(self):
        self._component.draw()
