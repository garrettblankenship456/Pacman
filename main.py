# Main file for the whole game

# Imports
from graphics import * # 2D graphics library
from world import * # Get all the classes from the folder
import config # Imports the config options
from boundingbox import *

# Main function
def main():
    # Initialize window
    window = GraphWin("Pacman", config.WINDOW_WIDTH, config.WINDOW_HEIGHT, autoflush=False)

    # Initialize world
    world = World()
    world.render(window)

    # Initialize scene objects
    # Player
    player = Rectangle(Point(0, 0), Point(30, 30))
    player.setFill("blue")
    player.draw(window)
    player.move(config.WINDOW_WIDTH / 2 - 15, 675)
    playerBox = BoundingBox(Point(config.WINDOW_WIDTH / 2 - 15, 675), Point(30, 30))

    # Main loop
    while True:
        # Controls
        keys = window.checkKeys()
        # Exit loop if escape pressed
        if "Escape" in keys:
            break

        # Player controls
        if "w" in keys:
            player.move(0, -0.05)
            playerBox.move(0, -0.05)
        if "s" in keys:
            player.move(0, 0.05)
            playerBox.move(0, 0.05)
        if "a" in keys:
            player.move(-0.05, 0)
            playerBox.move(-0.05, 0)
        if "d" in keys:
            player.move(0.05, 0)
            playerBox.move(0.05, 0)

        # Game logic
        print(world.isCollided(playerBox))

        # Update window
        update()

    # Graceful exit
    window.close()


# Call main function
main()
