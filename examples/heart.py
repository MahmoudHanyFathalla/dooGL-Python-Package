from dooGL import *

init_window(800, 600)

running = True
while running:
    running = magic()  # Handles events like mouse & keyboard input

    # Enable scaling grid
    scale(spacing=100, show_numbers=False, text_color=(1, 0, 0), font=None)

    # 1. Heart in the center
    heart(center=(400, 300), size=2, color=(1.0, 0.0, 0.0), fill=True)

    # 2. Heart in the top left with rotation
    heart(center=(100, 500), size=3, color=(1.0, 0.5, 0.0), fill=True, rotation=45)

    # 3. Heart near the top right with rotation and smaller size
    heart(center=(700, 100), size=4, color=(0.0, 1.0, 0.0), fill=False, rotation=90)

    # 4. Heart near the bottom left with larger size
    heart(center=(100, 100), size=3, color=(0.0, 0.0, 1.0), fill=True)

    # 5. Heart in the bottom right with a different color and rotation
    heart(center=(700, 500), size=5, color=(0.5, 0.0, 0.5), fill=False, rotation=30)

    # 6. Heart in the top center with a unique fill color
    heart(center=(400, 100), size=5, color=(1.0, 1.0, 0.0), fill=True, rotation=15)

    # 7. Smaller heart near the center, rotated
    heart(center=(300, 400), size=4, color=(0.5, 0.5, 1.0), fill=False, rotation=60)

    # 8. Larger heart near the bottom center
    heart(center=(400, 500), size=5, color=(1.0, 0.0, 0.0), fill=True, rotation=120)

    end()  # Refresh the screen
