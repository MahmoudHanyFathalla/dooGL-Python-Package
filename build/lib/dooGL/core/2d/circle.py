import math
from OpenGL.GL import *
from PIL import Image
from helper import *

def circle(center=None, radius=None, color=(1.0, 0.0, 0.0), fill=True, image=None, section=None, rotation=0):
    """
    circle(center=(400, 300), radius=100, color=(1.0, 0.0, 0.0), fill=True, image="doGl_logo.png", section="top_left", rotation=45)

    circle(
        center=(400, 300),  # The center of the circle, specifying the x and y coordinates.
        radius=100,  # The radius of the circle.
        color=(1.0, 0.0, 0.0),  # RGB color tuple (Red in this case); ignored if an image is provided.
        fill=True,  # Whether the circle should be filled (True) or just outlined (False).
        image="path_to_image.png",  # The file path to an image to be used as a texture on the circle; if provided, the color will be ignored.
        section="top_left",  # Draw only a section of the circle: "top", "bottom", "left", "right", "top_left", etc.
        rotation=45  # Rotate the section around the circle's center by the specified degree.
    )
    """
    radius=radius//2
    
    if center is None:
        center = (400, 300)  # Default center
    if radius is None:
        radius = 100  # Default radius (radius)
        
    cx, cy = center
    num_segments = 50  # Fixed number of segments for smooth circle
    
    # Set the drawing color if no image is provided
    if image:
        color = None
    else:
        glColor3f(color[0], color[1], color[2])

    # Determine the segment range based on the `section` parameter
    if section == "top_left":
        start_angle, end_angle = math.pi / 2, math.pi
    elif section == "top_right":
        start_angle, end_angle = 0, math.pi / 2
    elif section == "bottom_left":
        start_angle, end_angle = math.pi, 3 * math.pi / 2
    elif section == "bottom_right":
        start_angle, end_angle = 3 * math.pi / 2, 2 * math.pi
    elif section == "top":
        start_angle, end_angle = 0, math.pi
    elif section == "bottom":
        start_angle, end_angle = math.pi, 2 * math.pi
    elif section == "left":
        start_angle, end_angle = math.pi / 2, 3 * math.pi / 2
    elif section == "right":
        start_angle, end_angle = -math.pi / 2, math.pi / 2
    else:
        start_angle, end_angle = 0, 2 * math.pi  # Full circle by default

    # Apply rotation to the section angles
    rotation_radians = math.radians(rotation)
    start_angle += rotation_radians
    end_angle += rotation_radians

    # If an image is provided, map it as a texture to the section of the circle
    if image:
        texture_id, img_width, img_height = load_texture(image)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture_id)

    if fill:
        glBegin(GL_TRIANGLE_FAN)  # Draw filled section of the circle
        glVertex2f(cx, cy)  # Center of the circle
        
        for i in range(num_segments + 1):
            theta = start_angle + (end_angle - start_angle) * i / num_segments
            x = radius * math.cos(theta)
            y = radius * math.sin(theta)
            if image:
                glTexCoord2f((x / radius + 1) / 2, (y / radius + 1) / 2)
            glVertex2f(cx + x, cy + y)
        
        glEnd()

    else:
        glLineWidth(3)
        glBegin(GL_LINE_STRIP)  # Draw only the border
        
        for i in range(num_segments + 1):
            theta = start_angle + (end_angle - start_angle) * i / num_segments
            x = radius * math.cos(theta)
            y = radius * math.sin(theta)
            glVertex2f(cx + x, cy + y)
        
        glEnd()
        glLineWidth(1.0)

    if image:
        glDisable(GL_TEXTURE_2D)
