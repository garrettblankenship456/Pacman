# Nav creator
from graphics import *
import config
import time
from world import *

# Main function
def main():
    # Initialize window
    window = GraphWin("Pacman navmesh editor", config.WINDOW_WIDTH, config.WINDOW_HEIGHT, autoflush=False)

    # Draw trace image
    #trace = Image(Point(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2), "images/photo11.png")
    #trace.draw(window)

    clickPoint = Rectangle(Point(0, 0), Point(20, 20))
    clickPoint.setFill("white")
    clickPoint.draw(window)

    # Positions
    positions = []
    boxes = []
    i = 0

    # World loading
    w = World()
    w.render(window)

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
        clickPoint = Rectangle(Point(window.getCurrentMouseLocation().getX() // 20 * 20, window.getCurrentMouseLocation().getY() // 20 * 20), Point(((window.getCurrentMouseLocation().getX() + 20) // 20 * 20), ((window.getCurrentMouseLocation().getY() + 20) // 20) * 20))
        clickPoint.setFill("white")
        clickPoint.draw(window)
        if pos != None:
            positions.append(pos)

            r = Rectangle(Point(pos.getX() // 20 * 20, pos.getY() // 20 * 20), Point(pos.getX() // 20 * 20 + 20, pos.getY() // 20 * 20 + 20))
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
        data += str(int(p.getX() // 20))
        data += ","
        data += str(int(p.getY() // 20))
        data += "\n"
        file.write(data)

main()
