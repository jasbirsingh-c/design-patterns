from .factories.widget_factory import WidgetFactory

class Client:
    def __init__(self, widget_factory: WidgetFactory):
        self.widget_factory = widget_factory

    def create_ui(self): 
        self.scrollbar = self.widget_factory.create_scrollbar()
        self.window = self.widget_factory.create_window()
        # ...