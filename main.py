# Main file for the whole game

# Imports
from graphics import * # 2D graphics library
from world import * # Get all the classes from the folder
import config # Imports the config options

# Main function
def main():
    # Initialize window
    window = GraphWin("Pacman", config.WINDOW_WIDTH, config.WINDOW_HEIGHT, autoflush=False)

    # Initialize world
    world = World()
    world.render(window)

    # Initialize scene objects
    

    # Main loop
    while True:
        # Controls
        keys = window.checkKeys()
        # Exit loop if escape pressed
        if "Escape" in keys:
            break

        # Game logic
        

        # Update window
        update()

    # Graceful exit
    window.close()


# Call main function
main()
