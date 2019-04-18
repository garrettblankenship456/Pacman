# Main file for the whole game

# Imports
from graphics import * # 2D graphics library
from world import * # Get all the classes from the folder
import config # Imports the config options
from boundingbox import *
from player import *

# Main function
def main():
    # Initialize window
    window = GraphWin("Pacman", config.WINDOW_WIDTH, config.WINDOW_HEIGHT, autoflush=False)

    # Initialize world
    world = World()
    world.render(window)

    # Initialize scene objects
    # Player
    player = Player()
    player.draw(window)

    # Main loop
    while True:
        # Controls
        keys = window.checkKeys()
        # Exit loop if escape pressed
        if "Escape" in keys:
            break

        # Player controls
        if "w" in keys:
            player.move('n')
        if "s" in keys:
            player.move('s')
        if "a" in keys:
            player.move('w')
        if "d" in keys:
            player.move('e')

        # Game logic
        if world.isCollided(player.boundingBox):
            player.box.setFill("red")
        else:
            player.box.setFill("blue")

        # Update window and player
        player.update(world)
        update()

    # Graceful exit
    window.close()


# Call main function
main()
