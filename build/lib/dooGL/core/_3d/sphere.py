from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


def d3_sphere(center=(0.0, 0.0, 0.0), radius=1.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0)):
    """
    Draws a sphere with the given parameters.
    
    Parameters:
    - center: tuple of (x, y, z) for the center position of the sphere.
    - radius: float representing the radius of the sphere.
    - rotation: tuple of (rot_x, rot_y, rot_z) for the rotation along x, y, z axes in degrees.
    - color: tuple of (r, g, b) representing the color of the sphere (0.0 - 1.0).
    """
    x, y, z = center
    rot_x, rot_y, rot_z = rotation
    slices = 30  # Number of slices for the sphere, controls smoothness
    stacks = 15  # Number of stacks for the sphere, controls smoothness

    # Set sphere color
    glColor3f(*color)

    # Save the current transformation matrix
    glPushMatrix()

    # Move to the center of the sphere
    glTranslatef(x, y, z)

    # Apply rotations
    glRotatef(rot_x, 1.0, 0.0, 0.0)  # Rotate around x-axis
    glRotatef(rot_y, 0.0, 1.0, 0.0)  # Rotate around y-axis
    glRotatef(rot_z, 0.0, 0.0, 1.0)  # Rotate around z-axis

    # Draw the sphere
    for i in range(slices):
        theta1 = i * math.pi * 2 / slices
        theta2 = (i + 1) * math.pi * 2 / slices
        glBegin(GL_QUAD_STRIP)
        for j in range(stacks + 1):
            phi = j * math.pi / stacks
            x1 = radius * math.cos(theta1) * math.sin(phi)
            y1 = radius * math.sin(theta1) * math.sin(phi)
            z1 = radius * math.cos(phi)
            x2 = radius * math.cos(theta2) * math.sin(phi)
            y2 = radius * math.sin(theta2) * math.sin(phi)
            z2 = radius * math.cos(phi)
            glVertex3f(x1, y1, z1)
            glVertex3f(x2, y2, z2)
        glEnd()

    # Restore the previous transformation matrix
    glPopMatrix()
