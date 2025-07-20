from .client import Client
from .factories.motif_widget_factory import MotifWidgetFactory
from .factories.pm_widget_factory import PmWidgetFactory

class Main:
    def __init__(self):
        #widget_factory = MotifWidgetFactory()
        widget_factory = PmWidgetFactory()
        client = Client(widget_factory)
        client.create_ui()
        # ...

if __name__ == "__main__":
    main = Main()