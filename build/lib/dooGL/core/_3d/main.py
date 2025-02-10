import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import os
from init import *
from helper import *
from cube import *
from camera import *
from plane import *
from pyramid import *
from prism import *
from sphere import *
from torus import *
from cylinder import *
from diamond import *
from cone import *
from move import *

if __name__ == "__main__":
    d3_init_window(width=800, height=600, depth=2000.0, text="DoGL")
    #point = (0.0, 0.0, 0.0)
    
    running = True
    while running:
       
     
        running = magic(mouse_position=True)  # Event handling and rendering

        d3_camera(        
        move=True,  # Allow camera movement
        print_position=True,  # Print camera position and rotation values
        )

        d3_background(img_width=400, img_height=300, x=0.0, y=-300.0, z=-225.0)
        d3_scale(depth=1000)
        #d3_cube(center=(0.0, 0.0, 0.0), size=100.0, rotation=(0, 0, 0), color=(1.0, 1.0, 0.0))
        #d3_plane(center=(300.0, 300.0, 300.0),width=400.0, height=400.0, rotation=(0, 0, 0), color=(1.0, 1.0, 0.0))
        #d3_plane(center=(300.0, 100.0, 500.0),width=400.0, height=400.0, rotation=(90, 0, 0), color=(1.0, 0.0, 0.0))
        #d3_plane(center=(500.0, 300.0, 500.0),width=400.0, height=400.0, rotation=(0, 90, 0), color=(0, 0.0, 1.0))
        #d3_plane(center=(300.0, 300.0, 700.0),width=400.0, height=400.0, rotation=(0, 0, 0), color=(1.0, 0.0, 1.0))
        #d3_plane(center=(300.0, 500.0, 500.0),width=400.0, height=400.0, rotation=(90, 0, 0), color=(0, 1.0, 1))
        #d3_pyramid(center=(80, 80, 80),base_width=100.0, height=200.0, rotation=(0, 0, 0), color=(0, 1, 1))
        #d3_prism(center=(0.0, 0, 0), base_width=300, height=200, depth=100, rotation=(0, 0, 0), color=(0.5, 0.0, 1.0))
        #d3_sphere(center=(0.0, 0.0, 0), radius=100, rotation=(0, 0, 0), color=(0.0, 0.5, 1.0))
        #d3_torus(center=(0.0, 0.0, 0), radius=200, tube_radius=50, rotation=(0, 0, 0), color=(1.0, 0.5, 0.0))
        #d3_cylinder(center=(100.0, 100.0, 60), radius=100, height=1000, rotation=(90, 0, 0), color=(0.5, 0.7, 1.0))
        #d3_diamond(center=(0.0, 0.0, 0), base_width=200, height=900, rotation=(0, 0, 0), color=(1.0, 0.5, 0.0))
        #point = d3_move(point, speed=1, move_forward='w', move_backward='s', 
        #            move_left='a', move_right='d', move_down='q', move_up='e')
        #d3_cube(center=point, size=100.0, rotation=(0, 0, 0), color=(1.0, 1.0, 0.0))
        






       
        pygame.display.flip() 
