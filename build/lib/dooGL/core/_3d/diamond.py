from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def d3_diamond(center=(0.0, 0.0, 0.0), base_width=1.0, height=2.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0)):
    """
    Draws a diamond (two pyramids joined at the base) with the given parameters.
    
    Parameters:
    - center: tuple of (x, y, z) for the center position of the diamond.
    - base_width: float representing the width of the base of each pyramid.
    - height: float representing the height of the diamond (from top point to bottom point).
    - rotation: tuple of (rot_x, rot_y, rot_z) for the rotation along x, y, z axes in degrees.
    - color: tuple of (r, g, b) representing the color of the diamond (0.0 - 1.0).
    """
    x, y, z = center
    rot_x, rot_y, rot_z = rotation
    half_width = base_width / 2.0
    half_height = height / 2.0

    # Set diamond color
    glColor3f(*color)

    # Save the current transformation matrix
    glPushMatrix()

    # Move to the center of the diamond
    glTranslatef(x, y, z)

    # Apply rotations
    glRotatef(rot_x, 1.0, 0.0, 0.0)  # Rotate around x-axis
    glRotatef(rot_y, 0.0, 1.0, 0.0)  # Rotate around y-axis
    glRotatef(rot_z, 0.0, 0.0, 1.0)  # Rotate around z-axis

    # Define the vertices of the diamond
    top_vertex = (0.0, half_height, 0.0)       # Top vertex of the upper pyramid
    bottom_vertex = (0.0, -half_height, 0.0)   # Bottom vertex of the lower pyramid
    v0 = (-half_width, 0.0, -half_width)       # Front-left vertex of the base
    v1 = (half_width, 0.0, -half_width)        # Front-right vertex of the base
    v2 = (half_width, 0.0, half_width)         # Back-right vertex of the base
    v3 = (-half_width, 0.0, half_width)        # Back-left vertex of the base

    # Draw the top pyramid
    glBegin(GL_TRIANGLES)
    # Top vertex to base vertices
    glVertex3f(*top_vertex)
    glVertex3f(*v0)
    glVertex3f(*v1)

    glVertex3f(*top_vertex)
    glVertex3f(*v1)
    glVertex3f(*v2)

    glVertex3f(*top_vertex)
    glVertex3f(*v2)
    glVertex3f(*v3)

    glVertex3f(*top_vertex)
    glVertex3f(*v3)
    glVertex3f(*v0)
    glEnd()

    # Draw the bottom inverted pyramid
    glBegin(GL_TRIANGLES)
    # Bottom vertex to base vertices
    glVertex3f(*bottom_vertex)
    glVertex3f(*v0)
    glVertex3f(*v1)

    glVertex3f(*bottom_vertex)
    glVertex3f(*v1)
    glVertex3f(*v2)

    glVertex3f(*bottom_vertex)
    glVertex3f(*v2)
    glVertex3f(*v3)

    glVertex3f(*bottom_vertex)
    glVertex3f(*v3)
    glVertex3f(*v0)
    glEnd()

    # Restore the previous transformation matrix
    glPopMatrix()
