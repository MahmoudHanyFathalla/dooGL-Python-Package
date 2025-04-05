from dooGL import *
import pygame

# Initialize Pygame and OpenGL
pygame.init()
init_window(800, 600)

running = True
while running:
    running = magic()  # Handles events like mouse & keyboard input

    # Enable scaling grid
    scale(spacing=100, show_numbers=True, text_color=(1, 0, 0), font=None)

    # 1. Simple Bezier curve with control points in the center
    bezier_curve(control_points=[(100, 100), (200, 200), (300, 100)], color=(1.0, 0.0, 0.0))

    # 2. Bezier curve with rotation and control points at the top left
    bezier_curve(control_points=[(50, 400), (150, 500), (250, 400)], color=(0.0, 1.0, 0.0), rotation=30)

    # 3. Bezier curve in the bottom right with blue color and no rotation
    bezier_curve(control_points=[(500, 500), (600, 600), (700, 500)], color=(0.0, 0.0, 1.0))

    # 4. Bezier curve in the bottom left with purple color and rotation
    bezier_curve(control_points=[(50, 50), (150, 150), (250, 50)], color=(0.5, 0.0, 0.5), rotation=45)

    # 5. Another Bezier curve with orange color and rotated on a different pivot
    bezier_curve(control_points=[(600, 150), (650, 250), (700, 150)], color=(1.0, 0.65, 0.0), rotation=60)

    # 6. Bezier curve near the center with custom control points
    bezier_curve(control_points=[(200, 300), (250, 400), (300, 300)], color=(0.0, 1.0, 1.0))

    # 7. Bezier curve with a unique control point configuration (green)
    bezier_curve(control_points=[(400, 200), (450, 250), (500, 200)], color=(0.0, 1.0, 0.0), rotation=90)

    # 8. Bezier curve in the top-right corner with pink color and rotation
    bezier_curve(control_points=[(600, 50), (650, 150), (700, 50)], color=(1.0, 0.0, 1.0), rotation=45)

    end()  # Refresh the screen
