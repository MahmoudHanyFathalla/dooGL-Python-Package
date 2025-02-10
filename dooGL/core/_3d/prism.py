from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def d3_prism(center=(0.0, 0.0, 0.0), base_width=1.0, height=1.0, depth=1.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0)):
    """
    Draws a triangular prism with the given parameters.
    
    Parameters:
    - center: tuple of (x, y, z) for the center position of the prism.
    - base_width: float representing the width of the prism's triangular base.
    - height: float representing the height of the prism's triangular base.
    - depth: float representing the length of the prism (depth).
    - rotation: tuple of (rot_x, rot_y, rot_z) for the rotation along x, y, z axes in degrees.
    - color: tuple of (r, g, b) representing the color of the prism (0.0 - 1.0).
    """
    x, y, z = center
    rot_x, rot_y, rot_z = rotation
    half_base = base_width / 2.0
    half_depth = depth / 2.0

    # Set prism color
    glColor3f(*color)

    # Save the current transformation matrix
    glPushMatrix()

    # Move to the center of the prism
    glTranslatef(x, y, z)

    # Apply rotations
    glRotatef(rot_x, 1.0, 0.0, 0.0)  # Rotate around x-axis
    glRotatef(rot_y, 0.0, 1.0, 0.0)  # Rotate around y-axis
    glRotatef(rot_z, 0.0, 0.0, 1.0)  # Rotate around z-axis

    # Define the vertices of the triangular base (front and back)
    v0_front = (-half_base, 0.0, half_depth)  # Bottom-left of front triangle
    v1_front = (half_base, 0.0, half_depth)   # Bottom-right of front triangle
    v2_front = (0.0, height, half_depth)      # Top of front triangle

    v0_back = (-half_base, 0.0, -half_depth)  # Bottom-left of back triangle
    v1_back = (half_base, 0.0, -half_depth)   # Bottom-right of back triangle
    v2_back = (0.0, height, -half_depth)      # Top of back triangle

    # Draw front triangle
    glBegin(GL_TRIANGLES)
    glVertex3f(*v0_front)
    glVertex3f(*v1_front)
    glVertex3f(*v2_front)
    glEnd()

    # Draw back triangle
    glBegin(GL_TRIANGLES)
    glVertex3f(*v0_back)
    glVertex3f(*v1_back)
    glVertex3f(*v2_back)
    glEnd()

    # Draw the sides (connecting front and back triangles)
    glBegin(GL_QUADS)

    # Left side
    glVertex3f(*v0_front)
    glVertex3f(*v0_back)
    glVertex3f(*v2_back)
    glVertex3f(*v2_front)

    # Right side
    glVertex3f(*v1_front)
    glVertex3f(*v1_back)
    glVertex3f(*v2_back)
    glVertex3f(*v2_front)

    # Bottom side
    glVertex3f(*v0_front)
    glVertex3f(*v1_front)
    glVertex3f(*v1_back)
    glVertex3f(*v0_back)

    glEnd()

    # Restore the previous transformation matrix
    glPopMatrix()
