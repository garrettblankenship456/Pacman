# Main file for the whole game

# Imports
from graphics import * # 2D graphics library
from world import * # Get all the classes from the folder
import config # Imports the config options
from boundingbox import *
from player import *
from ghost import *
import time

# Main function
def main():
    # Initialize window
    window = GraphWin("Pacman", config.WINDOW_WIDTH, config.WINDOW_HEIGHT, autoflush=False)
    window.setBackground("white")

    # Initialize world
    world = World(window)
    world.render(window)

    # Initialize scene objects
    # Player
    player = Player(window)
    dead = False

    # Deltatime
    lastTime = time.time()
    deltaTime = 0

    # Create ghosts
    blinky = Ghost("blinky", Point(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2 - 27))
    clyde = Ghost("clyde", Point(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2 - 27))
    inky = Ghost("inky", Point(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2 - 27))
    pinky = Ghost("pinky", Point(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2 - 27))
    ghosts = (blinky, clyde, inky, pinky)
    startTime = time.time() # Time the ghost started, slow release

    # Main loop
    while True:
        # Controls
        keys = window.checkKeys()
        # Exit loop if escape pressed
        if "Escape" in keys:
            window.close()
            break

        # Player controls
        if dead == False:
            if "w" in keys:
                player.move('n')
            if "s" in keys:
                player.move('s')
            if "a" in keys:
                player.move('w')
            if "d" in keys:
                player.move('e')
            if "x" in keys:
                blinky.scare()
                clyde.scare()
                inky.scare()
                pinky.scare()
        else:
            sleep(1)
            break

        # Update deltatime
        currTime = time.time()
        deltaTime = currTime - lastTime
        lastTime = currTime
        #print(deltaTime)

        # Enemy path finding
        if time.time() > startTime + 5:
            blinky.update(window, player, world, deltaTime)

        if time.time() > startTime + 10:
            clyde.update(window, player, world, deltaTime)

        if time.time() > startTime + 15:
            inky.update(window, player, world, deltaTime)

        if time.time() > startTime + 20:
            pinky.update(window, player, world, deltaTime)

        # Update window and player
        dead = player.update(window, world, deltaTime, ghosts)
        window.update()

    # Graceful exit
    window.close()


# Call main function
main()
