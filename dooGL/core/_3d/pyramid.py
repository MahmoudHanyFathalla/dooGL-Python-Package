from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def d3_pyramid(center=(0.0, 0.0, 0.0), base_width=1.0, height=1.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0)):
    """
    Draws a pyramid with the given parameters.
    
    Parameters:
    - center: tuple of (x, y, z) for the center position of the pyramid's base.
    - base_width: float representing the width of the pyramid's base.
    - height: float representing the height of the pyramid.
    - rotation: tuple of (rot_x, rot_y, rot_z) for the rotation along x, y, z axes in degrees.
    - color: tuple of (r, g, b) representing the color of the pyramid (0.0 - 1.0).
    """
    x, y, z = center
    rot_x, rot_y, rot_z = rotation
    half_base = base_width / 2.0

    # Set pyramid color
    glColor3f(*color)

    # Save the current transformation matrix
    glPushMatrix()

    # Move to the center of the pyramid's base
    glTranslatef(x, y, z)

    # Apply rotations
    glRotatef(rot_x, 1.0, 0.0, 0.0)  # Rotate around x-axis
    glRotatef(rot_y, 0.0, 1.0, 0.0)  # Rotate around y-axis
    glRotatef(rot_z, 0.0, 0.0, 1.0)  # Rotate around z-axis

    # Draw pyramid
    glBegin(GL_TRIANGLES)

    # Apex of the pyramid
    apex = (0.0, height, 0.0)

    # Four base vertices
    v0 = (-half_base, 0.0, -half_base)
    v1 = (half_base, 0.0, -half_base)
    v2 = (half_base, 0.0, half_base)
    v3 = (-half_base, 0.0, half_base)

    # Front face
    glVertex3f(*apex)
    glVertex3f(*v0)
    glVertex3f(*v1)

    # Right face
    glVertex3f(*apex)
    glVertex3f(*v1)
    glVertex3f(*v2)

    # Back face
    glVertex3f(*apex)
    glVertex3f(*v2)
    glVertex3f(*v3)

    # Left face
    glVertex3f(*apex)
    glVertex3f(*v3)
    glVertex3f(*v0)

    glEnd()

    # Draw base of the pyramid
    glBegin(GL_QUADS)
    glVertex3f(*v0)
    glVertex3f(*v1)
    glVertex3f(*v2)
    glVertex3f(*v3)
    glEnd()

    # Restore the previous transformation matrix
    glPopMatrix()
