from OpenGL.GL import *
import math
from helper import *


def bezier_curve(control_points, steps=100, color=(1.0, 1.0, 1.0), rotation=0):
    """
    Draws a Bezier curve using any number of control points with optional rotation.
    
    :param control_points: A list of control points [(x1, y1), (x2, y2), ...]. Must have at least two points.
    :param steps: The number of line segments to approximate the curve.
    :param color: RGB color tuple (default is white).
    :param rotation: The angle to rotate the curve.
    """
    if len(control_points) < 2:
        raise ValueError("At least two control points are required to draw a Bezier curve.")
    
    def calculate_bezier_point(t, points):
        if len(points) == 1:
            return points[0]
        new_points = []
        for i in range(len(points) - 1):
            x = (1 - t) * points[i][0] + t * points[i + 1][0]
            y = (1 - t) * points[i][1] + t * points[i + 1][1]
            new_points.append((x, y))
        return calculate_bezier_point(t, new_points)
    
    points = []
    for t in range(steps + 1):
        t /= steps
        point = calculate_bezier_point(t, control_points)
        if rotation != 0:
            pivot = control_points[0]
            point = rotate_point(point[0], point[1], pivot[0], pivot[1], rotation)
        points.append(point)
    
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_LINE_STRIP)
    for point in points:
        glVertex2f(point[0], point[1])
    glEnd()
