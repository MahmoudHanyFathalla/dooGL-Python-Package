from dooGL import *
'''
if __name__ == "__main__":
    init_window(800, 600)  # Initialize window with size 800x600
    running = True
   # points=[(0,0),(0,100),(100,100),(100,0),(0,0)]
   # points2 = [(100, 100), (150, 100), (150, 150), (100, 150)]
    #pointc=(400,300)
    while running:
        running = magic(mouse_position=True)
        
        
       # background()
        
        scale(spacing=50,show_numbers=True)
        
        
       
        point((300,400),(1,1,0),5) 
        triangle(center=(600,100),size=100,color=(0,1,1))
        square(center=(100,100),size=100,color=(1,1,0))
        circle(center=(400,300),radius=200,fill=False)
        text((500,300),"dogl mf",background_color=(0,0,0))
      #  shape([(0,0),(0,100),(100,100),(100,0),(0,0)],rotation=360)
        polygon(center=(200, 300), sides=8, radius=200, color=(0, 1, 0),rotation=40,fill=False)
        ellipse(center=(400, 300), radius_x=100, radius_y=200, color=(1, 0, 0))
        arc(center=(600, 400), radius=100, start_angle=0, end_angle=360, color=(0.5, 0.5, 1.0))   
      #  bezier_curve(control_points=[(100, 100), (200, 300), (400, 300)], color=(1, 0, 0))
        line(start_point=(100, 100), end_point=(700, 100), color=(0.0, 0.0, 1.0), thickness=3.0, rotation=45, dashed=True)
        heart(center=(400, 300), size=10, color=(1.0, 0.0, 0.0), rotation=0,fill= False)
        star(center=(400, 300), radius=100, points=6, color=(1.0, 1.0, 0.0), rotation=70,fill=False)
             
       # move()
      #  points=move(points, speed=1)
      # points = move(points, speed=1, up='1', down='2', left='3', right='4')
       # shape(points)

        #points2 = move(points2, speed=1)
        #shape(points2)

       # pointc = move(pointc)
       # heart(center=pointc, size=10, color=(1.0, 0.0, 0.0), rotation=0,fill= False)

        end()  # Swap buffers to display everything
'''



#######3d######

from dooGL import *
d3_init_window(width=800, height=600, depth=2000.0, text="DoGL")

running = True
while running:
    
    
    running = magic(mouse_position=True)  # Event handling and rendering

    d3_camera(        
    move=True,  # Allow camera movement
    print_position=True,  # Print camera position and rotation values
    )

    
    d3_scale(depth=1000)
    d3_cube(center=(0.0, 0.0, 0.0), size=100.0, rotation=(0, 0, 0), color=(1.0, 1.0, 0.0))
    d3_plane(center=(300.0, 300.0, 300.0),width=400.0, height=400.0, rotation=(0, 0, 0), color=(1.0, 1.0, 0.0))
    d3_plane(center=(300.0, 100.0, 500.0),width=400.0, height=400.0, rotation=(90, 0, 0), color=(1.0, 0.0, 0.0))
    d3_plane(center=(500.0, 300.0, 500.0),width=400.0, height=400.0, rotation=(0, 90, 0), color=(0, 0.0, 1.0))
    d3_plane(center=(300.0, 300.0, 700.0),width=400.0, height=400.0, rotation=(0, 0, 0), color=(1.0, 0.0, 1.0))
    d3_plane(center=(300.0, 500.0, 500.0),width=400.0, height=400.0, rotation=(90, 0, 0), color=(0, 1.0, 1))
    d3_pyramid(center=(80, 80, 80),base_width=100.0, height=200.0, rotation=(0, 0, 0), color=(0, 1, 1))
    d3_prism(center=(0.0, 0, 0), base_width=300, height=200, depth=100, rotation=(0, 0, 0), color=(0.5, 0.0, 1.0))
    d3_sphere(center=(0.0, 0.0, 0), radius=100, rotation=(0, 0, 0), color=(0.0, 0.5, 1.0))
    d3_torus(center=(0.0, 0.0, 0), radius=200, tube_radius=50, rotation=(0, 0, 0), color=(1.0, 0.5, 0.0))
    d3_cylinder(center=(100.0, 100.0, 60), radius=100, height=1000, rotation=(90, 0, 0), color=(0.5, 0.7, 1.0))
    d3_diamond(center=(0.0, 0.0, 0), base_width=200, height=900, rotation=(0, 0, 0), color=(1.0, 0.5, 0.0))
    #point = d3_move(point, speed=1, move_forward='w', move_backward='s', 
    #            move_left='a', move_right='d', move_down='q', move_up='e')
    #d3_cube(center=point, size=100.0, rotation=(0, 0, 0), color=(1.0, 1.0, 0.0))
    






    
    end()

