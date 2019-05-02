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
    grid = Grid(0, 0, 40, 40, 15, 15)
    grid.drawGrid(15, window)

    # Add nodes to the grid and draw them
    grid.setWall(1, 3, True)
    grid.drawNodes(window)

    # Test path find
    grid.pathFind(grid.nodeList[0][2], grid.nodeList[5][10], window)

    # Main loop
    while True:
        break

    # Wait for input
    window.getMouse()

main()
