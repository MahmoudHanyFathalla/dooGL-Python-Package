from OpenGL.GL import *
import math
from helper import *


def heart(center=(400,300), size=5, color=(1.0, 0.0, 0.0), fill=True, rotation=0):
    """
    Draws a heart shape centered at a given point with the specified size.
    
    :param center: The center of the heart (x, y).
    :param size: The size of the heart starts from 1 to 20 most common range (affects the width and height).
    :param color: RGB color tuple (default is red).
    :param fill: Whether the heart should be filled (True) or just outlined (False).
    :param rotation: The angle to rotate the heart.
    """
    glColor3f(color[0], color[1], color[2])
    
    # Define the heart shape using mathematical equations
    vertices = []
    for angle in range(360):
        angle_rad = math.radians(angle)
        x = size * 16 * math.sin(angle_rad)**3
        y = size * (13 * math.cos(angle_rad) - 5 * math.cos(2 * angle_rad) - 2 * math.cos(3 * angle_rad) - math.cos(4 * angle_rad))
        rotated_x, rotated_y = rotate_point(x + center[0], y + center[1], center[0], center[1], rotation)
        vertices.append((rotated_x, rotated_y))
    
    if fill:
        glBegin(GL_POLYGON)
    else:
        glBegin(GL_LINE_LOOP)
    
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    
    glEnd()
