import math
from OpenGL.GL import *
from PIL import Image
from helper import *

def triangle(center=None, size=None, points=None, color=(1.0, 0.0, 0.0), fill=True, rotation=0, rotate_around="center", image=None):
    # Set the drawing color if no image is provided
    if image:
        color = None
    else:
        glColor3f(color[0], color[1], color[2])

    # If points are provided, ignore center and size
    if points is not None:
        center, size = None, None
    else:
        # Define vertices based on center and size
        if center is not None and size is not None:
            cx, cy = center
            half_size = size / 2
            height = math.sqrt(size**2 - (size / 2)**2)
            points = [
                (cx, cy + height / 2),  # Top vertex
                (cx - half_size, cy - height / 2),  # Bottom left vertex
                (cx + half_size, cy - height / 2),  # Bottom right vertex
            ]
        else:
            # If neither center/size nor points are provided, use default center and size
            center = (400, 300)
            size = 100
            cx, cy = center
            half_size = size / 2
            height = math.sqrt(size**2 - (size / 2)**2)
            points = [
                (cx, cy + height / 2),  # Top vertex
                (cx - half_size, cy - height / 2),  # Bottom left vertex
                (cx + half_size, cy - height / 2),  # Bottom right vertex
            ]

    # Determine the pivot point for rotation
    if rotate_around == "center" and center is not None:
        pivot_x, pivot_y = center
    elif rotate_around == "top":
        pivot_x, pivot_y = points[0]
    elif rotate_around == "bottom_left":
        pivot_x, pivot_y = points[1]
    elif rotate_around == "bottom_right":
        pivot_x, pivot_y = points[2]
    else:
        pivot_x, pivot_y = center if center else (0, 0)  # Default to center or (0, 0)
    
    # Rotate all points around the selected pivot point
    if rotation != 0:
        points = [rotate_point(x, y, pivot_x, pivot_y, rotation) for x, y in points]

    # If an image is provided, map it as a texture to the triangle
    if image:
        texture_id, img_width, img_height = load_texture(image)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture_id)

        glBegin(GL_TRIANGLES)
        glTexCoord2f(0.5, 1.0)  # Top of the texture
        glVertex2f(points[0][0], points[0][1])  # Top vertex
        
        glTexCoord2f(0.0, 0.0)  # Bottom-left of the texture
        glVertex2f(points[1][0], points[1][1])  # Bottom left
        
        glTexCoord2f(1.0, 0.0)  # Bottom-right of the texture
        glVertex2f(points[2][0], points[2][1])  # Bottom right
        glEnd()
        
        glDisable(GL_TEXTURE_2D)
    else:
        # Draw the triangle (either filled or just the border)
        if fill:
            glBegin(GL_TRIANGLES)  # Draw filled triangle
        else:
            glLineWidth(3)
            glBegin(GL_LINE_LOOP)  # Draw only the border
        
        for vertex in points:
            glVertex2f(vertex[0], vertex[1])
        
        glEnd()
        if not fill:
            glLineWidth(1.0)
