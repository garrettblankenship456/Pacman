# Holds the player pacman

# Imports
from graphics import *
import time
import config
from boundingbox import *
import math

# Class defintion
class Player:
    def __init__(self, size = 30):
        # Initialize variables
        self.images = ()
        self.box = Rectangle(Point(0, 0), Point(size, size))
        self.boundingBox = BoundingBox(Point(config.WINDOW_WIDTH / 2 - 15, 670), Point(size, size))
        self.direction = "none"
        self.movmentSpeed = 0.05

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
        if self.direction == 'n':
            self.box.move(0, -self.movmentSpeed)
            self.boundingBox.move(0, -self.movmentSpeed)
        if self.direction == 's':
            self.box.move(0, self.movmentSpeed)
            self.boundingBox.move(0, self.movmentSpeed)
        if self.direction == 'e':
            self.box.move(self.movmentSpeed, 0)
            self.boundingBox.move(self.movmentSpeed, 0)
        if self.direction == 'w':
            self.box.move(-self.movmentSpeed, 0)
            self.boundingBox.move(-self.movmentSpeed, 0)
