from OpenGL.GL import *
import math
from helper import *


def polygon(center=(400,300), sides=6, radius=200, color=(1.0, 1.0, 1.0), fill=True, rotation=0, image=None):
    """
    Draws a regular polygon with the specified number of sides, rotation, and optional background image.
    
    :param center: The center of the polygon (x, y).
    :param sides: The number of sides of the polygon (e.g., 3 for triangle, 5 for pentagon).
    :param radius: The radius of the polygon (distance from center to a vertex).
    :param color: RGB color tuple (default is white).
    :param fill: Whether the polygon should be filled (True) or just outlined (False).
    :param rotation: The angle to rotate the polygon.
    :param image: The file path to an image to be used as a texture.
    """
    radius= radius //2
    if sides < 3:
        raise ValueError("Polygon must have at least 3 sides.")
    
    points = []
    angle_step = 360 / sides
    for i in range(sides):
        angle = math.radians(i * angle_step + rotation)
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append((x, y))
    
    # Use texture if an image is provided
    if image:
        texture_id, img_width, img_height = load_texture(image)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        
        glBegin(GL_POLYGON)
        for i, point in enumerate(points):
            glTexCoord2f(i % 2, i // 2)
            glVertex2f(point[0], point[1])
        glEnd()
        
        glDisable(GL_TEXTURE_2D)
    else:
        glColor3f(color[0], color[1], color[2])
        if fill:
            glBegin(GL_POLYGON)
        else:
            glLineWidth(3)
            glBegin(GL_LINE_LOOP)
        
        for point in points:
            glVertex2f(point[0], point[1])
        
        glEnd()
        if not fill:
            glLineWidth(1.0)
