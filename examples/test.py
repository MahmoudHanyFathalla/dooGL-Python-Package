from dooGL import *

d3_init_window(width=800, height=600, depth=2000.0)
d3_camera(camera_pos=[-495,495,495])

running = True
while running:
    running = magic()
    

    # Add your drawing code here
    d3_cube(center=(0.0, 0.0, 0.0), size=100.0, rotation=(0, 0, 0), color=(1.0, 1.0, 0.0))

    end()  # Refreshes the screen and processes frame updates



from dooGL import *
import time

# Initialize a 2D window
init_window(800, 600)

# Define color sequence (19 colors)
colors = [
    (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1),
    (0.5, 0, 0), (0, 0.5, 0), (0, 0, 0.5), (0.5, 0.5, 0), (0.5, 0, 0.5), (0, 0.5, 0.5),
    (0.2, 0.6, 0.8), (0.8, 0.3, 0.1), (0.9, 0.9, 0.1), (0.1, 0.9, 0.9), (0.6, 0.1, 0.9),
    (0.3, 0.7, 0.4), (0.9, 0.1, 0.4)
]

# Initial square properties
center_x, center_y = 400, 300  # Start in the middle
size = 100
color_index = 0
rotation = 0
dx, dy = 5, 5  # Movement speed in x and y directions

running = True
while running:
    running = magic()  # Handles user input (keyboard & mouse)
    
    # Enable scaling (grid) with numbers
    scale(spacing=100, show_numbers=True, text_color=(1, 0, 0), font=None)

    # **Move the square within boundaries**
    center_x += dx
    center_y += dy

    # **Bounce off walls**
    if center_x + size / 2 >= 800 or center_x - size / 2 <= 0:
        dx = -dx  # Reverse direction on X-axis
    if center_y + size / 2 >= 600 or center_y - size / 2 <= 0:
        dy = -dy  # Reverse direction on Y-axis

    # **Change color gradually**
    color_index = (color_index + 1) % len(colors)
    current_color = colors[color_index]

    # **Rotate the square**
    rotation = (rotation + 5) % 360  # Increase rotation gradually

    # **Draw the square**
    square(center=(center_x, center_y), size=size, color=current_color, fill=True, rotation=rotation)

    end()  # Refresh the screen
    time.sleep(0.05)  # Small delay for animation smoothness
