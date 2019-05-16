# Holds the player pacman

# Imports
from graphics import *
import time
import config
from boundingbox import *
import math
from food import *

# Class defintion
class Player:
    def __init__(self, window, size = 39.5):
        # Initialize variables
        self.box = Rectangle(Point(0, 0), Point(size, size))
        self.boundingBox = BoundingBox(Point(config.WINDOW_WIDTH / 2 - 15, 655), Point(size, size))
        self.projectedBox = BoundingBox(Point(config.WINDOW_WIDTH / 2 - 15, 655), Point(size, size))
        self.direction = "e"
        self.nextDirection = "e"
        self.movmentSpeed = 120
        self.score = 0

        # Initialize food list
        xvalues = [37, 217, 337, 337, 537, 597, 597, 417, 477, 37, 217, 157, 497, 37, 57, 77, 97, 117, 137, 157, 157,
                   157, 157, 157, 157, 137, 117, 97, 77, 57, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 57,
                   77, 97, 117, 137, 157, 157, 157, 157, 177, 197, 217, 237, 257, 277, 297, 317, 337, 357, 377, 397,
                   417, 437, 457, 477, 497, 517, 537, 557, 577, 597, 597, 597, 597, 597, 597, 577, 557, 537, 517, 497,
                   477, 477, 477, 477, 477, 477, 457, 437, 417, 397, 377, 357, 357, 357, 357, 357, 357, 377, 397, 417,
                   437, 457, 477, 477, 477, 477, 477, 477, 477, 477, 477, 497, 517, 537, 557, 577, 597, 597, 597, 597,
                   597, 597, 597, 577, 557, 537, 517, 497, 477, 477, 477, 477, 477, 477, 477, 477, 497, 517, 537, 557,
                   577, 597, 577, 557, 537, 517, 497, 477, 457, 437, 417, 417, 417, 417, 417, 397, 377, 357, 337, 337,
                   337, 337, 357, 377, 397, 417, 417, 417, 417, 397, 377, 357, 337, 317, 297, 277, 277, 277, 277, 277,
                   277, 257, 237, 217, 197, 177, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157,
                   157, 157, 137, 117, 97, 77, 57, 37, 17, 37, 57, 77, 97, 117, 137, 157, 177, 197, 217, 217, 217, 217,
                   217, 237, 257, 277, 277, 277, 277, 257, 237, 217, 217, 217, 217, 217, 217, 217, 237, 257, 277, 277,
                   277, 277, 297, 317, 337, 357, 377, 397, 417, 417, 417, 417, 417, 417, 417, 417, 417, 417, 417, 437,
                   457, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 477, 497, 517, 537, 557, 577, 597,
                   597, 597, 597, 577, 557, 537, 537, 537, 537, 537, 557, 577, 597, 597, 597, 597, 577, 557, 537, 517,
                   497, 477, 457, 437, 417, 397, 377, 357, 337, 317, 297, 277, 257, 237, 217, 197, 177, 157, 137, 117,
                   97, 77, 57, 37, 37, 37, 37, 57, 77, 97, 97, 97, 97, 97, 77, 57, 37, 37, 37, 37, 57, 77, 97, 117, 137,
                   157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 157, 177, 197, 217, 217, 217, 217, 217,
                   217, 217, 217, 217, 217, 237, 257, 277, 297, 317, 337, 357, 377, 397, 417, 417, 417, 417, 397, 377,
                   357, 337, 337, 337, 337, 357, 377, 397, 417, 437, 457, 477, 477, 477, 477, 477, 477, 477, 477, 477,
                   477, 477, 497, 517, 537, 517, 497, 477, 477, 477, 477, 477, 457, 437, 417, 417, 417, 417, 417, 397,
                   377, 357, 337, 337, 337, 337, 317, 297, 277, 277, 277, 277, 257, 237, 217, 217, 217, 217, 217, 197,
                   177, 157, 157, 157, 157, 157, 137, 117, 97, 117, 137, 157, 157, 157, 157, 157, 177, 197, 217, 237,
                   257, 277, 297, 317, 337, 317, 297, 277, 277, 277, 277, 257, 237, 217]
        yvalues = [686, 626, 486, 626, 546, 626, 486, 226, 66, 546, 486, 66, 66, 66, 66, 66, 66, 66, 66, 86, 106, 126,
                   146, 166, 166, 166, 166, 166, 166, 166, 146, 126, 106, 86, 66, 86, 106, 126, 146, 166, 186, 206, 226,
                   226, 226, 226, 226, 226, 226, 206, 186, 166, 166, 166, 166, 166, 166, 166, 166, 166, 166, 166, 166,
                   166, 166, 166, 166, 166, 166, 166, 166, 166, 166, 166, 146, 126, 106, 86, 66, 66, 66, 66, 66, 66, 66,
                   86, 106, 126, 146, 166, 166, 166, 166, 166, 166, 166, 146, 126, 106, 86, 66, 66, 66, 66, 66, 66, 66,
                   86, 106, 126, 146, 166, 186, 206, 226, 226, 226, 226, 226, 226, 226, 206, 186, 166, 186, 206, 226,
                   226, 226, 226, 226, 226, 226, 246, 266, 286, 306, 326, 346, 366, 366, 366, 366, 366, 366, 366, 366,
                   366, 366, 366, 366, 366, 366, 366, 366, 346, 326, 306, 286, 286, 286, 286, 286, 266, 246, 226, 226,
                   226, 226, 226, 206, 186, 166, 166, 166, 166, 166, 166, 166, 166, 146, 126, 106, 86, 66, 66, 66, 66,
                   66, 66, 66, 86, 106, 126, 146, 166, 186, 206, 226, 246, 266, 286, 306, 326, 346, 366, 366, 366, 366,
                   366, 366, 366, 366, 366, 366, 366, 366, 366, 366, 366, 366, 366, 366, 346, 326, 306, 286, 286, 286,
                   286, 266, 246, 226, 226, 226, 226, 206, 186, 166, 186, 206, 226, 226, 226, 226, 246, 266, 286, 286,
                   286, 286, 286, 286, 286, 286, 306, 326, 346, 366, 386, 406, 426, 446, 466, 486, 486, 486, 486, 466,
                   446, 426, 406, 386, 366, 386, 406, 426, 446, 466, 486, 486, 486, 486, 486, 486, 486, 506, 526, 546,
                   546, 546, 546, 566, 586, 606, 626, 626, 626, 626, 646, 666, 686, 686, 686, 686, 686, 686, 686, 686,
                   686, 686, 686, 686, 686, 686, 686, 686, 686, 686, 686, 686, 686, 686, 686, 686, 686, 686, 686, 686,
                   686, 666, 646, 626, 626, 626, 626, 606, 586, 566, 546, 546, 546, 546, 526, 506, 486, 486, 486, 486,
                   486, 486, 486, 466, 446, 426, 406, 386, 366, 386, 406, 426, 446, 466, 486, 486, 486, 486, 466, 446,
                   426, 406, 386, 366, 386, 406, 426, 426, 426, 426, 426, 426, 426, 426, 426, 426, 426, 446, 466, 486,
                   486, 486, 486, 486, 506, 526, 546, 546, 546, 546, 546, 546, 546, 546, 526, 506, 486, 506, 526, 546,
                   566, 586, 606, 626, 626, 626, 626, 626, 626, 626, 606, 586, 566, 546, 546, 546, 546, 566, 586, 606,
                   626, 626, 626, 626, 626, 646, 666, 686, 686, 686, 686, 666, 646, 626, 626, 626, 626, 606, 586, 566,
                   546, 546, 546, 546, 566, 586, 606, 626, 626, 626, 626, 626, 626, 626, 606, 586, 566, 546, 546, 546,
                   546, 546, 546, 546, 546, 546, 546, 546, 546, 546, 526, 506, 486, 486, 486, 486]
        self.foodlist = []

        a = 0
        while a < len(xvalues) - 1:
            f2 = Food(xvalues[a], yvalues[a], "red", "blue", window)
            self.foodlist.append(f2)
            a += 1

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

    def update(self, window, world, deltaTime, ghosts):
        """Updates the player"""
        # Undraw images
        for p in self.images:
            p.undraw()

        # Change to new direction
        if self.nextDirection == "n":
            northProjection = BoundingBox(Point(self.boundingBox.pos.getX(), self.boundingBox.pos.getY() - 1), self.boundingBox.size)
            nCollision, box1 = world.isCollided(northProjection)

            if nCollision == False:
                self.direction = self.nextDirection
        elif self.nextDirection == "s":
            southProjection = BoundingBox(Point(self.boundingBox.pos.getX(), self.boundingBox.pos.getY() + 1), self.boundingBox.size)
            sCollision, box2 = world.isCollided(southProjection)

            if sCollision == False:
                self.direction = self.nextDirection
        elif self.nextDirection == "e":
            eastProjection = BoundingBox(Point(self.boundingBox.pos.getX() + 1, self.boundingBox.pos.getY()), self.boundingBox.size)
            eCollision, box3 = world.isCollided(eastProjection)

            if eCollision == False:
                self.direction = self.nextDirection
        elif self.nextDirection == "w":
            westProjection = BoundingBox(Point(self.boundingBox.pos.getX() - 1, self.boundingBox.pos.getY()), self.boundingBox.size)
            wCollision, box4 = world.isCollided(westProjection)

            if wCollision == False:
                self.direction = self.nextDirection

        # Velocity projection
        projected = [0, 0]
        if self.direction == 'n':
            # Calculate velocities
            projected[0] = 0
            projected[1] = -self.movmentSpeed * deltaTime

            # Draw image
            if self.frame == 0:
                self.images[0].draw(window)
            else:
                self.images[1].draw(window)
        if self.direction == 's':
            # Calculate velocities
            projected[0] = 0
            projected[1] = self.movmentSpeed * deltaTime

            # Draw image
            if self.frame == 0:
                self.images[0].draw(window)
            else:
                self.images[2].draw(window)
        if self.direction == 'e':
            # Calculate velocities
            projected[0] = self.movmentSpeed * deltaTime
            projected[1] = 0

            # Draw image
            if self.frame == 0:
                self.images[0].draw(window)
            else:
                self.images[3].draw(window)
        if self.direction == 'w':
            # Calculate velocities
            projected[0] = -self.movmentSpeed * deltaTime
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

        # Check collision based on projected position
        collision, box = world.isCollided(self.projectedBox)

        if collision:
            # Get intersection
            xIntersect = min(box.pos.getX() + box.size.getX(), self.boundingBox.pos.getX() + self.boundingBox.size.getX()) - max(box.pos.getX(), self.boundingBox.pos.getX())
            yIntersect = min(box.pos.getY() + box.size.getY(), self.boundingBox.pos.getY() + self.boundingBox.size.getY()) - max(box.pos.getY(), self.boundingBox.pos.getY())

            # Zero out velocity
            if not X == 0:
                projected[0] = xIntersect * (X * 10)

            if not Y == 0:
                projected[1] = yIntersect * (Y * 10)

        # Teleport if needed
        onTp = world.onTeleporter(self.projectedBox)
        if onTp != False:
            projected[0] = onTp.getX() - self.boundingBox.pos.getX()
            projected[1] = onTp.getY() - self.boundingBox.pos.getY()

        # Handle points
        for i in self.foodlist:
            if i.eaten(self.boundingBox.pos.getX(), self.boundingBox.pos.getY()):
                i.undrawFood()

                # Remove food
                self.foodlist.remove(i)

                # Add points
                self.score += 10

        # Death from ghost touch or win from no points left
        for g in ghosts:
            if BoundingBox.pointWithin(self.boundingBox, g.boundingBox):
                print("Death")
                return True

        if len(self.foodlist) == 0:
            print("Win")
            return True

        # Update animation only if the player hasnt collided with anything
        if self.lastFrameTime + self.animationDelay < time.time():
            self.frame = not self.frame
            self.lastFrameTime = time.time()

        for p in self.images:
            p.move(projected[0], projected[1])

        # Move the box to the projected
        self.box.move(projected[0], projected[1])
        self.boundingBox.move(projected[0], projected[1])

        # Return false, (alive)
        return False
