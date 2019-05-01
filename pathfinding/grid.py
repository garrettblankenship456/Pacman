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
        pathList = []
        evaluated = []
        nextNode = Node(startNode.gridX, startNode.gridY, 0, 0)

        # Keep running until target is found
        while True:
            nodesAround = nextNode.generateNodeMatrix()
            fValues = []
            for node in nodesAround:
                node.calculateGH(startNode, endNode)
                fValues.append(node.getF())

            # Continue to the next one
            lowestVal = fValues[0]
            nextNode = nodesAround[0]
            for i in range(1, len(fValues)):
                if fValues[i] < lowestVal:
                    if not nodesAround[i] in evaluated:
                        nextNode = nodesAround[i]
                        lowestVal = fValues[i]
                        evaluated.append(nextNode)

            # Create rectangle for the lowest value
            if window != None:
                for n in nodesAround:
                    r = Rectangle(Point(n.gridX * self.xScale, n.gridY * self.yScale), Point(n.gridX * self.xScale + self.xScale, n.gridY * self.yScale + self.yScale))
                    if nextNode == n:
                        r.setFill("green")
                    else:
                        r.setFill("blue")
                    if n in evaluated:
                        r.setFill("yellow")
                    r.draw(window)

            # End loop once target has been found
            print(lowestVal)
            if lowestVal == 0:
                print("Target found!")
                break

            sleep(1)

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
