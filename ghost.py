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

    def moveGhost(self, direction, window, world, targetPos):
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
        projected[0] = (targetPos.getX() - self.boundingBox.pos.getX())
        projected[1] = (targetPos.getY() - self.boundingBox.pos.getY())

        # Normalization
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

        print(X, Y)

        # Collision detection
        collided, box = world.isCollided(self.boundingBox)
        #if collided:
        #    projected[0] = X
        #    projected[1] = Y

        for i in self.images:
            i.move(X, Y)

        self.boundingBox.move(X, Y)