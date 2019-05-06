# Grid class

# Imports
from graphics import *
from time import sleep
from pathfinding.node import *
import random
from boundingbox import *

# Class definition
class Grid:
    """Holds all the nodes of the map"""
    def __init__(self, xPos, yPos, xScale, yScale, xExtents, yExtents, walls = None, window = None):
        # Initialize variables
        self.xPos = xPos
        self.yPos = yPos
        self.xScale = xScale
        self.yScale = yScale
        self.xExtents = xExtents
        self.yExtents = yExtents
        self.nodeList = []

        # Populate node list
        for i in range(xExtents):
            # Create x array
            self.nodeList.append([])

            # For every y in the x array
            for k in range(yExtents):
                self.nodeList[i].append(Node(i, k, i * self.xScale, k * self.yScale, window))

        # If the walls arent none then set each node to a wall if its within the box
        if walls != None:
            for box in walls:
                for xNode in self.nodeList:
                    for node in xNode:
                        if BoundingBox.pointWithin(box, BoundingBox(Point(node.gridX * self.xScale, node.gridY * self.yScale), Point(self.xScale, self.yScale))) == True:
                            node.wall = True

    def addNode(self, node):
        """Adds node to the nodelist"""
        self.nodeList.append(node)

    def pathFind(self, startNode, endNode, window = None):
        """Path finds from one node to another"""
        # Create nodes around the startNode and select the one with the lowest value
        openNodes = [startNode]
        closedNodes = []
        path = []
        reached = False

        # Get the start of the nodes
        lowestNode = openNodes[0]
        lowestIndex = 0

        # Keep running until target is found
        while reached == False:
            # Get node with lowest F
            i = 0
            lowestF = 99999999999
            for node in openNodes:
                currF = node.getF(startNode, endNode)
                if currF <= lowestF and not node in closedNodes:
                    lowestF = currF
                    lowestIndex = i
                    lowestNode = node

                i += 1

            # Debug statements
            if window != None:
                r = Rectangle(Point(lowestNode.gridX * self.xScale, lowestNode.gridY * self.yScale), Point(lowestNode.gridX * self.xScale + self.xScale, lowestNode.gridY * self.yScale + self.yScale))
                r.setWidth(4)
                r.setOutline("blue")
                r.draw(window)

            # Switch the node from open to closed
            openNodes.pop(lowestIndex)
            closedNodes.append(lowestNode)
            path.append(lowestNode)

            # Check if destination reached
            neighbors = endNode.getNeighbors(self.nodeList)
            if lowestNode in neighbors:
                reached = True
                print(reached)
                path.reverse()
                return path
                break
            elif len(openNodes) <= 0:
                # No path
                return [startNode]
                break
            else:
                # Go through all its neighbors
                neighbors = lowestNode.getNeighbors(self.nodeList)
                for neighbor in neighbors:
                    # Ignore if closed
                    if neighbor in closedNodes or neighbor.wall == True:
                        continue

                    # Add and compute score if its not calculated yet
                    if neighbor in closedNodes and neighbor in openNodes:
                        print("this shouldnt happen")
                    else:
                        openNodes.append(neighbor)
                        openNodes[-1].calculateGH(startNode, endNode)

                    # Update it if its a quicker path (later only if needed)

            #sleep(0.5)

    def setWall(self, x, y, isWall = True, window = None):
        """Sets if the node is wall"""
        self.nodeList[x][y].wall = isWall

        # Create wall at position if a window was provided
        if window != None:
            r = Rectangle(Point(x * 20, y * 20), Point(x * 20 + 20, y * 20 + 20))
            r.setFill("red")
            r.draw(window)

    def drawNodes(self, window):
        """Debug function to draw all the nodes to the window"""
        for nodeLine in self.nodeList:
            for node in nodeLine:
                node.fValText.draw(window)
                r = Rectangle(Point(node.gridX * self.xScale, node.gridY * self.yScale), Point(node.gridX * self.xScale + self.xScale, node.gridY * self.yScale + self.yScale))
                r.setWidth(4)

                # Change color if its a wall or not
                if node.wall == True:
                    r.setOutline("yellow")
                else:
                    r.setOutline("green")

                r.draw(window)

    def drawGrid(self, window):
        """Debug function to draw all the grid lines"""
        # X line grid dividers
        xLines = []
        for i in range(self.xExtents):
            xLines.append(Line(Point(i * self.xScale + self.xPos, self.yPos), Point(i * self.xScale + self.xPos, self.yPos + self.yScale * self.xExtents)))

        # Y line grid dividers
        yLines = []
        for i in range(self.yExtents):
            yLines.append(Line(Point(self.xPos, i * self.yScale + self.yPos), Point(self.xPos + self.xScale * self.yExtents, i * self.yScale + self.yPos)))

        # Draw each line
        for l in xLines:
            l.draw(window)

        for l in yLines:
            l.draw(window)
