from OpenGL.GL import *
import math
from helper import *


def arc(center=(400,300), radius=100, start_angle=0, end_angle=180, color=(1.0, 1.0, 1.0), line_width=2.0, rotation=0):
    """
    Draws an arc with rotation.
    
    :param center: The center of the arc (x, y).
    :param radius: The radius of the arc.
    :param start_angle: The starting angle of the arc (in degrees).
    :param end_angle: The ending angle of the arc (in degrees).
    :param color: RGB color tuple (default is white).
    :param line_width: Width of the arc line.
    :param rotation: The angle to rotate the arc.
    """
    radius = radius // 2
    points = []
    for i in range(start_angle, end_angle + 1):
        angle = math.radians(i)
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append(rotate_point(x, y, center[0], center[1], rotation))
    
    # Use texture if an image is provided
    
        glColor3f(color[0], color[1], color[2])
        glLineWidth(line_width)
        glBegin(GL_LINE_STRIP)
        for point in points:
            glVertex2f(point[0], point[1])
        glEnd()
        glLineWidth(1.0)
