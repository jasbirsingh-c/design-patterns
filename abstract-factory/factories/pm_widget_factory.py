from ..widgets.pm_scrollbar import PmScrollbar
from ..widgets.pm_window import PmWindow
from .widget_factory import WidgetFactory

class PmWidgetFactory(WidgetFactory):
    def create_scrollbar(self):
        return PmScrollbar()

    def create_window(self):
        return PmWindow()