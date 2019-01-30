from Vector import Vector
from Shapes import Shape

class Turtle:
    
    def __init__(self):
        self.position = Vector(0, 0)
        self.shape = Shape()
        
    def SetShape(self, newShape):
        self.shape = newShape
        
    def OnDraw(self):
        self.shape.Draw()
        
    def Reset(self):
        self.position.SetEulerAngles(0)
        self.position.SetVector(0, 0)
        
    