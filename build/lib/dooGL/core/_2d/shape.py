from OpenGL.GL import *
import math
from .helper import *

def shape(points=None, color=(1.0, 1.0, 1.0), line_width=2.0, point_size=5.0, rotation=0):
    """
    Draws a shape by connecting a list of points with lines or draws a single point if only one point is provided,
    with optional rotation.
    
    :param points: A list of points [(x1, y1), (x2, y2), ...]. The order matters.
    :param color: RGB color tuple (default is white).
    :param line_width: Width of the line connecting the points.
    :param point_size: Size of the point if only one point is provided.
    :param rotation: The angle to rotate the shape.
    """
    if points is None or len(points) < 1:
        raise ValueError("At least one point is required to draw.")
    
    # Rotate points around the first point if rotation is provided
    if rotation != 0 and len(points) > 1:
        pivot = points[0]  # Use the first point as the pivot
        points = [rotate_point(x, y, pivot[0], pivot[1], rotation) for x, y in points]
    
    # Draw a single point if only one point is provided
    if len(points) == 1:
        glColor3f(color[0], color[1], color[2])
        glPointSize(point_size)
        glBegin(GL_POINTS)
        glVertex2f(points[0][0], points[0][1])
        glEnd()
        glPointSize(1.0)  # Reset point size to default
    else:
        
            # Draw lines connecting the points
            glColor3f(color[0], color[1], color[2])
            glLineWidth(line_width)
            glBegin(GL_LINE_STRIP)
            for point in points:
                glVertex2f(point[0], point[1])
            glEnd()
            glLineWidth(1.0)  # Reset line width to default

