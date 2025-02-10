import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *




def d3_scale(depth=500.0):
    """
    Draws the X, Y, and Z axes in the 3D space.
    """
    width, height = pygame.display.get_surface().get_size()
    glEnable(GL_LINE_SMOOTH)
    glBegin(GL_LINES)
    
    # X-axis (Yellow)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-width, 0, 0)
    glVertex3f(width, 0, 0)
    
    # Y-axis (Red)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0, -height, 0)
    glVertex3f(0, height, 0)
    
    # Z-axis (Blue, extended from -depth to +depth)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0, 0, -depth)
    glVertex3f(0, 0, depth)
    
    glEnd()
    glDisable(GL_LINE_SMOOTH)
