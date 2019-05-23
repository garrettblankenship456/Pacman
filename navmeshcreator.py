# Nav creator
from graphics import *
import config
import time
from world import *

# Main function
def main():
    # Initialize window
    window = GraphWin("Pacman navmesh editor", config.WINDOW_WIDTH, config.WINDOW_HEIGHT, autoflush=False)
    window.setBackground("green")

    # Draw trace image
    #trace = Image(Point(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2), "images/trace.png")
    #trace.draw(window)

    clickPoint = Rectangle(Point(0, 0), Point(8, 8))
    clickPoint.setFill("white")
    clickPoint.draw(window)

    # Positions
    positions = []
    boxes = []
    i = 0

    # World loading
    w = World()
    w.render(window)

    config.MAP_OFFSET_Y = config.MAP_OFFSET_Y + w.nodeGrid.yPos
    config.MAP_OFFSET_X = config.MAP_OFFSET_X + w.nodeGrid.xPos
    w.nodeGrid.xScale = 9
    w.nodeGrid.xScale = 9

    # Main loop
    while True:
        keys = window.checkKeys()
        if "Escape" in keys:
            break
        if "z" in keys:
            positions.pop(i - 1)
            boxes[i - 1].undraw()
            boxes.pop(i - 1)
            i -= 1
            sleep(0.1)

        # Get click postitons
        pos = window.checkMouse()
        clickPoint.undraw()
        clickPoint = Rectangle(Point(window.getCurrentMouseLocation().getX() // w.nodeGrid.xScale * w.nodeGrid.xScale + config.MAP_OFFSET_X, window.getCurrentMouseLocation().getY() // w.nodeGrid.xScale * w.nodeGrid.xScale + config.MAP_OFFSET_Y), Point(((window.getCurrentMouseLocation().getX() + w.nodeGrid.xScale) // w.nodeGrid.xScale * w.nodeGrid.xScale + config.MAP_OFFSET_X), ((window.getCurrentMouseLocation().getY() + w.nodeGrid.xScale) // w.nodeGrid.xScale) * w.nodeGrid.xScale + config.MAP_OFFSET_Y))
        clickPoint.setFill("white")
        clickPoint.draw(window)
        if pos != None:
            positions.append(pos)

            r = Rectangle(Point(pos.getX() // w.nodeGrid.xScale * w.nodeGrid.xScale + config.MAP_OFFSET_X, pos.getY() // w.nodeGrid.xScale * w.nodeGrid.xScale + config.MAP_OFFSET_Y), Point(pos.getX() // w.nodeGrid.xScale * w.nodeGrid.xScale + w.nodeGrid.xScale + config.MAP_OFFSET_X, pos.getY() // w.nodeGrid.xScale * w.nodeGrid.xScale + w.nodeGrid.xScale + config.MAP_OFFSET_Y))
            r.setFill("orange")
            r.draw(window)
            boxes.append(r)
            i += 1

            sleep(0.1)

        window.update()

    # Save data
    path = input("Name of world: ")
    file = open(path, "w")
    for p in positions:
        data = ""
        data += str(int(p.getX() // w.nodeGrid.xScale))
        data += ","
        data += str(int(p.getY() // w.nodeGrid.xScale))
        data += "\n"
        file.write(data)

main()
