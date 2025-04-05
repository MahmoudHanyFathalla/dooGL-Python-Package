from dooGL import *

# Initialize the 3D window
d3_init_window(width=800, height=600, depth=2000.0, text="DoGL - Sphere Demonstration")

running = True
while running:
    running = magic(mouse_position=True)  # Event handling and rendering

    # Enable camera movement
    d3_camera(move=True, print_position=True)

    # Enable scaling grid
    d3_scale(depth=1000)

    # Default sphere
    d3_sphere(center=(-500.0, 100.0, 0.0), radius=50.0, color=(1.0, 1.0, 1.0))

    # Large sphere
    d3_sphere(center=(-250.0, 100.0, 0.0), radius=75.0, color=(1.0, 0.0, 0.0))

    # Small sphere
    d3_sphere(center=(0.0, 100.0, 0.0), radius=30.0, color=(0.0, 1.0, 0.0))

    # Rotated sphere (X-axis)
    d3_sphere(center=(250.0, 100.0, 0.0), radius=50.0, rotation=(45, 0, 0), color=(0.0, 0.0, 1.0))

    # Rotated sphere (Y-axis)
    d3_sphere(center=(500.0, 100.0, 0.0), radius=50.0, rotation=(0, 45, 0), color=(1.0, 1.0, 0.0))

    # Sphere with extreme rotation (all axes)
    d3_sphere(center=(750.0, 100.0, 0.0), radius=50.0, rotation=(45, 45, 45), color=(0.0, 1.0, 1.0))

    end()  # Swap buffers to display everything
