# World class, holds data for the world walls and angles
from graphics import *
import config
from boundingbox import *
import math
from point import *
from pathfinding.grid import *
from pathfinding.node import *

class World:
    """World data and collision detection"""
    def __init__(self, window = None):
        # Initialize data array
        self.worldData = []
        self.worldPolys = []
        self.hitboxes = []
        self.navWalls = []
        self.teleporters = [[BoundingBox(Point(-30, 340), Point(40, 40)), Point(590, 325)], [BoundingBox(Point(630, 340), Point(40, 40)), Point(10, 325)]]
        self.squares = []
        self.mirrored = False
        self.lineOfSymmetry = 0

        # Decorator
        self.background = Image(Point(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2 - 18), "images/background.png")

        # generate world data and nav mesh
        self.__genWorldData("levels/newworld.txt")

        # Generate grid
        self.nodeGrid = Grid(10, -5, 10, 10, 72, 72, None, window)
        self.__genNavMesh("levels/navmesh.txt")

    def __genPointMap(self, pointPath):
        """Reads the positions of all the points"""
        file = open(pointPath)
        for line in file:
            # Get position and size points
            points = line.split(" ")

            # Get XY from points
            pointData = points[0].split(",")
            xPos = (float(pointData[0]) + 2) * 9 - 6
            yPos = (float(pointData[1]) + config.MAP_OFFSET_Y) * 9 - 6

            # Get type
            type = ""

            if len(points) < 2:
                type = False
            else:
                type = True

            # Create hitbox
            self.squares.append(Square(Point(xPos, yPos), type))

    def __genWorldData(self, levelPath):
        # Creates all the world data from file
        file = open(levelPath)
        for line in file:
            # Get mirror status
            if line == "mirror_true\n":
                self.mirrored = True
            elif line.split(" ")[0] == "center_line":
                self.lineOfSymmetry = float(line.split(" ")[1]) * config.MAP_RESOLUTION_X
            else:
                # Get position and size points
                positions = []
                positions2 = []
                points = line.split(" ")

                # Get XY from points
                pointData = points[0].split(",")
                xPos = (float(pointData[0]) + config.MAP_OFFSET_X) * config.MAP_RESOLUTION_X
                yPos = (float(pointData[1]) + config.MAP_OFFSET_Y) * config.MAP_RESOLUTION_Y

                # Get size from points
                pointData = points[1].split(",")
                xSize = float(pointData[0]) * config.MAP_RESOLUTION_X
                ySize = float(pointData[1]) * config.MAP_RESOLUTION_Y

                # Create positions from pos and size
                positions.append(Point(xPos, yPos))
                positions.append(Point(xPos + xSize, yPos))
                positions.append(Point(xPos + xSize, yPos + ySize))
                positions.append(Point(xPos, yPos + ySize))

                # Create hitbox
                self.hitboxes.append(BoundingBox(Point(xPos, yPos), Point(xSize, ySize)))

                # Put array in world data
                self.worldData.append(positions)

                # If mirrored append a backwards array of positions
                if self.mirrored == True:
                    positions2.append(Point(self.lineOfSymmetry * 2 - xPos, yPos))
                    positions2.append(Point(self.lineOfSymmetry * 2 - xPos - xSize, yPos))
                    positions2.append(Point(self.lineOfSymmetry * 2 - xPos - xSize, yPos + ySize))
                    positions2.append(Point(self.lineOfSymmetry * 2 - xPos, yPos + ySize))
                    self.worldData.append(positions2)
                    poly2 = Polygon(positions2)
                    #poly2.setFill("black")
                    self.worldPolys.append(poly2)

                    # Create hitbox
                    self.hitboxes.append(BoundingBox(Point(self.lineOfSymmetry * 2 - xPos - xSize, yPos), Point(xSize, ySize)))

                # Loop through each line and make a polygon from it
                poly = Polygon(positions)
                #poly.setFill("black")
                self.worldPolys.append(poly)

        # Create points
        self.__genPointMap("levels/points.txt")

    def __genNavMesh(self, levelPath):
        # Creates all the world data from file
        file = open(levelPath)
        for line in file:
            # Get XY from points
            pointData = line.split(",")
            xPos = int(pointData[0])
            yPos = int(pointData[1])

            # Set walls
            self.nodeGrid.nodeList[xPos][yPos].wall = False

    def render(self, window):
        """Draws world to the GraphWin given"""
        # Draw background image
        self.background.draw(window)

        # Draw nav nodes
        #self.nodeGrid.drawGrid(window)
        #self.nodeGrid.drawNodes(window)

        #for poly in self.worldPolys:
            #poly.draw(window)
        #for b in self.hitboxes:
            #b.debugDraw(window)
        #for s in self.squares:
            #s.draw(window)

    def isCollided(self, box):
        """Checks if a point is in any rectangles"""
        collision = False
        hb = None
        for hitbox in self.hitboxes:
            if BoundingBox.pointWithin(hitbox, box) == True:
                collision = True
                hb = hitbox
                break

        return collision, hb

    def getClosest(self, position):
        """Gets the closest hitbox to the position"""
        closest = None
        lastDist = 9999
        for hitbox in self.hitboxes:
            dist = math.hypot(hitbox.getCenter().getX() - position.getX(), hitbox.getCenter().getY() - position.getY())
            if dist < lastDist:
                closest = hitbox
                lastDist = dist

        return closest, dist

    def onTeleporter(self, box):
        """Checks if the box touches a teleporter"""
        for i in range(len(self.teleporters)):
            if BoundingBox.pointWithin(box, self.teleporters[i][0]):
                return self.teleporters[i][1]

        # If not on any teleporters return false
        return False
