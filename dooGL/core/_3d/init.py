import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import os




def magic(mouse_position=False):
    """
    Handles events like quitting and mouse click.
    """
    running = True
    width, height = pygame.display.get_surface().get_size()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and mouse_position:
            x, y = event.pos
            y = height - y
            print(f"Mouse clicked at: x={x}, y={y}")
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    return running


def d3_init_window(width=800, height=600, depth=1000.0, icon=None, text="DoGL Window"):
    """
    Initialize the Pygame window with the given parameters for 3D perspective.
    """
    pygame.init()
    display = (width, height)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    # Set up perspective projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, depth)  # Perspective view with a field of view of 45 degrees
    
    # Set up the camera position using gluLookAt for an angled view
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Set window title and icon
    pygame.display.set_caption(text)
    if icon is None:
        icon = "doGl_logo.png"
    
    try:
        icon = pygame.image.load(icon)
        pygame.display.set_icon(icon)
    except FileNotFoundError:
        print(f"Icon file '{icon}' not found. Using default icon.")



def d3_background(image_path=None, img_width=10.0, img_height=7.5, x=0.0, y=0.0, z=-10.0):
    """
    Renders a background image as a textured quad.
    """
    default_image = "doGl_logo.png"
    
    if image_path is None:
        image_path = os.path.join(os.path.dirname(__file__), default_image)
    else:
        image_path = os.path.join(os.path.dirname(__file__), image_path)
    
    try:
        background_image = pygame.image.load(image_path)
    except FileNotFoundError:
        print(f"Background image '{image_path}' not found.")
        return
    
    image_data = pygame.image.tostring(background_image, "RGB", True)
    image_width, image_height = background_image.get_size()
    
    glEnable(GL_TEXTURE_2D)
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image_width, image_height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
    
    glColor3f(1.0, 1.0, 1.0)
    
    half_width = img_width / 2.0
    half_height = img_height / 2.0
    
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(x - half_width, y - half_height, z)
    glTexCoord2f(1, 0); glVertex3f(x + half_width, y - half_height, z)
    glTexCoord2f(1, 1); glVertex3f(x + half_width, y + half_height, z)
    glTexCoord2f(0, 1); glVertex3f(x - half_width, y + half_height, z)
    glEnd()
    
    glDisable(GL_TEXTURE_2D)
