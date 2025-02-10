from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def d3_cylinder(center=(0.0, 0.0, 0.0), radius=1.0, height=2.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0)):
    """
    Draws a cylinder with the given parameters.
    
    Parameters:
    - center: tuple of (x, y, z) for the center position of the cylinder's base.
    - radius: float representing the radius of the cylinder.
    - height: float representing the height of the cylinder.
    - rotation: tuple of (rot_x, rot_y, rot_z) for the rotation along x, y, z axes in degrees.
    - color: tuple of (r, g, b) representing the color of the cylinder (0.0 - 1.0).
    """
    x, y, z = center
    rot_x, rot_y, rot_z = rotation
    slices = 50  # Number of slices for smoothness

    # Set cylinder color
    glColor3f(*color)

    # Save the current transformation matrix
    glPushMatrix()

    # Move to the center of the cylinder's base
    glTranslatef(x, y, z)

    # Apply rotations
    glRotatef(rot_x, 1.0, 0.0, 0.0)  # Rotate around x-axis
    glRotatef(rot_y, 0.0, 1.0, 0.0)  # Rotate around y-axis
    glRotatef(rot_z, 0.0, 0.0, 1.0)  # Rotate around z-axis

    # Draw the cylinder body
    glBegin(GL_QUAD_STRIP)
    for i in range(slices + 1):
        theta = i * 2.0 * math.pi / slices
        x1 = radius * math.cos(theta)
        y1 = radius * math.sin(theta)

        # Draw two points for each quad (bottom and top)
        glVertex3f(x1, y1, 0.0)            # Bottom edge of cylinder
        glVertex3f(x1, y1, height)         # Top edge of cylinder
    glEnd()

    # Draw the top and bottom caps
    for cap_z in [0.0, height]:
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0.0, 0.0, cap_z)  # Center of the cap
        for i in range(slices + 1):
            theta = i * 2.0 * math.pi / slices
            x1 = radius * math.cos(theta)
            y1 = radius * math.sin(theta)
            glVertex3f(x1, y1, cap_z)
        glEnd()

    # Restore the previous transformation matrix
    glPopMatrix()
