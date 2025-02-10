import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


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
def d3_camera(camera_pos=[-495,495,495], speed=0.1, rotation=[25, 45, 0], rotation_speed=0.1, move=False, print_position=False,
              forward_z='w', backward_z='s', left_x='a', right_x='d', up_y='q', down_y='e', 
              rotate_up_x='up', rotate_down_x='down', rotate_left_y='left', rotate_right_y='right',
              roll_left_z='z', roll_right_z='x', 
              boundaries=False, max_y=None, min_y=None, max_x=None, min_x=None, max_z=None, min_z=None,
              rotate_x_max=None, rotate_x_min=None, rotate_y_max=None, rotate_y_min=None, rotate_z_max=None, rotate_z_min=None):
    
    keys = pygame.key.get_pressed()

    # Convert string keys to pygame constants using the key_map
    forward_z = key_map.get(forward_z.lower(), pygame.K_w)
    backward_z = key_map.get(backward_z.lower(), pygame.K_s)
    left_x = key_map.get(left_x.lower(), pygame.K_a)
    right_x = key_map.get(right_x.lower(), pygame.K_d)
    up_y = key_map.get(up_y.lower(), pygame.K_q)
    down_y = key_map.get(down_y.lower(), pygame.K_e)
    rotate_up_x = key_map.get(rotate_up_x.lower(), pygame.K_UP)
    rotate_down_x = key_map.get(rotate_down_x.lower(), pygame.K_DOWN)
    rotate_left_y = key_map.get(rotate_left_y.lower(), pygame.K_LEFT)
    rotate_right_y = key_map.get(rotate_right_y.lower(), pygame.K_RIGHT)
    roll_left_z = key_map.get(roll_left_z.lower(), pygame.K_z)
    roll_right_z = key_map.get(roll_right_z.lower(), pygame.K_x)

    # Check boundaries for movement
    move_left = move_right = move_up = move_down = move_forward = move_backward = True
    if boundaries:
        if min_x is not None and camera_pos[0] - speed <= min_x:
            move_left = False
        if max_x is not None and camera_pos[0] + speed >= max_x:
            move_right = False
        if min_y is not None and camera_pos[1] - speed <= min_y:
            move_down = False
        if max_y is not None and camera_pos[1] + speed >= max_y:
            move_up = False
        if min_z is not None and camera_pos[2] - speed <= min_z:
            move_forward = False
        if max_z is not None and camera_pos[2] + speed >= max_z:
            move_backward = False

    # Camera translation based on key input and boundary checks
    if move:
        if keys[forward_z] and move_forward:  # Move forward in Z
            camera_pos[2] -= speed
        if keys[backward_z] and move_backward:  # Move backward in Z
            camera_pos[2] += speed
        if keys[left_x] and move_left:  # Move left in X
            camera_pos[0] -= speed
        if keys[right_x] and move_right:  # Move right in X
            camera_pos[0] += speed
        if keys[up_y] and move_up:  # Move up in Y
            camera_pos[1] += speed
        if keys[down_y] and move_down:  # Move down in Y
            camera_pos[1] -= speed

        # Camera rotation based on key input and boundary checks for rotation
        if keys[rotate_up_x]:  # Rotate up (decrease pitch on X-axis)
            rotation[0] -= rotation_speed
            if rotate_x_min is not None and rotation[0] < rotate_x_min:
                rotation[0] = rotate_x_min
        if keys[rotate_down_x]:  # Rotate down (increase pitch on X-axis)
            rotation[0] += rotation_speed
            if rotate_x_max is not None and rotation[0] > rotate_x_max:
                rotation[0] = rotate_x_max
        if keys[rotate_left_y]:  # Rotate left (yaw on Y-axis)
            rotation[1] -= rotation_speed
            if rotate_y_min is not None and rotation[1] < rotate_y_min:
                rotation[1] = rotate_y_min
        if keys[rotate_right_y]:  # Rotate right (yaw on Y-axis)
            rotation[1] += rotation_speed
            if rotate_y_max is not None and rotation[1] > rotate_y_max:
                rotation[1] = rotate_y_max
        if keys[roll_left_z]:  # Roll left (rotate on Z-axis)
            rotation[2] -= rotation_speed
            if rotate_z_min is not None and rotation[2] < rotate_z_min:
                rotation[2] = rotate_z_min
        if keys[roll_right_z]:  # Roll right (rotate on Z-axis)
            rotation[2] += rotation_speed
            if rotate_z_max is not None and rotation[2] > rotate_z_max:
                rotation[2] = rotate_z_max

    # Update the camera view
    glLoadIdentity()
    
    # Apply rotations in the order Z (roll), Y (yaw), X (pitch)
    glRotatef(rotation[0], 1, 0, 0)  # Pitch (X-axis)
    glRotatef(rotation[1], 0, 1, 0)  # Yaw (Y-axis)
    glRotatef(rotation[2], 0, 0, 1)  # Roll (Z-axis)
    
    # Look at the target position
    target_pos = [camera_pos[0], camera_pos[1], camera_pos[2] - 1]
    gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2],  # Camera position
              target_pos[0], target_pos[1], target_pos[2],  # Look at the target
              0, 1, 0)  # Up vector (Y-axis is up)

    # Print camera position and rotation if the flag is set to True
    if print_position:
        print(f"Camera Position: X={camera_pos[0]}, Y={camera_pos[1]}, Z={camera_pos[2]}")
        print(f"Rotation: Pitch (X)={rotation[0]}, Yaw (Y)={rotation[1]}, Roll (Z)={rotation[2]}")
