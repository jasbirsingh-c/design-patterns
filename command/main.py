from abc import ABC
from abc import abstractmethod


class Command(ABC):
    def __init__(self, receiver):
        self.receiver = receiver
    
    @abstractmethod
    def execute(self):
        pass

class CopyCommand(Command):
    def execute(self):
        self.receiver.copy()

class PasteCommand(Command):
    def execute(self):
        self.receiver.paste()

class Button(ABC):
    def store_command(self, command):
        self.command = command

class CopyButton(Button):
    def perform_action(self):
        self.command.execute()

class PasteButton(Button):
    def perform_action(self):
        self.command.execute()

class CutButton(Button):
    def perform_action(self):
        self.command.execute()

class Receiver:
    def copy(self):
        print("Copying data...")

    def paste(self):
        print("Pasting data...")

    def cut(self):
        print("Cutting data...")

if __name__ == "__main__":
    receiver = Receiver()
    copy_command = CopyCommand(receiver)
    paste_command = PasteCommand(receiver)

    copy_button = CopyButton()
    copy_button.store_command(copy_command)
    copy_button.perform_action()
