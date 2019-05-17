from graphics import *
from world import *
from boundingbox import *
import time
import random

class Ghost(object):
    """Ghosts"""
    def __init__(self, name, pos):
        self.pos = pos
        self.name = name
        self.images = (Image(pos, "images/ghosts/" + name + "1.png"),
                       Image(pos, "images/ghosts/" + name + "2.png"))
        self.frame = False
        self.a = True

        self.boundingBox = BoundingBox(Point(pos.getX() - (39.5 / 2), pos.getY() - (39.5 / 2)), Point(39.5, 39.5))

        # Path finding variables
        self.ghostPathIndex = 0
        self.path = []
        self.lastTracked = 0
        self.scared = False
        self.lastScared = 0

    def drawGhost(self, win):
        self.image1.draw(win)
        time.sleep(0.1)
        self.image1.undraw()

    def scare(self):
        """Scares the ghost"""
        self.scared = True
        self.lastScared = time.time()

    def moveGhost(self, window, world, targetPos, multiplier = 1):
        for i in self.images:
            i.undraw()

        projected = [0, 0]

        if self.a == True:
            self.images[0].draw(window)
        elif self.a == False:
            self.images[1].draw(window)

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

        for i in self.images:
            i.move(X, Y)

        self.boundingBox.move(X, Y)

    def update(self, window, player, world, deltaTime):
        """Updates the ghost entirely, moves it and path finds accordingly"""
        if self.ghostPathIndex > len(self.path) - 1 or time.time() > self.lastTracked + 15 or self.scared:
            self.ghostPathIndex = 0

            plyGridX = int((player.boundingBox.pos.getX()) // world.nodeGrid.xScale) - 1
            plyGridY = int((player.boundingBox.pos.getY()) // world.nodeGrid.yScale) + 1
            ghostGridX = int((self.boundingBox.pos.getX()) // world.nodeGrid.xScale) - 1
            ghostGridY = int((self.boundingBox.pos.getY()) // world.nodeGrid.yScale) + 1

            if self.scared == True:
                # Make ghost run away
                # Gets neighbors of current node
                currentNode = world.nodeGrid.nodeList[ghostGridX][ghostGridY]
                neighbors = currentNode.getNeighbors(world.nodeGrid.nodeList)

                # Get random neighbor
                nextNode = neighbors[0]

                self.path = [random.choice(neighbors)]
                self.ghostPathIndex = 0

                # Reset the scared factor from a power pellet
                if time.time() > self.lastScared + 5:
                    self.scared = False
            else:
                try:
                    self.path = world.nodeGrid.pathFind(world.nodeGrid.nodeList[ghostGridX][ghostGridY], world.nodeGrid.nodeList[plyGridX][plyGridY], reversed = self.scared)
                except:
                    print("error")

            self.lastTracked = time.time()

        if self.ghostPathIndex < len(self.path) or self.lastTracked == 0:
            self.moveGhost(window, world, Point(self.path[self.ghostPathIndex].realPosX, self.path[self.ghostPathIndex].realPosY), 835 * deltaTime)

        if BoundingBox.pointWithin(self.boundingBox, BoundingBox(Point(self.path[self.ghostPathIndex].realPosX, self.path[self.ghostPathIndex].realPosY), Point(world.nodeGrid.xScale, world.nodeGrid.yScale))):
            self.ghostPathIndex += 1
