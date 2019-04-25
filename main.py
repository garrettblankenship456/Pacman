# Main file for the whole game

# Imports
from graphics import * # 2D graphics library
from world import * # Get all the classes from the folder
import config # Imports the config options
from boundingbox import *
from player import *
import time
import _thread

# Control loop
def controlLoop(window, player):
    while True:
        # Controls
        keys = window.checkKeys()
        # Exit loop if escape pressed
        if "Escape" in keys:
            window.close()
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

# Physics loop
def physLoop(window, world, player):
    while True:
        # Update window and player
        player.update(window, world, 1)
        window.update()

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

    # Deltatime
    lastTime = time.time()
    deltaTime = 0

    # Start control loop
    _thread.start_new_thread(controlLoop, (window, player))
    _thread.start_new_thread(physLoop, (window, world, player))

    # Main loop
    while True:
        # Update deltatime
        currTime = time.time()
        deltaTime = currTime - lastTime
        lastTime = currTime

        # Game logic
        if world.isCollided(player.boundingBox):
            player.box.setFill("red")
        else:
            player.box.setFill("blue")

    # Graceful exit
    window.close()


# Call main function
main()
