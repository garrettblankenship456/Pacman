# Node class

# Imports
from graphics import *

# Class definition
class Node:
    """Creates a node for finding paths"""
    def __init__(self, gridX, gridY, realPosX, realPosY):
        # Initialize variables
        self.gridX = gridX
        self.gridY = gridY
        self.realPosX = realPosX
        self.realPosY = realPosY
        self.parent = None # The last node used

        # Calculate F, H, and G variables
        self.g = 0
        self.h = 0
        self.f = 0

        # Stuff to hold values
        self.fValText = Text(Point(self.gridX * 40 + 20, self.gridY * 40 + 20), "NULL")

    def calculateGH(self, startNode, targetNode, window = None):
        """Calculates G value and H value to the targetNode and back"""
        dist2Self = abs(self.gridX - startNode.gridX) + abs(self.gridY - startNode.gridY)
        dist2Target = abs(self.gridX - targetNode.gridX) + abs(self.gridY - targetNode.gridY)
        self.g = dist2Self
        self.h = dist2Target
        self.fValText.setText(str(round(self.getF())))

        # Draw if window was supplied
        if window != None:
            self.fValText.draw(window)

    def getF(self, startNode = None, endNode = None, window = None):
        """Returns F value"""
        if startNode != None and endNode != None: self.calculateGH(startNode, endNode, window)

        return self.g + self.h

    def generateNodeMatrix(self):
        """Creates 8 node arounds the current node"""
        nodeList = []
        for i in range(3):
            for k in range(3):
                # Omit the middle cube
                if i == 1 and k == 1: continue
                n = Node(self.gridX - 1 + i, self.gridY - 1 + k, self.realPosX, self.realPosY)
                nodeList.append(n)

        # Return list
        return nodeList

    def __str__(self):
        data = "X: "
        data += str(self.gridX)
        data += ", Y: "
        data += str(self.gridY)
        data += ", G: "
        data += str(self.g)
        data += ", H: "
        data += str(self.h)
        data += "\n"
        return data