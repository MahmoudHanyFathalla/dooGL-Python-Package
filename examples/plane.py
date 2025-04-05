from dooGL import *

# Initialize the 3D window
d3_init_window(width=800, height=600, depth=2000.0, text="DoGL - Plane Demonstration")

running = True
while running:
    running = magic(mouse_position=True)  # Event handling and rendering

    # Allow camera movement
    d3_camera(move=True, print_position=True)

    # Enable scaling grid
    d3_scale(depth=1000)

    # Default plane
    d3_plane(center=(-500.0, 100.0, 0.0), width=100.0, height=500.0, color=(1.0, 1.0, 1.0))

    # Large plane
    d3_plane(center=(-250.0, 100.0, 0.0), width=300.0, height=150.0, color=(1.0, 0.0, 0.0))

    # Small plane
    d3_plane(center=(0.0, 100.0, 0.0), width=100.0, height=50.0, color=(0.0, 1.0, 0.0))

    # Rotated plane (X-axis)
    d3_plane(center=(250.0, 100.0, 0.0), width=200.0, height=100.0, rotation=(45, 0, 0), color=(0.0, 0.0, 1.0))

    # Rotated plane (Y-axis)
    d3_plane(center=(500.0, 100.0, 0.0), width=200.0, height=100.0, rotation=(0, 45, 0), color=(1.0, 1.0, 0.0))

    # Plane with extreme rotation (all axes)
    d3_plane(center=(750.0, 100.0, 0.0), width=200.0, height=100.0, rotation=(45, 45, 45), color=(0.0, 1.0, 1.0))

    end()  # Swap buffers to display everything
