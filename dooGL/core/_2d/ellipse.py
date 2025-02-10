from OpenGL.GL import *
import math
from .helper import *



def ellipse(center=(400,300), radius_x=100, radius_y=200, color=(1.0, 1.0, 1.0), fill=True, rotation=0, image=None):
    """
    Draws an ellipse centered at a point with rotation and optional background image.
    
    :param center: The center of the ellipse (x, y).
    :param radius_x: The radius along the x-axis.
    :param radius_y: The radius along the y-axis.
    :param color: RGB color tuple (default is white).
    :param fill: Whether the ellipse should be filled (True) or just outlined (False).
    :param rotation: The angle to rotate the ellipse.
    :param image: The file path to an image to be used as a texture.
    """
    radius_x =radius_x // 2
    radius_y =radius_y // 2
    points = []
    for i in range(360):
        angle = math.radians(i)
        x = center[0] + radius_x * math.cos(angle)
        y = center[1] + radius_y * math.sin(angle)
        points.append(rotate_point(x, y, center[0], center[1], rotation))
    
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
