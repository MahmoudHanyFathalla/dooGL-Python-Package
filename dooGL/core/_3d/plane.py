from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *



def d3_plane(center=(0.0, 0.0, 0.0), width=1.0, height=1.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0)):
    """
    Draws a plane with the given parameters.
    
    Parameters:
    - center: tuple of (x, y, z) for the center position of the plane.
    - width: float representing the width of the plane.
    - height: float representing the height of the plane.
    - rotation: tuple of (rot_x, rot_y, rot_z) for the rotation along x, y, z axes in degrees.
    - color: tuple of (r, g, b) representing the color of the plane (0.0 - 1.0).
    """
    x, y, z = center
    rot_x, rot_y, rot_z = rotation
    half_width = width / 2.0
    half_height = height / 2.0

    # Set plane color
    glColor3f(*color)

    # Save the current transformation matrix
    glPushMatrix()

    # Move to the center of the plane
    glTranslatef(x, y, z)

    # Apply rotations
    glRotatef(rot_x, 1.0, 0.0, 0.0)  # Rotate around x-axis
    glRotatef(rot_y, 0.0, 1.0, 0.0)  # Rotate around y-axis
    glRotatef(rot_z, 0.0, 0.0, 1.0)  # Rotate around z-axis

    # Draw plane
    glBegin(GL_QUADS)

    # Plane face
    glVertex3f(-half_width, -half_height, 0.0)
    glVertex3f(half_width, -half_height, 0.0)
    glVertex3f(half_width, half_height, 0.0)
    glVertex3f(-half_width, half_height, 0.0)

    glEnd()

    # Restore the previous transformation matrix
    glPopMatrix()
