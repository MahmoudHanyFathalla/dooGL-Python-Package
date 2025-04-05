from dooGL import *

# Initialize the 3D window
d3_init_window(width=800, height=600, depth=2000.0, text="DoGL - Prism Demonstration")

running = True
while running:
    running = magic(mouse_position=True)  # Event handling and rendering

    # Enable camera movement
    d3_camera(move=True, print_position=True)

    # Enable scaling grid
    d3_scale(depth=1000)

    # Default triangular prism
    d3_prism(center=(-500.0, 100.0, 0.0), base_width=100.0, height=150.0, depth=100.0, color=(1.0, 1.0, 1.0))

    # Large triangular prism
    d3_prism(center=(-250.0, 100.0, 0.0), base_width=150.0, height=200.0, depth=120.0, color=(1.0, 0.0, 0.0))

    # Small triangular prism
    d3_prism(center=(0.0, 100.0, 0.0), base_width=80.0, height=100.0, depth=80.0, color=(0.0, 1.0, 0.0))

    # Rotated triangular prism (X-axis)
    d3_prism(center=(250.0, 100.0, 0.0), base_width=100.0, height=150.0, depth=100.0, rotation=(45, 0, 0), color=(0.0, 0.0, 1.0))

    # Rotated triangular prism (Y-axis)
    d3_prism(center=(500.0, 100.0, 0.0), base_width=100.0, height=150.0, depth=100.0, rotation=(0, 45, 0), color=(1.0, 1.0, 0.0))

    # Prism with extreme rotation (all axes)
    d3_prism(center=(750.0, 100.0, 0.0), base_width=100.0, height=150.0, depth=100.0, rotation=(45, 45, 45), color=(0.0, 1.0, 1.0))

    end()  # Swap buffers to display everything
