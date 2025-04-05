from dooGL import *

# Initialize a 2D window
init_window(800, 600)  # Initialize window with size 800x600

running = True
while running:
    running = magic()  # Handles events like mouse & keyboard input
    
    # Enable scaling (grid) with numbers
    scale(spacing=100, show_numbers=False, text_color=(1, 0, 0), font=None)

    # Draw a square for reference
    square(center=(200, 200), size=100, color=(0.0, 0.0, 1.0), fill=True, rotation=0)

    end()  # Refresh the screen