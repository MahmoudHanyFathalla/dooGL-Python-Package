from dooGL import *


running = True
while running:
    running = magic()  # Handles events like mouse & keyboard input

    # Enable scaling grid
    scale(spacing=100, show_numbers=False, text_color=(1, 0, 0), font=None)

    # 1. Ellipse with a 100x200 radius, centered at (400, 300), filled, rotated 0 degrees
    ellipse(center=(400, 300), radius_x=100, radius_y=200, color=(1.0, 0.0, 0.0), fill=False, rotation=0)

    # 2. Ellipse with a 150x75 radius, centered at (200, 400), outlined, rotated 45 degrees
    ellipse(center=(200, 400), radius_x=150, radius_y=75, color=(0.0, 1.0, 0.0), fill=False, rotation=45)

    # 3. Ellipse with a 120x90 radius, centered at (600, 200), filled, rotated 90 degrees
    ellipse(center=(600, 200), radius_x=120, radius_y=90, color=(0.0, 0.0, 1.0), fill=True, rotation=90)

    # 4. Ellipse with a 200x100 radius, centered at (500, 500), outlined, rotated 180 degrees
    ellipse(center=(500, 500), radius_x=200, radius_y=100, color=(1.0, 1.0, 0.0), fill=False, rotation=180)

    # 5. Ellipse with a 180x120 radius, centered at (700, 100), filled, rotated 30 degrees
    ellipse(center=(700, 100), radius_x=180, radius_y=120, color=(0.0, 1.0, 1.0), fill=True, rotation=30)

    # 6. Ellipse with a 60x80 radius, centered at (300, 300), filled, rotated 60 degrees
    ellipse(center=(300, 300), radius_x=60, radius_y=80, color=(0.5, 0.2, 0.7), fill=True, rotation=60)

    # 7. Ellipse with a 200x150 radius, centered at (400, 400), filled, rotated 135 degrees
    ellipse(center=(400, 400), radius_x=200, radius_y=150, color=(0.9, 0.6, 0.3), fill=True, rotation=135)

    # 8. Ellipse with a 100x50 radius, centered at (100, 500), filled, rotated 45 degrees
    ellipse(center=(100, 500), radius_x=100, radius_y=50, color=(0.1, 0.9, 0.4), fill=True, rotation=45)

    # 9. Ellipse with a 250x200 radius, centered at (600, 600), outlined, rotated 90 degrees
    ellipse(center=(600, 600), radius_x=250, radius_y=200, color=(0.7, 0.3, 0.6), fill=False, rotation=90)

    # 10. Ellipse with a 100x150 radius, centered at (200, 200), filled, rotated 180 degrees
    ellipse(center=(200, 200), radius_x=100, radius_y=150, color=(0.8, 0.2, 0.5), fill=True, rotation=180)

    # 11. Ellipse with a 120x60 radius, centered at (500, 100), filled, rotated 270 degrees
    ellipse(center=(500, 100), radius_x=120, radius_y=60, color=(0.4, 0.2, 0.9), fill=True, rotation=270)

    # 12. Ellipse with a 180x90 radius, centered at (700, 400), outlined, rotated 45 degrees
    ellipse(center=(700, 400), radius_x=180, radius_y=90, color=(0.6, 0.8, 0.2), fill=False, rotation=45)

    end()  # Refresh the screen
