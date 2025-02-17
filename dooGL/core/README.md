Here's the updated README with all the mentioned 3D functions included:

---

# dooGL - A Python Package for 2D and 3D Graphics

`dooGL` is a Python package designed to simplify and enhance the creation of 2D and 3D graphics. Whether you're working on graphical user interfaces, creating visualizations, or developing games and simulations, `dooGL` provides a wide range of functions to draw various shapes, apply transformations, and handle user interactions. It supports both 2D and 3D graphics with customizable parameters like color, rotation, and texture.

## Table of Contents

- [Installation](#installation)
- [2D Functions](#2d-functions)
  - [Arc](#arc)
  - [Bezier Curve](#bezier-curve)
  - [Circle](#circle)
  - [Ellipse](#ellipse)
  - [Heart](#heart)
  - [Line](#line)
  - [Polygon](#polygon)
  - [Square](#square)
  - [Star](#star)
  - [Triangle](#triangle)
  - [Text](#text)
  - [Background](#background)
  - [Interactive Functions](#interactive-functions)
    - [Move](#move)
    - [Magic](#magic)
  - [Scale](#scale)
- [3D Functions](#3d-functions)
  - [3D Camera & Environment](#3d-camera--environment)
    - [d3_camera](#d3_camera)
    - [d3_background](#d3_background)
    - [d3_scale](#d3_scale)
    - [d3_init_window](#d3_init_window)
  - [3D Shapes](#3d-shapes)
    - [d3_cube](#d3_cube)
    - [d3_cylinder](#d3_cylinder)
    - [d3_diamond](#d3_diamond)
    - [d3_plane](#d3_plane)
    - [d3_prism](#d3_prism)
    - [d3_pyramid](#d3_pyramid)
    - [d3_sphere](#d3_sphere)
    - [d3_torus](#d3_torus)
  - [3D Interactivity](#3d-interactivity)
    - [d3_move](#d3_move)
- [Usage Examples](#usage-examples)
- [License](#license)

## Installation

To install the `dooGL` package, use the following command:

```bash
pip install dooGL
```

Ensure you have all dependencies installed before using the package. `dooGL` works with Python 3.6+.

## 2D Functions

### Arc

Draw an arc with customizable parameters such as center, radius, start and end angles, and rotation.

```python
arc(center=(200, 150), radius=50, start_angle=0, end_angle=180, color=(1.0, 0.0, 0.0), line_width=3.0, rotation=45)
```

### Bezier Curve

Draw a smooth Bezier curve using control points.

```python
bezier_curve(control_points=[(100, 100), (150, 200), (200, 100)], steps=50, color=(0.0, 1.0, 0.0), rotation=30)
```

### Circle

Draw a circle with optional filling, texture, and rotation.

```python
circle(center=(250, 250), radius=80, color=(0.0, 1.0, 0.0), fill=False, image="circle_texture.png", section="top_right", rotation=45)
```

### Ellipse

Draw an ellipse with customizable radii, color, and rotation.

```python
ellipse(center=(300, 300), radius_x=150, radius_y=100, color=(0.0, 1.0, 0.0), fill=True, rotation=45, image="ellipse_texture.png")
```

### Heart

Draw a heart shape with customizable size, color, and rotation.

```python
heart(center=(400, 300), size=10, color=(1.0, 0.0, 0.0), fill=True, rotation=45)
```

### Line

Draw a line between two points with customizable color, thickness, and rotation.

```python
line(start_point=(100, 100), end_point=(200, 200), color=(1.0, 0, 0), thickness=2, rotation=45, dashed=True)
```

### Polygon

Draw a polygon with customizable sides, radius, color, and rotation.

```python
polygon(center=(400, 300), sides=6, radius=200, color=(0, 1.0, 0), fill=True, rotation=45, image="texture.png")
```

### Square

Draw a square with customizable size, color, and rotation.

```python
square(center=(200, 200), size=100, color=(1.0, 0.0, 0.0), fill=True, rotation=45)
```

### Star

Draw a star with customizable radius, points, color, and rotation.

```python
star(center=(400, 300), radius=150, points=6, color=(1.0, 0.5, 0.0), fill=False, rotation=45)
```

### Triangle

Draw a triangle with customizable size, color, and rotation.

```python
triangle(center=(400, 300), size=100, color=(0.0, 1.0, 0.0), fill=True, rotation=30, rotate_around="center")
```

### Text

Draw text on the screen with customizable font, color, and background.

```python
text(position=(100, 100), text="Hello", font=None, text_color=(1, 1, 0), background_color=(0, 0.25, 0), size=(100, 50), rotation=0)
```

### Background

Set a background image for the window.

```python
background(image_path="background_image.png")
```

## Interactive Functions

### Move

Move points on the screen with keyboard controls.

```python
move(points=[(100, 100)], speed=2, up=pygame.K_w, down=pygame.K_s, left=pygame.K_a, right=pygame.K_d, boundaries=True, half_raduis=10, max_x=800, max_y=600)
```

### Magic

Capture mouse clicks and print their positions.

```python
running = magic(mouse_position=True)
```

## Scale

Scale the grid and optionally show numbers for the center lines.

```python
scale(spacing=50, show_numbers=True, text_color=(1, 0, 0), font=None)
```

## 3D Functions

### 3D Camera & Environment

#### **d3_camera**

Control the movement and rotation of a 3D camera.

```python
d3_camera(camera_pos=[-495, 495, 495], speed=0.1, rotation=[25, 45, 0], rotation_speed=0.1, move=True, print_position=True, 
          forward_z='w', backward_z='s', left_x='a', right_x='d', up_y='q', down_y='e', 
          rotate_up_x='up', rotate_down_x='down', rotate_left_y='left', rotate_right_y='right', 
          roll_left_z='z', roll_right_z='x', boundaries=True, max_y=500, min_y=0, max_x=500, min_x=0, max_z=500, min_z=0)
```

#### **d3_background**

Set a 3D scene background image.

```python
d3_background(image_path="background_image.png")
```

#### **d3_scale**

Draw a 3D coordinate system with X, Y, and Z axes.

```python
d3_scale(spacing=100, axis_color=(0.0, 1.0, 0.0), axis_width=2)
```

#### **d3_init_window**

Initialize an OpenGL-powered Pygame window for 3D rendering.

```python
d3_init_window(width=800, height=600, depth=32, title="3D Window")
```

### 3D Shapes

#### **d3_cube**

Draw a 3D cube with customizable size, rotation, and color.

```python
d3_cube(center=(0.0, 0.0, 0.0), size=1.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0))
```

#### **d3_cylinder**

Draw a 3D cylinder with customizable height, radius, and rotation.

```python
d3_cylinder(center=(0.0, 0.0, 0.0), radius=1.0, height=2.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 1.0))
```

#### **d3_diamond**

Draw a 3D diamond-shaped object.

```python
d3_diamond(center=(0.0, 0.0, 0.0), size=1.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 0.0, 1.0))
```

#### **d3_plane**

Draw a 3D plane with customizable size, color, and rotation.

```python
d3_plane(center=(0.0, 0.0, 0.0), width=2.0, height=2.0, rotation=(0.0, 0.0, 0.0), color=(0.0, 0.0, 1.0))
```

#### **d3_prism**

Create a 3D triangular prism with customizable depth and color.

```python
d3_prism(center=(0.0, 0.0, 0.0), size=1.0, depth=2.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 1.0, 0.0))
```

#### **d3_pyramid**

Draw a 3D pyramid with customizable base width, height, and color.

```python
d3_pyramid(center=(0.0, 0.0, 0.0), base_width=2.0, height=3.0, rotation=(0.0, 0.0, 0.0), color=(0.0, 1.0, 0.0))
```

#### **d3_sphere**

Draw a 3D sphere with customizable radius and rotation.

```python
d3_sphere(center=(0.0, 0.0, 0.0), radius=1.0, rotation=(0.0, 0.0, 0.0), color=(0.0, 0.0, 1.0))
```

#### **d3_torus**

Draw a 3D torus with customizable ring and tube radius.

```python
d3_torus(center=(0.0, 0.0, 0.0), inner_radius=1.0, outer_radius=2.0, rotation=(0.0, 0.0, 0.0), color=(1.0, 0.0, 0.0))
```

### 3D Interactivity

#### **d3_move**

Enable keyboard-controlled movement of points in 3D space.

```python
d3_move(points=[(0.0, 0.0, 0.0)], speed=0.1, forward='w', backward='s', left='a', right='d', up='q', down='e', boundaries=True)
```

## Usage Examples

Here's an example that demonstrates how to use some of the package's features:

```python
import dooGL


```

## License

This package is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Enjoy creating your graphical and 3D projects with `dooGL`!