# 3D functions


#### To use the `d3_camera` function in one line of Python, you can call it like this:  

```python
d3_camera(camera_pos=[-495,495,495], speed=0.1, rotation=[25, 45, 0], rotation_speed=0.1, move=False, print_position=False,
              forward_z='w', backward_z='s', left_x='a', right_x='d', up_y='q', down_y='e', 
              rotate_up_x='up', rotate_down_x='down', rotate_left_y='left', rotate_right_y='right',
              roll_left_z='z', roll_right_z='x', 
              boundaries=False, max_y=None, min_y=None, max_x=None, min_x=None, max_z=None, min_z=None,
              rotate_x_max=None, rotate_x_min=None, rotate_y_max=None, rotate_y_min=None, rotate_z_max=None, rotate_z_min=None)
```

### Parameters

- **camera_pos**: List `[x, y, z]`. The starting position of the camera in 3D space.
- **speed**: Float. Speed at which the camera moves.
- **rotation**: List `[pitch (X), yaw (Y), roll (Z)]`. Initial camera rotation in degrees.
- **rotation_speed**: Float. Speed at which the camera rotates.
- **move**: Bool. Enables (`True`) or disables (`False`) movement control.
- **print_position**: Bool. If `True`, prints camera position and rotation on update.

#### Movement Controls
- **forward_z** / **backward_z**: Keys to move forward/backward along Z-axis (default: `'w'`, `'s'`).
- **left_x** / **right_x**: Keys to move left/right along X-axis (default: `'a'`, `'d'`).
- **up_y** / **down_y**: Keys to move up/down along Y-axis (default: `'q'`, `'e'`).

#### Rotation Controls
- **rotate_up_x** / **rotate_down_x**: Keys to pitch up/down (default: `'up'`, `'down'`).
- **rotate_left_y** / **rotate_right_y**: Keys to yaw left/right (default: `'left'`, `'right'`).
- **roll_left_z** / **roll_right_z**: Keys to roll camera (default: `'z'`, `'x'`).

#### Boundaries and Limits
- **boundaries**: Bool. If `True`, restricts camera within defined limits.
- **max_x**, **min_x**: Float. Movement limits along X-axis.
- **max_y**, **min_y**: Float. Movement limits along Y-axis.
- **max_z**, **min_z**: Float. Movement limits along Z-axis.
- **rotate_x_max**, **rotate_x_min**: Float. Rotation limits for pitch (X-axis).
- **rotate_y_max**, **rotate_y_min**: Float. Rotation limits for yaw (Y-axis).
- **rotate_z_max**, **rotate_z_min**: Float. Rotation limits for roll (Z-axis). 

---

#### To use the `d3_cube` function in one line of Python, you can call it like this:  

```python
d3_cube(center=(0.0, 0.0, 0.0), size=1.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0))
```

### Parameters:  
- **center**: A tuple `(x, y, z)` representing the center position of the cube.  
- **size**: The size of the cube (applies to width, height, and depth).  
- **rotation**: A tuple `(rot_x, rot_y, rot_z)` specifying the rotation along the X, Y, and Z axes (in degrees).  
- **color**: An RGB tuple `(r, g, b)`, where values range from `0.0` to `1.0`.

---

#### To use the `d3_cylinder` function in one line of Python, you can call it like this:  

```python
d3_cylinder(center=(0.0, 0.0, 0.0), radius=1.0, height=2.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0))
```

### Parameters:  
- **center**: A tuple `(x, y, z)` representing the center position of the cylinder’s base.  
- **radius**: The radius of the cylinder.  
- **height**: The height of the cylinder.  
- **rotation**: A tuple `(rot_x, rot_y, rot_z)` specifying the rotation along the X, Y, and Z axes (in degrees).  
- **color**: An RGB tuple `(r, g, b)`, where values range from `0.0` to `1.0`.


---

#### To use the `d3_diamond` function in one line of Python, you can call it like this:  

```python
d3_diamond(center=(0.0, 0.0, 0.0), base_width=1.0, height=2.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0))
```

### Parameters:  
- **center**: A tuple `(x, y, z)` representing the center position of the diamond.  
- **base_width**: The width of the base of each pyramid.  
- **height**: The height of the diamond (from top point to bottom point).  
- **rotation**: A tuple `(rot_x, rot_y, rot_z)` specifying the rotation along the X, Y, and Z axes (in degrees).  
- **color**: An RGB tuple `(r, g, b)`, where values range from `0.0` to `1.0`.

---

#### To use the `d3_scale` function in one line of Python, you can call it like this:

```python
d3_scale(depth=500.0)
```

### Parameters:
- **depth**: A float value defining the extent of the Z-axis in the 3D space.

### Function Overview:
This function draws the X, Y, and Z axes using OpenGL:
- **X-axis**: Yellow, extending from `-width` to `width`.
- **Y-axis**: Red, extending from `-height` to `height`.
- **Z-axis**: Blue, extending from `-depth` to `depth`.

---

#### To use the `d3_init_window` function in one line of Python, you can call it like this:

```python
d3_init_window(width=800, height=600, depth=1000.0, icon="doGl_logo.png", text="DoGL Window")
```

### Parameters:
- **width**: The width of the window in pixels.
- **height**: The height of the window in pixels.
- **depth**: The depth of the perspective view.
- **icon**: The path to the window icon (default is `"doGl_logo.png"`).
- **text**: The title of the window.

---

#### To use the `d3_background` function in one line of Python, you can call it like this:

```python
d3_background(image_path="background.jpg", img_width=15.0, img_height=10.0, x=0.0, y=0.0, z=-15.0)
```

### Parameters:
- **image_path**: The path to the image file to be used as the background (default is `"doGl_logo.png"`).
- **img_width**: The width of the background image in 3D space (default is `10.0`).
- **img_height**: The height of the background image in 3D space (default is `7.5`).
- **x**: The X-coordinate for the position of the background image (default is `0.0`).
- **y**: The Y-coordinate for the position of the background image (default is `0.0`).
- **z**: The Z-coordinate for the position of the background image (default is `-10.0`).

---

#### To use the `d3_move` function in one line of Python, you can call it like this:

```python
d3_move(point=(0.0, 0.0, 0.0), speed=0.1, move_forward='w', move_backward='s', move_left='a', move_right='d', move_down='q', move_up='e')
```

### Parameters:
- **point**: A tuple of (x, y, z) representing the current position of the point.
- **speed**: A float representing the speed of movement (default is `0.1`).
- **move_forward**: Character representing the key to move forward (decrease z).
- **move_backward**: Character representing the key to move backward (increase z).
- **move_left**: Character representing the key to move left (decrease x).
- **move_right**: Character representing the key to move right (increase x).
- **move_down**: Character representing the key to move down (decrease y).
- **move_up**: Character representing the key to move up (increase y).

---

#### To use the `d3_plane` function in one line of Python, you can call it like this:

```python
d3_plane(center=(0.0, 0.0, 0.0), width=1.0, height=1.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0))
```

### Parameters:
- **center**: A tuple of (x, y, z) for the center position of the plane.
- **width**: A float representing the width of the plane.
- **height**: A float representing the height of the plane.
- **rotation**: A tuple of (rot_x, rot_y, rot_z) for the rotation along the x, y, and z axes in degrees.
- **color**: A tuple of (r, g, b) representing the color of the plane (0.0 - 1.0).

---

#### To use the `d3_prism` function in one line of Python, you can call it like this:

```python
d3_prism(center=(0.0, 0.0, 0.0), base_width=1.0, height=1.0, depth=1.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0))
```

### Parameters:
- **center**: A tuple of (x, y, z) for the center position of the prism.
- **base_width**: A float representing the width of the prism's triangular base.
- **height**: A float representing the height of the prism's triangular base.
- **depth**: A float representing the length of the prism (depth).
- **rotation**: A tuple of (rot_x, rot_y, rot_z) for the rotation along the x, y, and z axes in degrees.
- **color**: A tuple of (r, g, b) representing the color of the prism (0.0 - 1.0).

---

#### To use the `d3_pyramid` function in one line of Python, you can call it like this:

```python
d3_pyramid(center=(0.0, 0.0, 0.0), base_width=1.0, height=1.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0))
```

### Parameters:
- **center**: A tuple of (x, y, z) for the center position of the pyramid's base.
- **base_width**: A float representing the width of the pyramid's base.
- **height**: A float representing the height of the pyramid.
- **rotation**: A tuple of (rot_x, rot_y, rot_z) for the rotation along the x, y, and z axes in degrees.
- **color**: A tuple of (r, g, b) representing the color of the pyramid (0.0 - 1.0).

---

#### To use the `d3_sphere` function in one line of Python, you can call it like this:

```python
d3_sphere(center=(0.0, 0.0, 0.0), radius=1.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0))
```

### Parameters:
- **center**: A tuple of (x, y, z) for the center position of the sphere.
- **radius**: A float representing the radius of the sphere.
- **rotation**: A tuple of (rot_x, rot_y, rot_z) for the rotation along the x, y, and z axes in degrees.
- **color**: A tuple of (r, g, b) representing the color of the sphere (0.0 - 1.0).

---

#### To use the `d3_torus` function in one line of Python, you can call it like this:

```python
d3_torus(center=(0.0, 0.0, 0.0), radius=1.0, tube_radius=0.3, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0))
```

### Parameters:
- **center**: A tuple of (x, y, z) for the center position of the torus.
- **radius**: A float representing the radius of the torus (distance from the center of the torus to the center of the tube).
- **tube_radius**: A float representing the radius of the tube.
- **rotation**: A tuple of (rot_x, rot_y, rot_z) for the rotation along the x, y, and z axes in degrees.
- **color**: A tuple of (r, g, b) representing the color of the torus (0.0 - 1.0).

---
