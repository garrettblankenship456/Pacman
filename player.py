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
    def __init__(self, window, world, size = 39):
        # Starting positions
        startX = config.WINDOW_WIDTH / 2 - 15
        startY = 525

        # Initialize variables
        self.box = Rectangle(Point(0, 0), Point(size, size))
        self.boundingBox = BoundingBox(Point(startX, startY), Point(size, size))
        self.projectedBox = BoundingBox(Point(startX, startY), Point(size, size))
        self.direction = "e"
        self.nextDirection = "e"
        self.movmentSpeed = 85
        self.score = 0
        self.life = 3 # Player has 3 lifes

        # Initialize food list
        self.foodlist = [Food(1, 1, "red", "blue", window)]

        for square in world.squares:
            f2 = None

            if square.type == "powerpellet":
                f2 = Food(square.pos.getX(), square.pos.getY(), "black", "blue", window)
                f2.powerpellet = True
            else:
                f2 = Food(square.pos.getX(), square.pos.getY(), "black", "blue", window)

            self.foodlist.append(f2)

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
        self.box.move(startX, startY)
        for p in self.images:
            p.move(startX + size / 2, startY + size / 2)

    def draw(self, window):
        """Draws player to the screen"""
        self.box.draw(window)

    def move(self, direction):
        """Moves player direction"""
        # Get projection position and see if it collides
        self.nextDirection = direction

    def respawn(self):
        """Respawns the player"""
        toPos = Point((config.WINDOW_WIDTH / 2 - 15) - self.boundingBox.pos.getX(), (525 - self.boundingBox.pos.getY()))
        self.boundingBox.move(toPos.getX(), toPos.getY())

        for i in self.images:
            i.move(toPos.getX(), toPos.getY())

    def update(self, window, world, deltaTime, ghosts):
        """Updates the player"""
        # Undraw images
        for p in self.images:
            p.undraw()

        # Change to new direction
        if self.nextDirection == "n":
            northProjection = BoundingBox(Point(self.boundingBox.pos.getX(), self.boundingBox.pos.getY() - 2), self.boundingBox.size)
            nCollision, box1 = world.isCollided(northProjection)

            if nCollision == False:
                self.direction = self.nextDirection
        elif self.nextDirection == "s":
            southProjection = BoundingBox(Point(self.boundingBox.pos.getX(), self.boundingBox.pos.getY() + 2), self.boundingBox.size)
            sCollision, box2 = world.isCollided(southProjection)

            if sCollision == False:
                self.direction = self.nextDirection
        elif self.nextDirection == "e":
            eastProjection = BoundingBox(Point(self.boundingBox.pos.getX() + 2, self.boundingBox.pos.getY()), self.boundingBox.size)
            eCollision, box3 = world.isCollided(eastProjection)

            if eCollision == False:
                self.direction = self.nextDirection
        elif self.nextDirection == "w":
            westProjection = BoundingBox(Point(self.boundingBox.pos.getX() - 2, self.boundingBox.pos.getY()), self.boundingBox.size)
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
                if i.powerpellet == True:
                    # Scare all the ghosts, its a power pellet
                    for g in ghosts:
                        g.scare()

                i.drawFood()

                # Remove food
                self.foodlist.remove(i)

                # Add points
                self.score += 10

        # Death from ghost touch or win from no points left
        for g in ghosts:
            if BoundingBox.pointWithin(self.boundingBox, g.boundingBox):
                # If they arent scared, pacman is dead
                if g.scared == False:
                    # Count down
                    self.life -= 1

                    # Close game if less than 3 lifes
                    if self.life < 1:
                        return True
                    else:
                        time.sleep(1)
                        self.respawn()

                        # Respawn all the ghosts
                        for g in ghosts:
                            g.respawn(world, True)

                        return 2
                else: # They are scared so theyre worth points
                    if g.alive == True:
                        print("Ghost eaten")
                        self.score += 200
                        g.respawn(world)

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
