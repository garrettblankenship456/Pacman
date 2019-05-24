# Main file for the whole game

# Imports
from graphics import * # 2D graphics library
from world import * # Get all the classes from the folder
import config # Imports the config options
from boundingbox import *
from player import *
from ghost import *
import time
import threading

# Main function
def main():
    # Initialize window
    window = GraphWin("Pacman", config.WINDOW_WIDTH, config.WINDOW_HEIGHT, autoflush=False)
    window.setBackground("black")

    # Initialize world
    world = World(window)
    world.render(window)

    # Initialize game state
    global gameState
    gameState = 0 # 0 = Main menu, 1 = Gameplay, 2 = End game

    # Initialize scene objects
    # Player
    def win():
        # Controls win condition
        global gameState
        sleep(1)
        gameState = 2
        physThread.join()

    player = Player(window, world, win)
    dead = False

    # Create ghosts
    blinky = Ghost("blinky", Point(config.WINDOW_WIDTH / 2, 283), window)
    clyde = Ghost("clyde", Point(config.WINDOW_WIDTH / 2 - 5, config.WINDOW_HEIGHT / 2 - 27), window)
    inky = Ghost("inky", Point(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2 - 27), window)
    pinky = Ghost("pinky", Point(config.WINDOW_WIDTH / 2 + 5, config.WINDOW_HEIGHT / 2 - 27), window)
    ghosts = (blinky, clyde, inky, pinky)
    startTime = time.time() # Time the ghost started, slow release

    # Initialize menu frames and items
    score = Text(Point(config.WINDOW_WIDTH / 2, 25), "00")
    score.setTextColor("white")
    score.draw(window)
    startMenu = Image(Point(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2), "images/menu.jpg")
    endScreen = Image(Point(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2), "images/end.png")

    # Physics loop
    def physLoop(player, world, ghosts):
        """Updates the physics for everything, its a function for the seperate thread"""
        global gameState
        timeStep = 90 / 10000
        startTime = time.time()
        previous = time.time()
        lag = 0
        while gameState != 2:
            # Skip if the player is dead
            if player.alive == True: continue

            current = time.time()
            elapsed = current - previous
            previous = current
            lag += elapsed

            while lag >= timeStep:
                # Update player
                if player.update(world, ghosts) == 2:
                    startTime = time.time() # Makes the ghosts take time to start after respawn

                # Enemy path finding
                if time.time() > startTime + 1:
                    blinky.update(player, world, 0.01)
                if time.time() > startTime + 10:
                    clyde.update(player, world, 0.01)
                if time.time() > startTime + 15:
                    inky.update(player, world, 0.01)
                if time.time() > startTime + 20:
                    pinky.update(player, world, 0.01)

                lag -= timeStep
            sleep(0.0001)

    # Start thread
    physThread = threading.Thread(target=physLoop, args=(player, world, ghosts))

    # Main loop
    while True:
        # Run the function based on the game state
        if gameState == 0:
            # Check for key input
            startMenu.draw(window)
            window.getKey()
            gameState = 1
            startMenu.undraw()

            # Draw ready text
            ready = Text(Point(config.WINDOW_WIDTH / 2, 410), "READY!")
            ready.setSize(24)
            ready.setStyle("bold")
            ready.setTextColor("yellow")
            ready.draw(window)
            update()
            sleep(1) # Let player see the game start
            ready.undraw()

            physThread.start()
        elif gameState == 1:
            # Update score value
            score.setText(int(player.score))

            # Controls
            keys = window.checkKeys()
            # Exit loop if escape pressed or lives == 0
            if "Escape" in keys or player.life == 0:
                gameState = 2
                continue

            # Player controls
            if player.alive == False:
                if "w" in keys:
                    player.move('n')
                if "s" in keys:
                    player.move('s')
                if "a" in keys:
                    player.move('w')
                if "d" in keys:
                    player.move('e')

            # Render ghosts
            blinky.render(window)
            clyde.render(window)
            inky.render(window)
            pinky.render(window)

            # Update window and player
            player.render(window)
            window.update()
        elif gameState == 2:
            sleep(1)
            endScreen.draw(window)

            # Display score text
            score = Text(Point(config.WINDOW_WIDTH / 2, 600), "Score: " + str(player.score))
            score.setSize(32)
            score.setTextColor("white")
            score.draw(window)

            window.getKey()
            break

    # Graceful exit
    window.close()


# Call main function
main()
