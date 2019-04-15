# World class, holds data for the world walls and angles
from graphics import *
import config

class World:
    """World data and collision detection"""
    def __init__(self):
        # Initialize data array
        self.worldData = []
        self.worldPolys = []
        self.mirrored = False
        
        # generate world data
        self.__genWorldData("levels/default.txt")

    def __genWorldData(self, levelPath):
        # Creates all the world data from file
        file = open(levelPath)
        for line in file:
            # Get mirror status
            if line == "mirror_true\n":
                self.mirrored = True
                continue

            # Get position and size points
            positions = []
            points = line.split(" ")

            # Get XY from points
            pointData = points[0].split(",")
            xPos = int(pointData[0]) * config.MAP_RESOLUTION_X
            yPos = int(pointData[1]) * config.MAP_RESOLUTION_Y

            # Get size from points
            pointData = points[1].split(",")
            xSize = int(pointData[0]) * config.MAP_RESOLUTION_X
            ySize = int(pointData[1]) * config.MAP_RESOLUTION_Y

            # Create positions from pos and size
            positions.append(Point(xPos, yPos))
            positions.append(Point(xPos + xSize, yPos))
            positions.append(Point(xPos + xSize, yPos + ySize))
            positions.append(Point(xPos, yPos + ySize))

            # Put array in world data
            self.worldData.append(positions)

            # If mirrored append a backwards array of positions
            positions.append(Point(-xPos, yPos))
            positions.append(Point(-xPos - xSize, yPos))
            positions.append(Point(-xPos - xSize, yPos + ySize))
            positions.append(Point(-xPos, yPos + ySize))
            self.worldData.append(positions)

            # Loop through each line and make a polygon from it
            poly = Polygon(positions)
            poly.setFill("black")
            self.worldPolys.append(poly)

    def render(self, window):
        """Draws world to the GraphWin given"""
        for poly in self.worldPolys:
            poly.draw(window)
