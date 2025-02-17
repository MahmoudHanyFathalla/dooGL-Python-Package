from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import math
from PIL import Image
import pygame
import numpy as np

def scale(spacing=50, show_numbers=True, text_color=(1, 0, 0), font=None):
    """
    Draws the grid with an option to display small numbers beside the two main red center lines.

    :param spacing: The distance between grid lines (default is 50).
    :param show_numbers: Boolean flag to indicate whether to display numbers beside the center lines (default is False).
    :param text_color: The color of the text in (1.0, 0.0, 0.0) format (default is red).
    :param font: The Pygame font object to use for rendering the text (default is None).
    """
    # Set default font if not provided
    if font is None:
        font = pygame.font.SysFont("Arial", 12)  # Use a small font for numbers

    # Get the width and height of the display surface
    width, height = pygame.display.get_surface().get_size()

    # Calculate the center of the screen
    center_x = width // 2
    center_y = height // 2

    # Draw vertical and horizontal grid lines with the main red center lines
    for x in range(0, width, spacing):
        if x == center_x:
            glColor3f(1, 0, 0)  # Red color for the main center line
        else:
            glColor3f(0.5, 0.5, 0.5)  # Gray color for the grid lines
        
        glBegin(GL_LINES)
        glVertex2f(x, 0)
        glVertex2f(x, height)
        glEnd()

        # Display numbers beside the red vertical center line if show_numbers is True
        if show_numbers and x == center_x and x != 0:
            for y in range(0, height, spacing):
                if y != center_y:  # Skip the center point
                    text(position=(x + 5, y), text=f"{y}", font=font, text_color=text_color, background_color=(0, 0, 0, 0), size=(30, 15))

    for y in range(0, height, spacing):
        if y == center_y:
            glColor3f(1, 0, 0)  # Red color for the main center line
        else:
            glColor3f(0.5, 0.5, 0.5)  # Gray color for the grid lines
        
        glBegin(GL_LINES)
        glVertex2f(0, y)
        glVertex2f(width, y)
        glEnd()

        # Display numbers beside the red horizontal center line if show_numbers is True
        if show_numbers and y == center_y and y != 0:
            for x in range(0, width, spacing):
                if x != center_x:  # Skip the center point
                    text(position=(x, y - 15), text=f"{x}", font=font, text_color=text_color, background_color=(0, 0, 0, 0), size=(30, 15))

def rotate_point(x, y, cx, cy, angle):
    """Rotate a point around a pivot point (cx, cy) by a given angle."""
    rad = math.radians(angle)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)
    
    # Translate point to origin (pivot at (0,0))
    x -= cx
    y -= cy
    
    # Rotate point
    new_x = x * cos_a - y * sin_a
    new_y = x * sin_a + y * cos_a
    
    # Translate point back to original location
    x = new_x + cx
    y = new_y + cy
    
    return x, y

def load_texture(image_path):
    """Load an image as a texture and return the texture ID."""
    img = Image.open(image_path)
    img_data = img.convert("RGBA").tobytes()
    width, height = img.size
    
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    # Set texture parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    # Load texture data
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    
    return texture_id, width, height

def text(position=(0, 0), text="Default Text", font=None, text_color=(1, 1, 0), background_color=(0, 0.25, 0), size=(100, 50), rotation=0):
    
    """
    Draws 2D text at the given coordinates using Pygame and OpenGL, with an option to rotate the text.

    :param position: A tuple (x, y) for the text position.
    :param text: The string of text to render (default is "Default Text").
    :param font: The Pygame font object to use for rendering (default is None).
    :param text_color: The RGB color of the text in (1.0, 1.0, 1.0) format (default is yellow).
    :param background_color: The RGB background color in (1.0, 1.0, 1.0) format (default is dark green).
    :param size: A tuple (width, height) to control the size of the text area (default is (100, 50)).
    :param rotation: The angle in degrees to rotate the text (default is 0).
    """
    # Set default font if not provided
    if font is None:
        font = pygame.font.SysFont("Arial", 24)
    
    # Convert colors from (1.0, 1.0, 1.0) format to (255, 255, 255) format
    text_color = tuple(int(c * 255) for c in text_color)
    background_color = tuple(int(c * 255) for c in background_color)
    
    # Render the text using Pygame
    textSurface = font.render(text, True, text_color, background_color)
    
    # Scale the text surface to the desired width and height
    textSurface = pygame.transform.scale(textSurface, size)
    
    # Rotate the text surface if needed
    if rotation != 0:
        textSurface = pygame.transform.rotate(textSurface, rotation)
    
    # Convert the Pygame surface to a string of pixel data
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    
    # Set the position to draw the text in OpenGL (bottom-left corner of the text)
    x, y = position
    glRasterPos2d(x, y)
    
    # Draw the pixels directly onto the OpenGL window
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)