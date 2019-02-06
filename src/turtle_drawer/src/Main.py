from Turtle import Turtle
from Vector import Vector


if __name__ == '__main__':
	turtle = Turtle()
	print (turtle.position.x)
	turtle.position = Vector(4, 5)
	print (str(turtle.position.x) + " , " + str(turtle.position.y))
