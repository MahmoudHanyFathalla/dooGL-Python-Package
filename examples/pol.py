from dooGL import *
import pygame
import math

# Initialize Pygame and OpenGL
pygame.init()
init_window(800, 600)

running = True
while running:
    running = magic()  # Handles events like mouse & keyboard input

    # Enable scaling grid
    scale(spacing=100, show_numbers=False, text_color=(1, 0, 0), font=None)

    # 1. Polygon with 6 sides (hexagon) centered at (400, 300), filled, rotated 0 degrees
    polygon(center=(400, 300), sides=6, radius=100, color=(1.0, 0.0, 0.0), fill=True, rotation=0)

    # 2. Polygon with 5 sides (pentagon) centered at (600, 400), outlined, rotated 30 degrees
    polygon(center=(600, 400), sides=5, radius=80, color=(0.0, 1.0, 0.0), fill=False, rotation=30)

    # 3. Polygon with 3 sides (triangle) centered at (200, 100), filled, rotated 60 degrees
    polygon(center=(200, 100), sides=3, radius=60, color=(0.0, 0.0, 1.0), fill=True, rotation=60)

    # 4. Polygon with 8 sides (octagon) centered at (500, 300), filled, rotated 90 degrees
    polygon(center=(500, 300), sides=8, radius=120, color=(1.0, 1.0, 0.0), fill=True, rotation=90)

    # 5. Polygon with 4 sides (square) centered at (700, 500), outlined, rotated 120 degrees
    polygon(center=(700, 500), sides=4, radius=50, color=(0.0, 1.0, 1.0), fill=False, rotation=120)

    # 6. Polygon with 7 sides (heptagon) centered at (300, 400), filled, rotated 45 degrees
    polygon(center=(300, 400), sides=7, radius=90, color=(0.5, 0.2, 0.7), fill=True, rotation=45)

    # 7. Polygon with 9 sides (nonagon) centered at (600, 200), filled, rotated 180 degrees
    polygon(center=(600, 200), sides=9, radius=110, color=(0.2, 0.5, 0.8), fill=True, rotation=180)

    # 8. Polygon with 10 sides (decagon) centered at (500, 500), outlined, rotated 60 degrees
    polygon(center=(500, 500), sides=10, radius=130, color=(0.9, 0.6, 0.3), fill=False, rotation=60)

    # 9. Polygon with 12 sides (dodecagon) centered at (200, 500), filled, rotated 45 degrees
    polygon(center=(200, 500), sides=12, radius=150, color=(0.8, 0.2, 0.5), fill=True, rotation=45)

    # 10. Polygon with 20 sides (icosagon) centered at (700, 300), filled, rotated 90 degrees
    polygon(center=(700, 300), sides=20, radius=100, color=(0.1, 0.9, 0.4), fill=True, rotation=90)

    # 11. Polygon with 15 sides (pentadecagon) centered at (400, 100), filled, rotated 30 degrees
    polygon(center=(400, 100), sides=15, radius=90, color=(0.5, 0.1, 0.9), fill=True, rotation=30)

    # 12. Polygon with 11 sides (hendecagon) centered at (650, 400), outlined, rotated 150 degrees
    polygon(center=(650, 400), sides=11, radius=80, color=(0.7, 0.3, 0.6), fill=False, rotation=150)

    end()  # Refresh the screen
