from graphics import *
from world import *
from boundingbox import *

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

    def drawGhost(self, win):
        self.image1.draw(win)
        time.sleep(0.1)
        self.image1.undraw()

    def moveGhost(self, direction, window, world, targetPos, multiplier = 1):
        for i in self.images:
            i.undraw()

        projected = [0, 0]
        if direction.lower() == "n":
            projected[0] = 0
            projected[1] = -0.1
        elif direction.lower() == "e":
            projected[0] = 0.1
            projected[1] = 0

            self.a = False
        elif direction.lower() == "s":
            projected[0] = 0
            projected[1] = 0.1
        elif direction.lower() == "w":
            projected[0] = -0.1
            projected[1] = 0

            self.a = True

        if self.a == True:
            self.images[0].draw(window)
        elif self.a == False:
            self.images[1].draw(window)

        # Paths
        projected[0] = ((targetPos.getX() + 20) - (self.boundingBox.pos.getX() + self.boundingBox.size.getX() / 2)) * multiplier
        projected[1] = ((targetPos.getY() + 20) - (self.boundingBox.pos.getY() + self.boundingBox.size.getY() / 2)) * multiplier
        #print("X:", projected[0], " Y:", projected[1])

        # Normalization
        X = 0
        Y = 0
        if projected[0] > 0:
            X = 0.1 * multiplier
        elif projected[0] < 0:
            X = -0.1 * multiplier

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