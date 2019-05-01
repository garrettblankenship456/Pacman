# File to test path finding algorithm

# Imports
from graphics import *
from grid import *
from node import *

# Main function
def main():
    # Initialize window
    window = GraphWin("Path finding", 800, 800)
    window.setBackground("white")

    # Create grid
    grid = Grid(0, 0, 40, 40)
    grid.drawGrid(15, window)

    # Create node and draw to screen
    node1 = Node(2, 3, 0, 0)
    node2 = Node(15, 7, 0, 0)
    node3 = Node(1, 1, 0, 0)

    # Add nodes to the grid and draw them
    grid.addNode(node1)
    grid.addNode(node2)
    grid.addNode(node3)
    grid.drawNodes(window)

    # Test path find
    grid.pathFind(node1, node2, window)

    # Main loop
    while True:
        break

    # Wait for input
    window.getMouse()

main()
