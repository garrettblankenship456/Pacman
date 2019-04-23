import time
from graphics import *


class Pacman(object):
    """Pac-man character"""
    def __init__(self, firstImage, secondImage, x, y):
        self.image1 = firstImage
        self.image2 = secondImage
        self.x = x
        self.y = y

    def drawPacMan(self):
        self.image1.draw(win)
        time.sleep(0.1)
        self.image1.undraw()
        self.image2.draw(win)
        time.sleep(0.1)
        self.image2.undraw()

    def checkArrows(self):
        if win.checkKey().lower() == "up":
            while win.checkKey().lower() == "up":
                self.rotatePacman("up")
                self.movePacman("n", 10)

        elif win.checkKey().lower() == "right":
            while win.checkKey().lower() == "right":
                self.rotatePacman("right")
                self.movePacman("e", 10)

        elif win.checkKey().lower() == "down":
            while win.checkKey().lower() == "down":
                self.rotatePacman("down")
                self.movePacman("s", 10)

        elif win.checkKey().lower() == "left":
            while win.checkKey().lower() == "left":
                self.rotatePacman("left")
                self.movePacman("w", 10)


    def movePacman(self, direction, distance):
        if direction.lower() == "n":
            self.y -= 10
        elif direction.lower() == "e":
            self.x += 10
        elif direction.lower() == "s":
            self.y += 10
        elif direction.lower() == "w":
            self.x -= 10

    def rotatePacman(self, direction):
        print("in rotate")
        self.image1.undraw()
        self.image2.undraw()
        print(direction)
        if direction.lower() == "up":
            self.image1 = Image(Point(self.x, self.y), "images/directions/northFirst.png")
            self.image2 = Image(Point(self.x, self.y), "images/directions/center.png")
            self.drawPacMan()
        if direction.lower() == "down":
            self.image1 = Image(Point(self.x, self.y), "images/directions/southFirst.png")
            self.image2 = Image(Point(self.x, self.y), "images/directions/center.png")
            self.drawPacMan()
        if direction.lower() == "right":
            self.image1 = Image(Point(self.x, self.y), "images/directions/eastFirst.png")
            self.image2 = Image(Point(self.x, self.y), "images/directions/center.png")
            self.drawPacMan()
        if direction.lower() == "left":
            self.image1 = Image(Point(self.x, self.y), "images/directions/westFirst.png")
            self.image2 = Image(Point(self.x, self.y), "images/directions/center.png")
            self.drawPacMan()


win = GraphWin("Pac-man test", 600, 600)
win.setBackground("gray")

















#Wrote this, but not sure if I'll use it
a = """        if win.checkKey().lower() == "up":
            image01 = Image(Point(x, y), "images/directions/northFirst.png")
            image02 = Image(Point(x, y), "images/directions/northSecond.png")
            image1.undraw()
            image2.undraw()
            a = 0
            while a != 1:
                image01.draw(win)
                time.sleep(0.15)
                image01.undraw()
                image02.draw(win)
                image02.undraw()
                movePacman("N", 50, image01, image02)
        elif win.checkKey().lower() == "down":
            image01 = Image(Point(x, y), "images/directions/southFirst.png")
            image02 = Image(Point(x, y), "images/directions/southSecond.png")
            image1.undraw()
            image2.undraw()
            a = 0
            while a != 1:
                image01.draw(win)
                time.sleep(0.15)
                image01.undraw()
                image02.draw(win)
                image02.undraw()
                movePacman("S", 50, image01, image02)
        elif win.checkKey().lower() == "right":
            image01 = Image(Point(x, y), "images/directions/eastFirst.png")
            image02 = Image(Point(x, y), "images/directions/eastSecond.png")
            image1.undraw()
            image2.undraw()
            a = 0
            while a != 1:
                image01.draw(win)
                time.sleep(0.15)
                image01.undraw()
                image02.draw(win)
                image02.undraw()
                movePacman("E", 50, image01, image02)
        elif win.checkKey().lower() == "left":
            image01 = Image(Point(x, y), "images/directions/westFirst.png")
            image02 = Image(Point(x, y), "images/directions/westSecond.png")
            image1.undraw()
            image2.undraw()
            a = 0
            while a != 1:
                image01.draw(win)
                time.sleep(0.15)
                image01.undraw()
                image02.draw(win)
                image02.undraw()
                movePacman("W", 50, image01, image02)"""