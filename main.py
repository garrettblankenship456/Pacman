# Main file for the whole game

# Imports
from graphics3d import * # Allows 3d rendering
import config # Imports the config options

# Main function
def main():
    # Initialize window
    window = Window3d("PyCraft", config.WINDOW_WIDTH, config.WINDOW_HEIGHT)

    # Initialize scene objects
    

    # Main loop
    while True:
        # Controls
        keys = window.window.checkKeys()
        # Exit loop if escape pressed
        if "Escape" in keys:
            break

        # Game logic


        # Update window
        window.update()

    # Graceful exit
    window.window.close()


# Call main function
main()
