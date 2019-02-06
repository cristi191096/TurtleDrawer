from Vector import Vector
from Shapes import Shape

class Turtle:
    
    __turtles = 0
    
    def __init__(self):
        self.position = Vector(0, 0)
        self.shape = Shape()
        
        Turtle.__turtles += 1
        
    def SetShape(self, newShape):
        self.shape = newShape
        
    def OnDraw(self):
        self.shape.Draw()
        
    @property
    def ID(self):
        return Turtle.__turtles
        
    def Reset(self):
        self.position.SetEulerAngles(0, 0, 0)
        self.position.SetVector(0, 0)
        
    
