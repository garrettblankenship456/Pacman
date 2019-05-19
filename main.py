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
    window.setBackground("black")

    # Initialize world
    world = World(window)
    world.render(window)

    # Initialize game state
    gameState = 1 # 0 = Main menu, 1 = Gameplay, 2 = End game

    # Initialize scene objects
    # Player
    player = Player(window, world)
    dead = False

    # Deltatime
    lastTime = time.time()
    deltaTime = 0

    # Create ghosts
    blinky = Ghost("blinky", Point(config.WINDOW_WIDTH / 2, 283), window)
    clyde = Ghost("clyde", Point(config.WINDOW_WIDTH / 2 - 35, config.WINDOW_HEIGHT / 2 - 27), window)
    inky = Ghost("inky", Point(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2 - 27), window)
    pinky = Ghost("pinky", Point(config.WINDOW_WIDTH / 2 + 35, config.WINDOW_HEIGHT / 2 - 27), window)
    ghosts = (blinky, clyde, inky, pinky)
    startTime = time.time() # Time the ghost started, slow release

    # Initialize menu frames and items
    score = Text(Point(config.WINDOW_WIDTH / 2, 25), "00")
    score.setTextColor("white")
    score.draw(window)
    #startMenu = Image(Point(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2), "images/menu.png")
    #endScreen = Image(Point(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2), "images/end.png")

    # Main loop
    while True:
        # Run the function based on the game state
        if gameState == 0:
            # Check for key input
            window.getKey()
            gameState = 1
        elif gameState == 1:
            # Update score value
            score.setText(int(player.score))

            # Controls
            keys = window.checkKeys()
            # Exit loop if escape pressed
            if "Escape" in keys:
                window.close()
                gameState = 2
                continue

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
                    blinky.respawn(world)
                    clyde.respawn(world)
                    inky.respawn(world)
                    pinky.respawn(world)
            else:
                sleep(1)
                gameState = 2
                continue

            # Update deltatime
            currTime = time.time()
            deltaTime = currTime - lastTime
            lastTime = currTime
            #print(deltaTime)

            # Enemy path finding
            if time.time() > startTime + 0:
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
        elif gameState == 2:
            window.getKey()
            break

    # Graceful exit
    window.close()


# Call main function
main()
