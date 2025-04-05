from dooGL import *

# Initialize the 3D window
d3_init_window(width=800, height=600, depth=2000.0, text="DoGL - Pyramid Demonstration")

running = True
while running:
    running = magic(mouse_position=True)  # Event handling and rendering

    # Allow camera movement
    d3_camera(move=True, print_position=True)

    # Enable scaling grid
    d3_scale(depth=1000)

    # Default pyramid
    d3_pyramid(center=(-500.0, 100.0, 0.0), base_width=100.0, height=150.0, color=(1.0, 1.0, 1.0))

    # Large pyramid
    d3_pyramid(center=(-250.0, 100.0, 0.0), base_width=200.0, height=250.0, color=(1.0, 0.0, 0.0))

    # Small pyramid
    d3_pyramid(center=(0.0, 100.0, 0.0), base_width=50.0, height=80.0, color=(0.0, 1.0, 0.0))

    # Rotated pyramid (X-axis)
    d3_pyramid(center=(250.0, 100.0, 0.0), base_width=100.0, height=150.0, rotation=(45, 0, 0), color=(0.0, 0.0, 1.0))

    # Rotated pyramid (Y-axis)
    d3_pyramid(center=(500.0, 100.0, 0.0), base_width=100.0, height=150.0, rotation=(0, 45, 0), color=(1.0, 1.0, 0.0))

    # Pyramid with extreme rotation (all axes)
    d3_pyramid(center=(750.0, 100.0, 0.0), base_width=100.0, height=150.0, rotation=(45, 45, 45), color=(0.0, 1.0, 1.0))

    end()  # Swap buffers to display everything
