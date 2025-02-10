import pygame
import math
# Dictionary to map key strings to pygame key constants
key_map = {
    # Alphabet keys
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

    # Number keys
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

    # Non-alphabetic keys
    'space': pygame.K_SPACE,
    'enter': pygame.K_RETURN,
    'esc': pygame.K_ESCAPE,
    'ctrl': pygame.K_LCTRL,  # or pygame.K_RCTRL for right control
    'shift': pygame.K_LSHIFT,  # or pygame.K_RSHIFT for right shift
}



def move(points, speed=1, up=pygame.K_UP, down=pygame.K_DOWN, left=pygame.K_LEFT, right=pygame.K_RIGHT, boundaries=True, half_raduis=0, max_y=None, min_y=None, max_x=None, min_x=None):
    keys = pygame.key.get_pressed()

    # Check if the keys are provided as strings and convert them to pygame key constants
    if isinstance(up, str):
        up = key_map.get(up.lower(), pygame.K_UP)
    if isinstance(down, str):
        down = key_map.get(down.lower(), pygame.K_DOWN)
    if isinstance(left, str):
        left = key_map.get(left.lower(), pygame.K_LEFT)
    if isinstance(right, str):
        right = key_map.get(right.lower(), pygame.K_RIGHT)

    # Handle single point case
    if isinstance(points, tuple):
        points = [points]

    # Get screen boundaries if boundaries is True
    if boundaries:
        width, height = pygame.display.get_surface().get_size()

    # Determine if any point reaches the boundary, considering the shape size and custom boundaries
    move_left = move_right = move_up = move_down = True

    for x, y in points:
        if boundaries:
            if x - half_raduis <= 0 or (min_x is not None and x - half_raduis <= min_x):
                move_left = False
            if x + half_raduis >= width or (max_x is not None and x + half_raduis >= max_x):
                move_right = False
            if y - half_raduis <= 0 or (min_y is not None and y - half_raduis <= min_y):
                move_up = False
            if y + half_raduis >= height or (max_y is not None and y + half_raduis >= max_y):
                move_down = False
        else:
            if min_x is not None and x - half_raduis <= min_x:
                move_left = False
            if max_x is not None and x + half_raduis >= max_x:
                move_right = False
            if min_y is not None and y - half_raduis <= min_y:
                move_up = False
            if max_y is not None and y + half_raduis >= max_y:
                move_down = False

    # Move points based on custom or default keyboard input and boundary checks
    for i, (x, y) in enumerate(points):
        if keys[left] and move_left:
            x -= speed
        if keys[right] and move_right:
            x += speed
        if keys[down] and move_up:
            y -= speed
        if keys[up] and move_down:
            y += speed

        points[i] = (x, y)

    # If it was a single point, return it as a tuple
    if len(points) == 1:
        return points[0]
    
    return points


