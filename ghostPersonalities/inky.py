# Seperate personality for the ghost inky
# Inky moves randomly until blinky is nearby
from ghost import *
import math

# Sub class
class Inky(Ghost):
    def __init__(self, name, pos, blinky, window):
        # Run the constructor
        super().__init__(name, pos, window)
        self.parentGhost = blinky

    # Override the update for the personality
    def update(self, player, world, deltaTime):
        """Updates the ghost entirely, moves it and path finds accordingly"""
        # Get distance to blinky
        distance = math.hypot(self.parentGhost.boundingBox.pos.getX() - self.boundingBox.pos.getX(),
                              self.parentGhost.boundingBox.pos.getY() - self.boundingBox.pos.getY())

        if self.ghostPathIndex > len(self.path) - 1 or time.time() > self.lastTracked + 5 or self.firstTickScared == True:
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

            if self.scared == True or distance > 185:
                # Make ghost to a random point
                randNode = world.nodeGrid.randomNode()
                self.path = world.nodeGrid.pathFind(world.nodeGrid.nodeList[ghostGridX][ghostGridY], randNode)
            else:
                try:
                    self.path = world.nodeGrid.pathFind(world.nodeGrid.nodeList[ghostGridX][ghostGridY], world.nodeGrid.nodeList[plyGridX][plyGridY])
                except:
                    print("error")

            self.lastTracked = time.time()

        if self.ghostPathIndex < len(self.path) or self.lastTracked == 0:
            notAlive = not self.alive
            self.moveGhost(world, Point(self.path[self.ghostPathIndex].realPosX, self.path[self.ghostPathIndex].realPosY), (835 - (240 * self.scared) + (440 * notAlive)) * deltaTime)

        if BoundingBox.pointWithin(self.boundingBox, BoundingBox(Point(self.path[self.ghostPathIndex].realPosX, self.path[self.ghostPathIndex].realPosY), Point(world.nodeGrid.xScale, world.nodeGrid.yScale))):
            self.ghostPathIndex += 1