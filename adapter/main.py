from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def BoundingBox(self):
        pass

    @abstractmethod
    def CreateManipulator(self):
        pass

class DrawingEditor:
    def __init__(self, shape: Shape):
        self.shape = shape

    def Draw(self):
        print("DrawingEditor Draw...")
        self.shape.BoundingBox()

class Line(Shape):
    def BoundingBox(self):
        pass

    def CreateManipulator(self):
        pass

#adaptee
class TextView:
    def GetExtent(self):
        print("TextView GetExtent")

#adapter: it adapts the interface of TextView (GetExtend) to the interface of Shape
class TextShape(Shape):
    text_view = TextView()
    
    def BoundingBox(self):
        self.text_view.GetExtent()

    def CreateManipulator(self):
        pass

#main
if __name__ == "__main__":
    text_shape = TextShape()
    editor = DrawingEditor(text_shape)
    editor.Draw()