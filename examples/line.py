from dooGL import *

init_window(800, 600)

running = True
while running:
    running = magic()  # Handles events like mouse & keyboard input

    # Enable scaling grid
    scale(spacing=50, show_numbers=True, text_color=(1, 0, 0), font=None)

    # 1. Line from (100, 500) to (300, 500) with rotation of 30 degrees
    line(start_point=(100, 400), end_point=(300, 400), color=(1.0, 0.0, 0.0), thickness=3, rotation=30, dashed=True)

    # 2. Line from (200, 400) to (500, 600) with rotation of 45 degrees
    line(start_point=(200, 400), end_point=(300, 300), color=(0.0, 1.0, 0.0), thickness=2, rotation=45, dashed=False)

    # 3. Line from (300, 300) to (600, 300) with rotation of 60 degrees
    line(start_point=(300, 300), end_point=(400, 300), color=(0.0, 0.0, 1.0), thickness=4, rotation=60, dashed=True)

    # 4. Line from (150, 150) to (650, 150) with rotation of 90 degrees
    line(start_point=(100, 150), end_point=(30, 100), color=(1.0, 1.0, 0.0), thickness=2, rotation=90, dashed=False)

    # 5. Line from (200, 500) to (500, 100) with rotation of 120 degrees
    line(start_point=(200, 400), end_point=(200, 100), color=(0.0, 1.0, 1.0), thickness=3, rotation=120, dashed=True)

    # 6. Draw a point at (400, 300) with size 10 and red color
    point(position=(400, 300), color=(1.0, 0.0, 0.0), size=10)

    # 7. Draw a point at (100, 100) with size 8 and blue color
    point(position=(100, 100), color=(0.0, 0.0, 1.0), size=8)

    # 8. Draw a point at (700, 500) with size 6 and green color
    point(position=(600, 500), color=(0.0, 1.0, 0.0), size=6)

    # 9. Draw a point at (300, 100) with size 12 and yellow color
    point(position=(300, 100), color=(1.0, 1.0, 0.0), size=12)

    # 10. Draw a point at (500, 400) with size 14 and purple color
    point(position=(500, 400), color=(1.0, 0.0, 1.0), size=14)

    end()  # Refresh the screen
