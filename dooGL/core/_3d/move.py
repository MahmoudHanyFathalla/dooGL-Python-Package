from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame


# Dictionary to map key strings to pygame key constants
key_map = {
    'a': pygame.K_a,
    'b': pygame.K_b,
    'c': pygame.K_c,
    'd': pygame.K_d,
    'e': pygame.K_e,
    'f': pygame.K_f,
    'g': pygame.K_g,
    'h': pygame.K_h,
    'i': pygame.K_i,
    'j': pygame.K_j,
    'k': pygame.K_k,
    'l': pygame.K_l,
    'm': pygame.K_m,
    'n': pygame.K_n,
    'o': pygame.K_o,
    'p': pygame.K_p,
    'q': pygame.K_q,
    'r': pygame.K_r,
    's': pygame.K_s,
    't': pygame.K_t,
    'u': pygame.K_u,
    'v': pygame.K_v,
    'w': pygame.K_w,
    'x': pygame.K_x,
    'y': pygame.K_y,
    'z': pygame.K_z,
    
    '0': pygame.K_0,
    '1': pygame.K_1,
    '2': pygame.K_2,
    '3': pygame.K_3,
    '4': pygame.K_4,
    '5': pygame.K_5,
    '6': pygame.K_6,
    '7': pygame.K_7,
    '8': pygame.K_8,
    '9': pygame.K_9,

    'space': pygame.K_SPACE,
    'enter': pygame.K_RETURN,
    'esc': pygame.K_ESCAPE,
    'ctrl': pygame.K_LCTRL,
    'shift': pygame.K_LSHIFT,
}



def d3_move(point=(0.0, 0.0, 0.0), speed=0.1, 
            move_forward=None, move_backward=None, 
            move_left=None, move_right=None, 
            move_down=None, move_up=None):
    """
    Moves a 3D point in x, y, or z directions based on specified keyboard input.
    
    Parameters:
    - point: tuple of (x, y, z) representing the current position of the point.
    - speed: float representing the speed of movement.
    - move_forward: character representing the key to move forward (decrease z).
    - move_backward: character representing the key to move backward (increase z).
    - move_left: character representing the key to move left (decrease x).
    - move_right: character representing the key to move right (increase x).
    - move_down: character representing the key to move down (decrease y).
    - move_up: character representing the key to move up (increase y).
    
    Returns:
    - Updated position of the point as a tuple (x, y, z).
    """
    x, y, z = point

    keys = pygame.key.get_pressed()

    # Use specified control keys to move the point
    if move_forward and keys[key_map[move_forward]]:  # Move forward in z-axis
        z -= speed
    if move_backward and keys[key_map[move_backward]]:  # Move backward in z-axis
        z += speed
    if move_left and keys[key_map[move_left]]:  # Move left in x-axis
        x -= speed
    if move_right and keys[key_map[move_right]]:  # Move right in x-axis
        x += speed
    if move_down and keys[key_map[move_down]]:  # Move down in y-axis
        y -= speed
    if move_up and keys[key_map[move_up]]:  # Move up in y-axis
        y += speed

    return x, y, z
