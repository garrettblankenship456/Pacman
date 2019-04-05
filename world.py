# World class, holds data for the world walls and angles
from graphics import *

class World:
    """World data and collision detection"""
    def __init__(self):
        # Initialize data array
        self.worldData = []
        self.worldPolys = []
        
        # generate world data
        self.__genWorldData("levels/default.txt")

    def __genWorldData(self, levelPath):
        # Creates all the world data from file
        file = open(levelPath)
        for line in file:
            # Get 4 points
            positions = []
            points = line.split(" ")

            # Get XY from points
            for point in points:
                pointData = point.split(",")
                x = int(pointData[0])
                y = int(pointData[1])
                positions.append(Point(x, y))

            # Put array in world data
            self.worldData.append(positions)
            
            # Loop through each line and make a polygon from it
            poly = Polygon(positions)
            self.worldPolys.append(poly)

    def render(self, window):
        """Draws world to the GraphWin given"""
        for poly in self.worldPolys:
            poly.draw(window)
