# Grid class

# Imports
from graphics import *
from time import sleep
from node import *

# Class definition
class Grid:
    """Holds all the nodes of the map"""
    def __init__(self, xPos, yPos, xScale, yScale):
        # Initialize variables
        self.xPos = xPos
        self.yPos = yPos
        self.xScale = xScale
        self.yScale = yScale
        self.nodeList = []

    def addNode(self, node):
        """Adds node to the nodelist"""
        self.nodeList.append(node)

    def pathFind(self, startNode, endNode, window = None):
        """Path finds from one node to another"""
        # Create nodes around the startNode and select the one with the lowest value
        openNodes = [startNode]
        closedNodes = []
        reached = False

        # Keep running until target is found
        while reached == False:
            # Get node with lowest F
            lowestNode = openNodes[0]
            lowestF = lowestNode.getF(startNode, endNode)
            for node in openNodes:
                currF = node.getF(startNode, endNode)
                if currF < lowestF:
                    lowestF = currF
                    lowestNode = node

            r = Rectangle(Point(lowestNode.gridX * self.xScale, lowestNode.gridY * self.yScale), Point(lowestNode.gridX * self.xScale + self.xScale, lowestNode.gridY * self.yScale + self.yScale))
            r.setOutline("blue")
            r.draw(window)

            # Check if destination reached
            if lowestNode == endNode:
                print("Destination reached")
                break
            else:
                closedNodes.append(lowestNode)

                # Go through all its neighbors
                neighbors = lowestNode.generateNodeMatrix()
                lowestG = lowestNode.g
                for neighbor in neighbors:
                    neighbor.calculateGH(startNode, endNode)

                    r = Rectangle(Point(neighbor.gridX * self.xScale, neighbor.gridY * self.yScale),
                                  Point(neighbor.gridX * self.xScale + self.xScale,
                                        neighbor.gridY * self.yScale + self.yScale))
                    r.setOutline("green")
                    r.draw(window)
                    neighbor.getF(startNode, endNode, window)

                    if neighbor.g < lowestG and neighbor in closedNodes:
                        lowestG = neighbor.g
                        neighbor.parent = lowestNode
                        continue
                    elif lowestG < neighbor.g and neighbor in openNodes:
                        neighbor.parent = lowestNode
                        continue
                    elif not neighbor in openNodes and not neighbor in closedNodes:
                        openNodes.append(neighbor)

    def drawNodes(self, window):
        """Debug function to draw all the nodes to the window"""
        for node in self.nodeList:
            r = Rectangle(Point(node.gridX * self.xScale, node.gridY * self.yScale), Point(node.gridX * self.xScale + self.xScale, node.gridY * self.yScale + self.yScale))
            r.setFill("red")
            r.draw(window)

    def drawGrid(self, max, window):
        """Debug function to draw all the grid lines"""
        # X line grid dividers
        xLines = []
        for i in range(max):
            xLines.append(Line(Point(i * self.xScale + self.xPos, self.yPos), Point(i * self.xScale + self.xPos, self.yPos + self.yScale * max)))

        # Y line grid dividers
        yLines = []
        for i in range(max):
            yLines.append(Line(Point(self.xPos, i * self.yScale + self.yPos), Point(self.xPos + self.xScale * max, i * self.yScale + self.yPos)))

        # Draw each line
        for l in xLines:
            l.draw(window)

        for l in yLines:
            l.draw(window)
