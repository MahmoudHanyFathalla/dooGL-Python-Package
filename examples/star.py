from dooGL import *

init_window(800, 600)

running = True
while running:
    running = magic()  # Handles events like mouse & keyboard input

    # Enable scaling grid
    scale(spacing=100, show_numbers=False, text_color=(1, 0, 0), font=None)

    # 1. Star in the center
    star(center=(400, 300), radius=100, points=5, color=(1.0, 1.0, 0.0), fill=True)

    # 2. Star near the top left with rotation
    star(center=(100, 500), radius=80, points=6, color=(0.0, 1.0, 0.0), fill=True, rotation=30)

    # 3. Star near the top right with rotation and smaller size
    star(center=(700, 100), radius=60, points=7, color=(1.0, 0.0, 0.0), fill=False, rotation=45)

    # 4. Star near the bottom left with larger size
    star(center=(100, 100), radius=120, points=5, color=(0.0, 0.0, 1.0), fill=True)

    # 5. Star in the bottom right, rotated with a different size
    star(center=(700, 500), radius=90, points=8, color=(1.0, 0.65, 0.0), fill=False, rotation=60)

    # 6. Another star in the center area with a different color and fill
    star(center=(300, 400), radius=70, points=5, color=(1.0, 1.0, 1.0), fill=False, rotation=90)

    # 7. Smaller star in the top center
    star(center=(400, 100), radius=50, points=4, color=(0.5, 0.0, 0.5), fill=True, rotation=0)

    # 8. Star near the bottom center with a unique size
    star(center=(400, 500), radius=150, points=6, color=(0.0, 1.0, 1.0), fill=True, rotation=120)

    end()  # Refresh the screen
