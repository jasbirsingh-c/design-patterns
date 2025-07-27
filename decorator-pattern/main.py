from .components.window import Window
from .components.text_view import TextView
from .decorators.border_decorator import BorderDecorator
from .decorators.scroll_decorator import ScrollDecorator
from .decorators.line_no_decorator import LineDecorator

class Main:
    def __init__(self):
        window = Window()
        text_view = TextView()

        window.set_contents(LineDecorator(BorderDecorator(ScrollDecorator(text_view))))
        window.draw()

if __name__ == "__main__":
    Main()