from dooGL import *
import math

# Initialize a 2D window
init_window(800, 600)  # Window size 800x600

running = True
while running:
    running = magic()  # Handles events like mouse & keyboard input

    # Enable scaling grid
    scale(spacing=100, show_numbers=False, text_color=(1, 0, 0), font=None)

    # 1. Default triangle (centered)
    triangle(center=(150, 150), size=100, color=(1.0, 0.0, 0.0), fill=True)

    # 2. Larger triangle
    triangle(center=(350, 150), size=150, color=(0.0, 1.0, 0.0), fill=True)

    # 3. Rotated triangle
    triangle(center=(550, 150), size=100, color=(0.0, 0.0, 1.0), fill=True, rotation=45)

    # 4. Outlined triangle
    triangle(center=(150, 350), size=100, color=(1.0, 1.0, 0.0), fill=False)

    # 5. Triangle rotated around bottom-left corner
    triangle(center=(350, 350), size=100, color=(1.0, 0.5, 0.0), fill=True, rotation=30, rotate_around="bottom_left")

    # 6. Triangle with texture
    triangle(center=(550, 350), color=(1.0, 1.0, 1.0), size=100, image="doGl_logo.png")

    # 7. Smaller triangle with different position
    triangle(center=(150, 500), size=50, color=(0.0, 1.0, 1.0), fill=True)

    # 8. Triangle with very large size
    triangle(center=(350, 500), size=200, color=(0.5, 0.0, 0.5), fill=True)

    # 9. Rotated triangle at 90 degrees
    triangle(center=(550, 500), size=100, color=(0.5, 0.5, 0.0), fill=True, rotation=90)

    # 10. Triangle at the top-left corner with rotation
    triangle(center=(50, 50), size=100, color=(0.0, 0.5, 0.5), fill=True, rotation=15)

    # 11. Triangle at the top-right corner with a different color
    triangle(center=(750, 50), size=100, color=(0.8, 0.2, 0.2), fill=True)

    # 12. Triangle at the bottom-left corner
    triangle(center=(50, 550), size=100, color=(0.8, 0.8, 0.0), fill=True)

    # 13. Triangle at the bottom-right corner with rotation and outline
    triangle(center=(750, 550), size=100, color=(0.2, 0.8, 0.2), fill=False, rotation=60)

    end()  # Refresh the screen
