# Holds the class for the cube that gives points

# Imports
from graphics import *
from boundingbox import *

# Class
class Square:
    """Point square"""
    def __init__(self, pos, type):
        self.pos = Point(pos.getX() - 5, pos.getY() - 5)
        self.boundingBox = BoundingBox(pos, Point(10, 10))
        self.value = 100 # The amount of points its worth
        self.type = type

        self.box = Rectangle(pos, Point(pos.getX() + 10, pos.getY() + 10))
        self.box.setFill("yellow")

    def draw(self, window):
        """Draws the box to the window"""
        self.box.draw(window)

    def update(self, player):
        """Updates the square"""
        #if BoundingBox.pointWithin(player, self.boundingBox):
        if BoundingBox.positionCheck(player, self.pos):
            return self.value
        else:
            return False
