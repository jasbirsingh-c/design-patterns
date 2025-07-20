from abc import ABC, abstractmethod

class HelpHandler(ABC):
    
    def handleHelp(self):
        self.handler.handleHelp()

    def setHandler(self, handler, topic):
        self.handler = handler
        self.topic = topic


class Widget(HelpHandler):
    def __init__(self, handler, topic):
        self.setHandler(handler, topic)

    def handleHelp(self):
        if (self.topic == 'widget'):
            print('Widget help')
        else:
            self.handler.handleHelp()    

class Dialog(Widget):
    def __init__(self, handler, topic):
        self.setHandler(handler, topic)

    def handleHelp(self):
        if (self.topic == 'dialog'):
            print('Dialog help')
        else:
            self.handler.handleHelp()

class Button(Widget):
    def __init__(self, handler, topic):
        self.setHandler(handler, topic)

    def handleHelp(self):
        if (self.topic == 'button'):
            print('Button help')
        else:
            self.handler.handleHelp()

widget = Widget(0, 'widget')
dialog = Dialog(widget, 'dialog')
button = Button(dialog, 'widgetss')

button.handleHelp()


