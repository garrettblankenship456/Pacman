# Node class

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

    def calculateGH(self, startNode, targetNode):
        """Calculates G value and H value to the targetNode and back"""
        dist2Self = ((startNode.gridX - self.gridX) ** 2 + (startNode.gridY - self.gridY) ** 2) ** (1/2)
        dist2Target = ((targetNode.gridX - self.gridX) ** 2 + (targetNode.gridY - self.gridY) ** 2) ** (1/2)
        self.g = dist2Self
        self.h = dist2Target
        print("G:", self.g)
        print("H:", self.h)

    def getF(self):
        """Returns F value"""
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
