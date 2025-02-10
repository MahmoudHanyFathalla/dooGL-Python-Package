from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import math

def d3_torus(center=(0.0, 0.0, 0.0), radius=1.0, tube_radius=0.3, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0)):
    """
    Draws a torus with the given parameters.
    
    Parameters:
    - center: tuple of (x, y, z) for the center position of the torus.
    - radius: float representing the radius of the torus (distance from the center of the torus to the center of the tube).
    - tube_radius: float representing the radius of the tube.
    - rotation: tuple of (rot_x, rot_y, rot_z) for the rotation along x, y, z axes in degrees.
    - color: tuple of (r, g, b) representing the color of the torus (0.0 - 1.0).
    """
    x, y, z = center
    rot_x, rot_y, rot_z = rotation
    num_major = 50  # Number of segments for the major radius (smoothness of the torus)
    num_minor = 30  # Number of segments for the minor radius (smoothness of the tube)

    # Set torus color
    glColor3f(*color)

    # Save the current transformation matrix
    glPushMatrix()

    # Move to the center of the torus
    glTranslatef(x, y, z)

    # Apply rotations
    glRotatef(rot_x, 1.0, 0.0, 0.0)  # Rotate around x-axis
    glRotatef(rot_y, 0.0, 1.0, 0.0)  # Rotate around y-axis
    glRotatef(rot_z, 0.0, 0.0, 1.0)  # Rotate around z-axis

    # Draw the torus
    for i in range(num_major):
        theta1 = i * 2.0 * math.pi / num_major
        theta2 = (i + 1) * 2.0 * math.pi / num_major

        glBegin(GL_QUAD_STRIP)
        for j in range(num_minor + 1):
            phi = j * 2.0 * math.pi / num_minor

            # First point on the ring
            x1 = (radius + tube_radius * math.cos(phi)) * math.cos(theta1)
            y1 = (radius + tube_radius * math.cos(phi)) * math.sin(theta1)
            z1 = tube_radius * math.sin(phi)

            # Second point on the ring
            x2 = (radius + tube_radius * math.cos(phi)) * math.cos(theta2)
            y2 = (radius + tube_radius * math.cos(phi)) * math.sin(theta2)
            z2 = tube_radius * math.sin(phi)

            glVertex3f(x1, y1, z1)
            glVertex3f(x2, y2, z2)

        glEnd()

    # Restore the previous transformation matrix
    glPopMatrix()
