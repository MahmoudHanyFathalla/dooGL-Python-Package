from dooGL import *

# Initialize the 3D window
d3_init_window(width=800, height=600, depth=2000.0, text="DoGL - Torus Demonstration")

running = True
while running:
    running = magic(mouse_position=True)  # Event handling and rendering

    # Enable camera movement
    d3_camera(move=True, print_position=True)

    # Enable scaling grid
    d3_scale(depth=1000)

    # Default torus
    d3_torus(center=(-500.0, 100.0, 0.0), radius=70.0, tube_radius=30.0, color=(1.0, 1.0, 1.0))

    # Large torus
    d3_torus(center=(-250.0, 100.0, 0.0), radius=50.0, tube_radius=40.0, color=(1.0, 0.0, 0.0))

    # Small torus
    d3_torus(center=(0.0, 100.0, 0.0), radius=80.0, tube_radius=20.0, color=(0.0, 1.0, 0.0))

    # Rotated torus (X-axis)
    d3_torus(center=(250.0, 100.0, 0.0), radius=30.0, tube_radius=30.0, rotation=(45, 0, 0), color=(0.0, 0.0, 1.0))

    # Rotated torus (Y-axis)
    d3_torus(center=(500.0, 100.0, 0.0), radius=60.0, tube_radius=30.0, rotation=(0, 45, 0), color=(1.0, 1.0, 0.0))

    # Torus with extreme rotation (all axes)
    d3_torus(center=(750.0, 100.0, 0.0), radius=50.0, tube_radius=30.0, rotation=(45, 45, 45), color=(0.0, 1.0, 1.0))

    end()  # Swap buffers to display everything
