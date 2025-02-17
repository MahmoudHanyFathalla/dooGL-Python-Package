from OpenGL.GL import *
import math
from .helper import *


def star(center=(400,300), radius=200, points=5, color=(1.0, 1.0, 0.0), fill=True, rotation=0):
    """
    Draws a star shape using OpenGL.

    Parameters:
    center: Tuple (x, y) for the center of the star.
    radius: Radius of the star.
    points: Number of points on the star (default is 5).
    color: RGB color tuple (default is yellow).
    fill: Boolean to decide if the star should be filled or just an outline.
    rotation: Rotation angle in degrees for the star.
    """
    radius =radius // 2
    glPushMatrix()
    
    # Translate to center
    glTranslatef(center[0], center[1], 0)
    
    # Rotate
    glRotatef(rotation, 0, 0, 1)
    
    # Set color
    glColor3f(*color)
    
    # Calculate the star's points
    angle = 360.0 / points
    half_angle = angle / 2
    coords = []

    for i in range(points * 2):
        current_angle = math.radians(i * half_angle)
        current_radius = radius if i % 2 == 0 else radius / 2
        x = current_radius * math.cos(current_angle)
        y = current_radius * math.sin(current_angle)
        coords.append((x, y))

    # Draw the star
    if fill:
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(0, 0)
        for (x, y) in coords:
            glVertex2f(x, y)
        glVertex2f(coords[0][0], coords[0][1])  # Close the shape
        glEnd()
    else:
        glBegin(GL_LINE_LOOP)
        for (x, y) in coords:
            glVertex2f(x, y)
        glVertex2f(coords[0][0], coords[0][1])  # Close the shape
        glEnd()
    
    glPopMatrix()

