# World creator
from graphics import *
import config
import time

# Main function
def main():
    # Initialize window
    window = GraphWin("Pacman world editor", config.WINDOW_WIDTH, config.WINDOW_HEIGHT, autoflush=False)

    # Draw trace image
    trace = Image(Point(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2), "photo11.png")
    trace.draw(window)

    clickPoint = Rectangle(Point(0, 0), Point(10, 10))
    clickPoint.setFill("white")
    clickPoint.draw(window)
    cursor = Rectangle(Point(0, 0), Point(0, 0))
    cursor.setFill("white")
    cursor.draw(window)

    # Click positions
    pos1 = False
    pos2 = False

    # Rectangles
    shapes = []

    # Main loop
    while True:
        keys = window.checkKeys()
        if "Escape" in keys:
            break
        if "z" in keys:
            shapes[len(shapes) - 1].undraw()
            del shapes[len(shapes) - 1]
            time.sleep(1)

        # Get click postitons
        pos = window.checkMouse()
        clickPoint.undraw()
        clickPoint = Rectangle(Point(window.getCurrentMouseLocation().getX() // config.MAP_RESOLUTION_X * config.MAP_RESOLUTION_X, window.getCurrentMouseLocation().getY() // config.MAP_RESOLUTION_Y * config.MAP_RESOLUTION_Y), Point(((window.getCurrentMouseLocation().getX() + config.MAP_RESOLUTION_X) // config.MAP_RESOLUTION_X * config.MAP_RESOLUTION_X), ((window.getCurrentMouseLocation().getY() + config.MAP_RESOLUTION_Y) // config.MAP_RESOLUTION_Y) * config.MAP_RESOLUTION_Y))
        clickPoint.setFill("white")
        clickPoint.draw(window)
        if pos != None:
            if pos1 == False:
                pos1 = Point(pos.getX() // config.MAP_RESOLUTION_X, pos.getY() // config.MAP_RESOLUTION_Y)
            elif pos2 == False:
                pos2 = Point(pos.getX() // config.MAP_RESOLUTION_X, pos.getY() // config.MAP_RESOLUTION_Y)

                shapes.append(Rectangle(Point(pos1.getX() * config.MAP_RESOLUTION_X, pos1.getY() * config.MAP_RESOLUTION_Y), Point(pos2.getX() * config.MAP_RESOLUTION_X, pos2.getY() * config.MAP_RESOLUTION_Y)))
                shapes[len(shapes) - 1].setFill("white")
                shapes[len(shapes) - 1].draw(window)

                pos1 = False
                pos2 = False
        else:
            if pos1 != False:
                # Undraw and redraw cursor
                cursor.undraw()
                cursor = Rectangle(Point(pos1.getX() * config.MAP_RESOLUTION_X, pos1.getY() * config.MAP_RESOLUTION_Y), Point((window.getCurrentMouseLocation().getX() // config.MAP_RESOLUTION_X * config.MAP_RESOLUTION_X), (window.getCurrentMouseLocation().getY() // config.MAP_RESOLUTION_Y) * config.MAP_RESOLUTION_Y))
                cursor.setFill("white")
                cursor.draw(window)

        window.update()

    # Save data
    path = input("Name of world: ")
    file = open(path, "w")
    for s in shapes:
        data = ""
        data += str(s.getP1().getX() // config.MAP_RESOLUTION_X)
        data += ","
        data += str(s.getP1().getY() // config.MAP_RESOLUTION_Y)
        data += " "
        data += str((s.getP2().getX() - s.getP1().getX()) // config.MAP_RESOLUTION_X)
        data += ","
        data += str((s.getP2().getY() - s.getP1().getY()) // config.MAP_RESOLUTION_Y)
        data += "\n"
        file.write(data)
    
main()