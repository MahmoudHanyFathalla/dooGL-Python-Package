from dooGL import *

# Initialize a 2D window
init_window(800, 600)  # Window size 800x600

running = True
while running:
    running = magic()  # Handles events like mouse & keyboard input

    # Enable scaling grid
    scale(spacing=100, show_numbers=False, text_color=(1, 0, 0), font=None)

    # 1. Default square (centered)
    square(center=(150, 150), size=100, color=(1.0, 0.0, 0.0), fill=True)

    # 2. Larger square
    square(center=(350, 150), size=150, color=(0.0, 1.0, 0.0), fill=True)

    # 3. Rotated square
    square(center=(550, 150), size=100, color=(0.0, 0.0, 1.0), fill=True, rotation=45)

    # 4. Outlined square
    square(center=(150, 350), size=100, color=(1.0, 1.0, 0.0), fill=False)

    # 5. Square rotated around bottom-left corner
    square(center=(350, 300), size=100, color=(1.0, 0.5, 0.0), fill=True, rotation=30, rotate_around="bottom_left")

    # 6. Square with texture
    square(center=(550, 350), size=100,image="doGl_logo.png")

    # 7. Smaller square with different position
    square(center=(150, 500), size=50, color=(0.0, 1.0, 1.0), fill=True)

    # 8. Square with very large size
    square(center=(350, 500), size=200, color=(0.5, 0.0, 0.5), fill=False,image="doGl_logo.png")

    # 9. Rotated square at 90 degrees
    square(center=(550, 500), size=100, color=(0.5, 0.5, 0.0), fill=True, rotation=90)

    # 10. Square at the top-left corner with rotation
    square(center=(50, 50), size=100, color=(0.0, 0.5, 0.5), fill=True, rotation=15)

    # 11. Square at the top-right corner with a different color
    square(center=(750, 50), size=100, color=(0.8, 0.2, 0.2), fill=True)

    # 12. Square at the bottom-left corner
    square(center=(50, 550), size=100, color=(0.8, 0.8, 0.0), fill=True)

    # 13. Square at the bottom-right corner with rotation and outline
    square(center=(750, 550), size=100, color=(0.2, 0.8, 0.2), fill=False, rotation=60)

    end()  # Refresh the screen
