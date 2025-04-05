from dooGL import *

init_window(800, 600)

running = True
while running:
    running = magic()  # Handles events like mouse & keyboard input

    # Enable scaling grid
    scale(spacing=100, show_numbers=False, text_color=(1, 0, 0), font=None)

    # 1. Arc in the top-left corner with a rotation of 30 degrees
    arc(center=(100, 500), radius=100, start_angle=0, end_angle=180, color=(1.0, 0.0, 0.0), line_width=3, rotation=30)

    # 2. Arc in the top-right corner with a rotation of 45 degrees
    arc(center=(700, 500), radius=80, start_angle=45, end_angle=225, color=(0.0, 1.0, 0.0), line_width=4, rotation=45)

    # 3. Arc in the center of the screen with a rotation of 60 degrees
    arc(center=(400, 300), radius=150, start_angle=0, end_angle=270, color=(0.0, 0.0, 1.0), line_width=2, rotation=60)

    # 4. Arc in the bottom-left corner with a rotation of 90 degrees
    arc(center=(100, 100), radius=50, start_angle=90, end_angle=180, color=(1.0, 1.0, 0.0), line_width=2, rotation=90)

    # 5. Arc in the bottom-right corner with a rotation of 120 degrees
    arc(center=(700, 100), radius=120, start_angle=0, end_angle=180, color=(1.0, 0.5, 0.0), line_width=3, rotation=120)

    # 6. Arc near the center-top with a rotation of 150 degrees
    arc(center=(400, 50), radius=100, start_angle=180, end_angle=360, color=(0.5, 0.0, 0.5), line_width=2, rotation=150)

    # 7. Arc near the top-right with a rotation of 180 degrees
    arc(center=(650, 150), radius=90, start_angle=90, end_angle=270, color=(0.0, 1.0, 1.0), line_width=4, rotation=180)

    # 8. Arc near the bottom-left with a rotation of 210 degrees
    arc(center=(150, 450), radius=70, start_angle=0, end_angle=90, color=(0.0, 1.0, 0.5), line_width=3, rotation=210)

    end()  # Refresh the screen
