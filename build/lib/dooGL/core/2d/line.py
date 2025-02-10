from OpenGL.GL import *
import math
from helper import *


def line(start_point=(300,400), end_point=(500,500), color=(1.0, 1.0, 1.0), thickness=2.0, rotation=0, dashed=False):
    """
    Draws a line between two points with optional rotation, color, thickness, and dashed style.
    
    :param start_point: The starting point of the line (x, y).
    :param end_point: The ending point of the line (x, y).
    :param color: RGB color tuple (default is white).
    :param thickness: The thickness of the line.
    :param rotation: The angle to rotate the line around the start point.
    :param dashed: Whether the line should be dashed (True) or solid (False).
    """
    glColor3f(color[0], color[1], color[2])
    glLineWidth(thickness)
    
    # Rotate the end point around the start point if rotation is provided
    if rotation != 0:
        end_point = rotate_point(end_point[0], end_point[1], start_point[0], start_point[1], rotation)
    
    # Draw a dashed or solid line
    if dashed:
        glEnable(GL_LINE_STIPPLE)
        glLineStipple(1, 0x00FF)  # Dash pattern (can be customized)
    
    glBegin(GL_LINES)
    glVertex2f(start_point[0], start_point[1])
    glVertex2f(end_point[0], end_point[1])
    glEnd()
    
    if dashed:
        glDisable(GL_LINE_STIPPLE)
    
    glLineWidth(1.0)  # Reset line width to default
