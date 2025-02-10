import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from PIL import Image
import math
from .square import *  
from .init import *
from .helper import *
from .triangle import *
from .circle import *
from .shape import *
from .mouse import *
from .arc import *
from .bezier_curve import *
from .ellipse import *
from .heart import *
from .line import *
from .polygon import *
from .star import *
from .control import *

# python -m dooGL.core._2d.main
if __name__ == "__main__":
    init_window(800, 600)  # Initialize window with size 800x600
    running = True
   # points=[(0,0),(0,100),(100,100),(100,0),(0,0)]
   # points2 = [(100, 100), (150, 100), (150, 150), (100, 150)]
    #pointc=(400,300)
    while running:
        running = magic(mouse_position=True)
        
        
       # background()
        
        scale(spacing=50)
        
        
       
       # point((300,400),(1,1,0),90) 
       # triangle(center=(600,100),size=100,color=(0,1,1))
       # square(center=(100,100),size=100,color=(1,1,0))
       # circle(section="bottom_right",center=(400,300),radius=200,fill=False)
      #  text((500,300),"dogl mf",background_color=(0,0,0))
      #  shape([(0,0),(0,100),(100,100),(100,0),(0,0)],rotation=360)
      #  polygon(center=(200, 300), sides=8, radius=200, color=(0, 1, 0),rotation=40,fill=False)
      #  ellipse(center=(400, 300), radius_x=100, radius_y=200, color=(1, 0, 0))
      #  arc(center=(600, 400), radius=100, start_angle=0, end_angle=360, color=(0.5, 0.5, 1.0))   
      #  bezier_curve(control_points=[(100, 100), (200, 300), (400, 300)], color=(1, 0, 0))
      #  line(start_point=(100, 100), end_point=(700, 100), color=(0.0, 0.0, 1.0), thickness=3.0, rotation=45, dashed=True)
      #  heart(center=(400, 300), size=30, color=(1.0, 0.0, 0.0), rotation=0,fill= False)
      #  star(center=(400, 300), radius=100, points=360, color=(1.0, 1.0, 0.0), rotation=70,fill=False)
             
      #  move()
      #  points=move(points, speed=1)
       # points = move(points, speed=1, up='1', down='2', left='3', right='4')
       # shape(points)

        #points2 = move(points2, speed=1)
        #shape(points2)

       # pointc = move(pointc)
       # heart(center=pointc, size=10, color=(1.0, 0.0, 0.0), rotation=0,fill= False)

        end()  # Swap buffers to display everything

  