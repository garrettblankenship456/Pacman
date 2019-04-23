# Holds the player pacman

# Imports
from graphics import *
import time
import config
from boundingbox import *
import math

# Class defintion
class Player:
    def __init__(self, size = 39.5):
        # Initialize variables
        self.images = (Image())
        self.box = Rectangle(Point(0, 0), Point(size, size))
        self.boundingBox = BoundingBox(Point(config.WINDOW_WIDTH / 2 - 15, 670), Point(size, size))
        self.projectedBox = BoundingBox(Point(config.WINDOW_WIDTH / 2 - 15, 670), Point(size, size))
        self.direction = "none"
        self.movmentSpeed = 0.1

        # Move graphics box and setfill
        self.box.setFill("blue")
        self.box.move(config.WINDOW_WIDTH / 2 - 15, 670)

    def draw(self, window):
        """Draws player to the screen"""
        self.box.draw(window)

    def move(self, direction):
        """Moves player direction"""
        # Get projection position and see if it collides
        self.direction = direction

    def update(self, world):
        """Updates the player"""
        # Velocity projection
        projected = [0, 0]
        if self.direction == 'n':
            projected[0] = 0
            projected[1] = -self.movmentSpeed
        if self.direction == 's':
            projected[0] = 0
            projected[1] = self.movmentSpeed
        if self.direction == 'e':
            projected[0] = self.movmentSpeed
            projected[1] = 0
        if self.direction == 'w':
            projected[0] = -self.movmentSpeed
            projected[1] = 0

        # Get projected boundingbox
        self.projectedBox.pos = Point(self.boundingBox.pos.getX() + projected[0], self.boundingBox.pos.getY() + projected[1])

        # Check collision based on projected position
        collision, box = world.isCollided(self.projectedBox)
        if collision:
            projected[0] = 0
            projected[1] = 0

        # Move the box to the projected
        self.box.move(projected[0], projected[1])
        self.boundingBox.move(projected[0], projected[1])
