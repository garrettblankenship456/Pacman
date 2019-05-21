from graphics import *
from world import *
from boundingbox import *
import time
import random

class Ghost(object):
    """Ghosts"""
    def __init__(self, name, pos, window):
        self.pos = pos
        self.name = name
        self.images = (Image(pos, "images/ghosts/" + name + "1.png"),
                       Image(pos, "images/ghosts/" + name + "2.png"),
                       Image(pos, "images/ghosts/scared1.png"),
                       Image(pos, "images/ghosts/dead.png"))
        self.frame = False
        self.a = True
        self.startPos = pos
        print(self.startPos)

        # Draw the first image
        self.images[0].draw(window)

        self.boundingBox = BoundingBox(Point(pos.getX() - (39 / 2), pos.getY() - (39 / 2)), Point(39, 39))

        # Path finding variables
        self.ghostPathIndex = 0
        self.path = []
        self.lastTracked = 0
        self.scared = False
        self.alive = True
        self.firstTickScared = False
        self.lastScared = 0

    def scare(self):
        """Scares the ghost"""
        self.scared = True
        self.lastScared = time.time()
        self.firstTickScared = True

    def moveGhost(self, world, targetPos, multiplier = 1):
        projected = [0, 0]

        # Paths based on if its headed to, or running from
        projected[0] = ((targetPos.getX() + 20) - (self.boundingBox.pos.getX() + self.boundingBox.size.getX() / 2)) * multiplier
        projected[1] = ((targetPos.getY() + 20) - (self.boundingBox.pos.getY() + self.boundingBox.size.getY() / 2)) * multiplier

        # Normalization
        X = 0
        Y = 0
        if projected[0] > 0:
            X = 0.1 * multiplier

            # Set direction based on projected
            self.a = False
        elif projected[0] < 0:
            X = -0.1 * multiplier

            # Set direction based on projected
            self.a = True

        if projected[1] > 0:
            Y = 0.1 * multiplier
        elif projected[1] < 0:
            Y = -0.1 * multiplier

        # Collision detection in north-south
        xProjection = BoundingBox(Point(self.boundingBox.pos.getX() + X, self.boundingBox.pos.getY()),
                                      self.boundingBox.size)
        yProjection = BoundingBox(Point(self.boundingBox.pos.getX(), self.boundingBox.pos.getY() + Y),
                                      self.boundingBox.size)

        xCollision, box = world.isCollided(xProjection)
        yCollision, box = world.isCollided(yProjection)
        if xCollision:
            X = 0

        if yCollision:
            Y = 0

        self.boundingBox.move(X, Y)

    def update(self, player, world, deltaTime):
        """Updates the ghost entirely, moves it and path finds accordingly"""
        if self.ghostPathIndex > len(self.path) - 1 or time.time() > self.lastTracked + 15 or self.firstTickScared == True:
            self.ghostPathIndex = 0
            self.firstTickScared = False

            plyGridX = int((player.boundingBox.pos.getX()) // world.nodeGrid.xScale) - 1
            plyGridY = int((player.boundingBox.pos.getY()) // world.nodeGrid.yScale) + 1
            ghostGridX = int((self.boundingBox.pos.getX()) // world.nodeGrid.xScale) - 1
            ghostGridY = int((self.boundingBox.pos.getY()) // world.nodeGrid.yScale) + 1

            # Reset alive if its made it
            if self.alive == False:
                self.alive = True
                self.scared = False

            if self.scared == True:
                # Make ghost to a random point
                randNode = world.nodeGrid.randomNode()
                self.path = world.nodeGrid.pathFind(world.nodeGrid.nodeList[ghostGridX][ghostGridY], randNode)

                # End scared status
                if time.time() > self.lastScared + 7:
                    self.scared = False
            else:
                try:
                    self.path = world.nodeGrid.pathFind(world.nodeGrid.nodeList[ghostGridX][ghostGridY], world.nodeGrid.nodeList[plyGridX][plyGridY])
                except:
                    print("error")

            self.lastTracked = time.time()

        if self.ghostPathIndex < len(self.path) or self.lastTracked == 0:
            notAlive = not self.alive
            self.moveGhost(world, Point(self.path[self.ghostPathIndex].realPosX, self.path[self.ghostPathIndex].realPosY), (835 - (240 * self.scared) + (600 * notAlive)) * deltaTime)

        if BoundingBox.pointWithin(self.boundingBox, BoundingBox(Point(self.path[self.ghostPathIndex].realPosX, self.path[self.ghostPathIndex].realPosY), Point(world.nodeGrid.xScale, world.nodeGrid.yScale))):
            self.ghostPathIndex += 1

    def render(self, window):
        """Draws all the images in the correct position"""
        # Update images
        for i in self.images:
            i.undraw()

        if self.alive == False:
            self.images[3].draw(window)
        elif self.scared == True:
            self.images[2].draw(window)
        elif self.a == True:
            self.images[0].draw(window)
        elif self.a == False:
            self.images[1].draw(window)

        # Move images
        toX = (self.boundingBox.pos.getX() - (self.images[0].getAnchor().getX() - 20))
        toY = (self.boundingBox.pos.getY() - (self.images[0].getAnchor().getY() - 20))

        for i in self.images:
            i.move(toX, toY)

    def respawn(self, world, force = False):
        """Path finds back to the home"""
        if force == False:
            # Get position
            ghostGridX = int((self.boundingBox.pos.getX()) // world.nodeGrid.xScale) - 1
            ghostGridY = int((self.boundingBox.pos.getY()) // world.nodeGrid.yScale) + 1

            # Set attributes and path find
            self.alive = False
            self.ghostPathIndex = 0
            self.lastTracked = time.time() + 3489326784 # Forces the last tracked to always be the most
            self.path = world.nodeGrid.pathFind(world.nodeGrid.nodeList[ghostGridX][ghostGridY], world.nodeGrid.nodeList[31][34])
        else:
            # Get position
            toX = self.startPos.getX() - self.boundingBox.pos.getX() - (39 / 2)
            toY = self.startPos.getY() - self.boundingBox.pos.getY() - (39 / 2)

            self.alive = True
            self.scared = False
            self.ghostPathIndex = 0
            self.lastTime = time.time() + 321312412

            # Move it all
            self.boundingBox.move(toX, toY)
