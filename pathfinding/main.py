# File to test path finding algorithm

# Imports
from graphics import *
from pathfinding.grid import *
from pathfinding.node import *

# Main function
def main():
    # Initialize window
    window = GraphWin("Path finding", 800, 800)
    window.setBackground("white")

    # Create grid
    grid = Grid(-10, 5, 40, 40, 20, 20, None, window)
    #grid.drawGrid(window)

    # Add nodes to the grid and draw them
    for i in range(0, 19):
        for x in range(0, 19):
            grid.setWall(x, i, False)

    for i in range(0, 18):
        grid.setWall(5, i, True)

    grid.drawNodes(window)

    # Test path find
    grid.pathFind(grid.nodeList[1][1], grid.nodeList[14][15], window)

    # Main loop
    while True:
        break

    # Wait for input
    window.getMouse()

main()
