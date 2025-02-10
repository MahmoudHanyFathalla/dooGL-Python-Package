# square.py
import math
from OpenGL.GL import *
from PIL import Image
from .helper import *


def square(center=None, size=None, points=None, color=(1.0, 0.0, 0.0), fill=True, rotation=0, rotate_around="center", image=None):
        
    """
    square(center=(400, 300), size=100, points=[(100, 100), (200, 100), (200, 200), (100, 200)], color=(1.0, 0.0, 0.0), fill=True, rotation=45, rotate_around="center", image="doGl_logo.png")

    square(
        center=(400, 300),  # The center of the square, specifying the x and y coordinates.
        size=100,  # The size (width and height) of the square, with the center as the pivot point.
        points=[(100, 100), (200, 100), (200, 200), (100, 200)],  # Custom vertices for the square; if provided, it overrides the center and size.
        color=(1.0, 0.0, 0.0),  # RGB color tuple (Red in this case); ignored if an image is provided.
        fill=True,  # Whether the square should be filled (True) or just outlined (False).
        rotation=45,  # The angle in degrees to rotate the square. The rotation is applied around the specified pivot point.
        rotate_around="center",  # The pivot point for the rotation: 'center', 'top_left', 'top_right', 'bottom_left', or 'bottom_right'.
        image="path_to_image.png"  # The file path to an image to be used as a texture on the square; if provided, the color will be ignored.
    )
    """
    
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
            points = [
                (cx - half_size, cy - half_size),  # Bottom left
                (cx + half_size, cy - half_size),  # Bottom right
                (cx + half_size, cy + half_size),  # Top right
                (cx - half_size, cy + half_size),  # Top left
            ]
        else:
            # If neither center/size nor points are provided, use default center and size
            center = (400, 300)
            size = 100
            cx, cy = center
            half_size = size / 2
            points = [
                (cx - half_size, cy - half_size),  # Bottom left
                (cx + half_size, cy - half_size),  # Bottom right
                (cx + half_size, cy + half_size),  # Top right
                (cx - half_size, cy + half_size),  # Top left
            ]

    # Determine the pivot point for rotation
    if rotate_around == "center" and center is not None:
        pivot_x, pivot_y = center
    elif rotate_around == "top_left":
        pivot_x, pivot_y = points[3]
    elif rotate_around == "top_right":
        pivot_x, pivot_y = points[2]
    elif rotate_around == "bottom_left":
        pivot_x, pivot_y = points[0]
    elif rotate_around == "bottom_right":
        pivot_x, pivot_y = points[1]
    else:
        pivot_x, pivot_y = center if center else (0, 0)  # Default to center or (0, 0)
    
    # Rotate all points around the selected pivot point
    if rotation != 0:
        points = [rotate_point(x, y, pivot_x, pivot_y, rotation) for x, y in points]

    # If an image is provided, map it as a texture to the square
    if image:
        texture_id, img_width, img_height = load_texture(image)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture_id)

        # Correct the texture coordinates to display the image without a 180-degree rotation
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0)  # Top-left of the texture
        glVertex2f(points[0][0], points[0][1])  # Bottom left
        
        glTexCoord2f(1.0, 1.0)  # Top-right of the texture
        glVertex2f(points[1][0], points[1][1])  # Bottom right
        
        glTexCoord2f(1.0, 0.0)  # Bottom-right of the texture
        glVertex2f(points[2][0], points[2][1])  # Top right
        
        glTexCoord2f(0.0, 0.0)  # Bottom-left of the texture
        glVertex2f(points[3][0], points[3][1])  # Top left
        glEnd()
        
        glDisable(GL_TEXTURE_2D)
    else:
        # Draw the square (either filled or just the border)
        if fill:
            glBegin(GL_QUADS)  # Draw filled square
        else:
            glLineWidth(3)
            glBegin(GL_LINE_LOOP)  # Draw only the border
        
        for vertex in points:
            glVertex2f(vertex[0], vertex[1])
        
        glEnd()
        if not fill:
            glLineWidth(1.0)