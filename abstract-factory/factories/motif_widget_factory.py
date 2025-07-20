from ..widgets.motif_scrollbar import MotifScrollbar
from ..widgets.motif_window import MotifWindow
from .widget_factory import WidgetFactory

class MotifWidgetFactory(WidgetFactory):
    def create_scrollbar(self):
        return MotifScrollbar()

    def create_window(self):
        return MotifWindow()