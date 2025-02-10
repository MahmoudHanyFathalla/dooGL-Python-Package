from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def d3_cube(center=(0.0, 0.0, 0.0), size=1.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0)):
    """
    Draws a cube with the given parameters.
    
    Parameters:
    - center: tuple of (x, y, z) for the center position of the cube.
    - size: float representing the width, height, and depth of the cube.
    - rotation: tuple of (rot_x, rot_y, rot_z) for the rotation along x, y, z axes in degrees.
    - color: tuple of (r, g, b) representing the color of the cube (0.0 - 1.0).
    """
    x, y, z = center
    rot_x, rot_y, rot_z = rotation
    half_size = size / 2.0

    # Set cube color
    glColor3f(*color)

    # Save the current transformation matrix
    glPushMatrix()

    # Move to the center of the cube
    glTranslatef(x, y, z)

    # Apply rotations
    glRotatef(rot_x, 1.0, 0.0, 0.0)  # Rotate around x-axis
    glRotatef(rot_y, 0.0, 1.0, 0.0)  # Rotate around y-axis
    glRotatef(rot_z, 0.0, 0.0, 1.0)  # Rotate around z-axis

    # Draw cube
    glBegin(GL_QUADS)

    # Front face
    glVertex3f(-half_size, -half_size, half_size)
    glVertex3f(half_size, -half_size, half_size)
    glVertex3f(half_size, half_size, half_size)
    glVertex3f(-half_size, half_size, half_size)

    # Back face
    glVertex3f(-half_size, -half_size, -half_size)
    glVertex3f(-half_size, half_size, -half_size)
    glVertex3f(half_size, half_size, -half_size)
    glVertex3f(half_size, -half_size, -half_size)

    # Left face
    glVertex3f(-half_size, -half_size, -half_size)
    glVertex3f(-half_size, -half_size, half_size)
    glVertex3f(-half_size, half_size, half_size)
    glVertex3f(-half_size, half_size, -half_size)

    # Right face
    glVertex3f(half_size, -half_size, -half_size)
    glVertex3f(half_size, half_size, -half_size)
    glVertex3f(half_size, half_size, half_size)
    glVertex3f(half_size, -half_size, half_size)

    # Top face
    glVertex3f(-half_size, half_size, -half_size)
    glVertex3f(-half_size, half_size, half_size)
    glVertex3f(half_size, half_size, half_size)
    glVertex3f(half_size, half_size, -half_size)

    # Bottom face
    glVertex3f(-half_size, -half_size, -half_size)
    glVertex3f(half_size, -half_size, -half_size)
    glVertex3f(half_size, -half_size, half_size)
    glVertex3f(-half_size, -half_size, half_size)

    glEnd()

    # Restore the previous transformation matrix
    glPopMatrix()
