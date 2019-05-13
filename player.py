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
        self.box = Rectangle(Point(0, 0), Point(size, size))
        self.boundingBox = BoundingBox(Point(config.WINDOW_WIDTH / 2 - 15, 655), Point(size, size))
        self.projectedBox = BoundingBox(Point(config.WINDOW_WIDTH / 2 - 15, 655), Point(size, size))
        self.direction = "e"
        self.nextDirection = "e"
        self.movmentSpeed = 0.15
        self.score = 0

        # Animation variables
        self.images = (Image(Point(0, 0), "images/directions/center.png"),
                       Image(Point(0, 0), "images/directions/northFirst.png"),
                       Image(Point(0, 0), "images/directions/southFirst.png"),
                       Image(Point(0, 0), "images/directions/eastFirst.png"),
                       Image(Point(0, 0), "images/directions/westFirst.png"))
        self.frame = 0 # Holds the frame, if its facing a direction or center
        self.animationDelay = 0.1
        self.lastFrameTime = time.time()

        # Move graphics box and setfill
        self.box.move(config.WINDOW_WIDTH / 2 - 15, 655)
        for p in self.images:
            p.move(config.WINDOW_WIDTH / 2 - 15 + size / 2, 655 + size / 2)

    def draw(self, window):
        """Draws player to the screen"""
        self.box.draw(window)

    def move(self, direction):
        """Moves player direction"""
        # Get projection position and see if it collides
        self.nextDirection = direction

    def update(self, window, world, deltaTime):
        """Updates the player"""
        # Undraw images
        for p in self.images:
            p.undraw()

        # Velocity projection
        projected = [0, 0]
        if self.direction == 'n':
            # Calculate velocities
            projected[0] = 0
            projected[1] = -self.movmentSpeed

            # Draw image
            if self.frame == 0:
                self.images[0].draw(window)
            else:
                self.images[1].draw(window)
        if self.direction == 's':
            # Calculate velocities
            projected[0] = 0
            projected[1] = self.movmentSpeed

            # Draw image
            if self.frame == 0:
                self.images[0].draw(window)
            else:
                self.images[2].draw(window)
        if self.direction == 'e':
            # Calculate velocities
            projected[0] = self.movmentSpeed
            projected[1] = 0

            # Draw image
            if self.frame == 0:
                self.images[0].draw(window)
            else:
                self.images[3].draw(window)
        if self.direction == 'w':
            # Calculate velocities
            projected[0] = -self.movmentSpeed
            projected[1] = 0

            # Draw image
            if self.frame == 0:
                self.images[0].draw(window)
            else:
                self.images[4].draw(window)

        # Get normalized movement
        X = 0
        Y = 0
        if projected[0] > 0:
            X = -0.1
        elif projected[0] < 0:
            X = 0.1

        if projected[1] > 0:
            Y = -0.1
        elif projected[1] < 0:
            Y = 0.1

        # Get projected boundingbox
        self.projectedBox.pos = Point(self.boundingBox.pos.getX() - X, self.boundingBox.pos.getY() - Y)
        northProjection = BoundingBox(Point(self.boundingBox.pos.getX(), self.boundingBox.pos.getY() - 1), self.boundingBox.size)
        southProjection = BoundingBox(Point(self.boundingBox.pos.getX(), self.boundingBox.pos.getY() + 1), self.boundingBox.size)
        eastProjection = BoundingBox(Point(self.boundingBox.pos.getX() + 1, self.boundingBox.pos.getY()), self.boundingBox.size)
        westProjection = BoundingBox(Point(self.boundingBox.pos.getX() - 1, self.boundingBox.pos.getY()), self.boundingBox.size)

        # Check collision based on projected position
        collision, box = world.isCollided(self.projectedBox)
        nCollision, box = world.isCollided(northProjection)
        sCollision, box = world.isCollided(southProjection)
        eCollision, box = world.isCollided(eastProjection)
        wCollision, box = world.isCollided(westProjection)

        if collision:
            # Zero out velocity
            projected[0] = X
            projected[1] = Y

        # Change to new direction
        if self.nextDirection == "n":
            if nCollision == False:
                self.direction = self.nextDirection
        elif self.nextDirection == "s":
            if sCollision == False:
                self.direction = self.nextDirection
        elif self.nextDirection == "e":
            if eCollision == False:
                self.direction = self.nextDirection
        elif self.nextDirection == "w":
            if wCollision == False:
                self.direction = self.nextDirection

        # Teleport if needed
        onTp = world.onTeleporter(self.projectedBox)
        if onTp != False:
            projected[0] = onTp.getX() - self.boundingBox.pos.getX()
            projected[1] = onTp.getY() - self.boundingBox.pos.getY()

        # Handle points
        """for p in world.squares:
            onPoint = p.update(self.boundingBox)
            if onPoint != False:
                #print("Got point")
                p.box.undraw()
                world.squares.remove(p)
                break"""

        # Update animation only if the player hasnt collided with anything
        if self.lastFrameTime + self.animationDelay < time.time():
            self.frame = not self.frame
            self.lastFrameTime = time.time()

        for p in self.images:
            p.move(projected[0], projected[1])

        # Move the box to the projected
        self.box.move(projected[0], projected[1])
        self.boundingBox.move(projected[0], projected[1])
