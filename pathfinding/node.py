# Node class

# Imports
from graphics import *

# Class definition
class Node:
    """Creates a node for finding paths"""
    def __init__(self, gridX, gridY, realPosX, realPosY, wall = False, window = None):
        # Initialize variables
        self.gridX = gridX
        self.gridY = gridY
        self.realPosX = realPosX
        self.realPosY = realPosY
        self.parent = None # The last node used
        self.wall = wall

        # Calculate F, H, and G variables
        self.g = 0
        self.h = 0
        self.f = 0

        # Stuff to hold values
        self.fValText = Text(Point(self.gridX * 20 + 10, self.gridY * 20 + 10), "0")
        if window != None:
            self.fValText.draw(window)

    def calculateGH(self, startNode, targetNode, window = None):
        """Calculates G value and H value to the targetNode and back"""
        dist2Self = abs(self.gridX - startNode.gridX) + abs(self.gridY - startNode.gridY)
        dist2Target = abs(targetNode.gridX - self.gridX) ** 2 + abs(targetNode.gridY - self.gridY) ** 2
        self.g = dist2Self
        self.h = dist2Target

        # Draw if window was supplied
        self.fValText.setText(str(round(self.getF())))

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

    def getNeighbors(self, nodeList):
        """Gets the neighbors of the nodes"""
        neighbors = []
        neighbors.append(nodeList[self.gridX - 1][self.gridY - 1])
        neighbors.append(nodeList[self.gridX][self.gridY - 1])
        neighbors.append(nodeList[self.gridX + 1][self.gridY - 1])

        neighbors.append(nodeList[self.gridX - 1][self.gridY])
        neighbors.append(nodeList[self.gridX + 1][self.gridY])

        neighbors.append(nodeList[self.gridX - 1][self.gridY + 1])
        neighbors.append(nodeList[self.gridX][self.gridY + 1])
        neighbors.append(nodeList[self.gridX + 1][self.gridY + 1])

        # Remove walls
        for neighbor in neighbors:
            if neighbor.wall == True:
                neighbors.remove(neighbor)

        return neighbors

    def isWall(self, nodeList):
        """Sets the node to be a wall if it matches any walls in the list"""
        for node in nodeList:
            if node.gridX == self.gridX and node.gridY == self.gridY:
                self.wall = True
                break

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
