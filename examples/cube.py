from dooGL import *

# Initialize the 3D window
d3_init_window(width=800, height=600, depth=2000.0, text="DoGL - Cube Demonstration")

running = True
while running:
    running = magic(mouse_position=True)  # Event handling and rendering

    # Allow camera movement
    d3_camera(move=True, print_position=True)

    # Enable scaling grid
    d3_scale(depth=1000)

    # Default cube
    d3_cube(center=(-500.0, 100.0, 0.0), size=100.0, color=(1.0, 1.0, 1.0))

    # Large cube
    d3_cube(center=(-250.0, 100.0, 0.0), size=200.0, color=(1.0, 0.0, 0.0))

    # Small cube
    d3_cube(center=(0.0, 100.0, 0.0), size=50.0, color=(0.0, 1.0, 0.0))

    # Rotated cube (X-axis)
    d3_cube(center=(250.0, 100.0, 0.0), size=100.0, rotation=(45, 0, 0), color=(0.0, 0.0, 1.0))

    # Rotated cube (Y-axis)
    d3_cube(center=(500.0, 100.0, 0.0), size=100.0, rotation=(0, 45, 0), color=(1.0, 1.0, 0.0))

    # Cube with extreme rotation (all axes)
    d3_cube(center=(750.0, 100.0, 0.0), size=100.0, rotation=(45, 45, 45), color=(0.0, 1.0, 1.0))

    end()  # Swap buffers to display everything
