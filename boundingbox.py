# Class to hold the bounding boxes for the world

# Imports
from graphics import *

# Class
class BoundingBox:
    """AABB Collider"""
    def __init__(self, position, size):
        # Initialize variables
        self.pos = position
        self.size = size
        self.r = Rectangle(self.pos, Point(self.pos.getX() + self.size.getX(), self.pos.getY() + self.size.getY()))
        self.r.setFill("red")

    def move(self, x, y):
        """Moves bounding box"""
        self.pos = Point(self.pos.getX() + x, self.pos.getY() + y)

    def debugDraw(self, window):
        # Draws hitbox at the pos
        self.r.draw(window)

    def render(self):
        self.r.move(self.pos.getX() - self.r.getP1().getX(), self.pos.getY() - self.r.getP1().getY())

    def getCenter(self):
        """Returns the center"""
        return Point(self.pos.getX() + (self.size.getX() / 2), self.pos.getY() + (self.size.getY() / 2))

    @staticmethod
    def pointWithin(box, box2):
        """Returns true or false if another bounding box is within"""
        within = False

        # Box 1 positions
        b1X = box.pos.getX()
        b1Y = box.pos.getY()
        b1xSize = box.size.getX()
        b1ySize = box.size.getY()

        # Box 2 positions
        b2X = box2.pos.getX()
        b2Y = box2.pos.getY()
        b2xSize = box2.size.getX()
        b2ySize = box2.size.getY()

        # Check collision
        if b2X < b1X + b1xSize and b2X + b2xSize > b1X and b2Y < b1Y + b1ySize and b2Y + b2ySize > b1Y:
            within = True

        return within

    @staticmethod
    def positionCheck(box, position):
        """Returns true or false if a position is within the bounding box"""
        within = False

        # Box 1 positions
        b1X = box.pos.getX()
        b1Y = box.pos.getY()
        b1xSize = box.size.getX()
        b1ySize = box.size.getY()

        # Box 2 positions
        b2X = position.getX()
        b2Y = position.getY()

        # Check collision
        if b2X < b1X + b1xSize and b2X > b1X and b2Y < b1Y + b1ySize and b2Y > b1Y:
            within = True

        return within
