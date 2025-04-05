from dooGL import *
import math

# Initialize a 2D window
init_window(800, 600)  # Window size 800x600

running = True
while running:
    running = magic()  # Handles events like mouse & keyboard input

    # Enable scaling grid
    scale(spacing=100, show_numbers=False, text_color=(1, 0, 0), font=None)

    # 1. Default full circle (centered)
    circle(center=(150, 150), radius=100, color=(1.0, 0.0, 0.0), fill=True)

    # 2. Large filled circle with rotation
    circle(center=(350, 150), radius=150, color=(0.0, 1.0, 0.0), fill=True, rotation=45)

    # 3. Half circle section (top half)
    circle(center=(550, 150), radius=100, color=(0.0, 0.0, 1.0), fill=True, section="top", rotation=30)

    # 4. Outlined circle
    circle(center=(150, 350), radius=100, color=(1.0, 1.0, 0.0), fill=False)

    # 5. Bottom-left section of a circle
    circle(center=(350, 350), radius=100, color=(1.0, 0.5, 0.0), fill=True, section="bottom_left")

    # 6. Circle with texture (e.g., logo)
    circle(center=(550, 350), radius=100, fill=True)

    # 7. Quarter circle section (top-left)
    circle(center=(150, 550), radius=100, color=(0.0, 1.0, 1.0), fill=True, section="top_left")

    # 8. Rotated circle section (right side)
    circle(center=(350, 550), radius=100, color=(0.5, 0.0, 0.5), fill=True, section="right", rotation=90)

    # 9. Large circle with bottom section only
    circle(center=(550, 550), radius=150, color=(0.5, 0.5, 0.0), fill=True, section="bottom")

    # 10. Small circle at the top-left corner with rotation
    circle(center=(50, 50), radius=50, color=(0.8, 0.2, 0.2), fill=True, rotation=45)

    # 11. Circle at the top-right corner with different section (top-right)
    circle(center=(750, 50), radius=50, color=(0.2, 0.8, 0.2), fill=False, section="top_right")
    circle(center=(700, 50), radius=50, color=(0.2, 0.8, 0.2), fill=True, section="top_right")

    # 12. Bottom-right corner circle with texture
    circle(center=(750, 550), radius=50,  fill=True)

    # 13. Outlined circle at bottom-left corner
    circle(center=(50, 550), radius=50, color=(0.8, 0.8, 0.0), fill=False)

    end()  # Refresh the screen
