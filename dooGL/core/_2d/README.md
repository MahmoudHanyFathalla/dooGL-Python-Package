# 2D Functions

#### Arc
Draw an arc with customizable center, radius, angles, color, and rotation.

```python
arc(center=(200, 150), radius=50, start_angle=0, end_angle=180, color=(1.0, 0.0, 0.0), line_width=3.0, rotation=45)
```

- **center**: The coordinates of the arc's center `(x, y)`.
- **radius**: The arc's radius.
- **start_angle**: The starting angle of the arc (in degrees).
- **end_angle**: The ending angle of the arc (in degrees).
- **color**: RGB color tuple (default is white).
- **line_width**: The thickness of the arc's line.
- **rotation**: The angle by which to rotate the arc.

#### Bezier Curve
Draw a smooth Bezier curve with control points.

```python
bezier_curve(control_points=[(100, 100), (150, 200), (200, 100)], steps=50, color=(0.0, 1.0, 0.0), rotation=30)
```

- **control_points**: A list of control points `[(x1, y1), (x2, y2), ...]`.
- **steps**: The number of steps to approximate the curve (more steps = smoother curve).
- **color**: RGB color tuple (default is white).
- **rotation**: The rotation angle for the entire curve around the first control point.

#### Circle
Draw a circle with optional filling, texture, and rotation.

```python
circle(center=(250, 250), radius=80, color=(0.0, 1.0, 0.0), fill=False, image="circle_texture.png", section="top_right", rotation=45)
```

- **center**: The `(x, y)` coordinates of the circle's center.
- **radius**: The radius of the circle.
- **color**: RGB color tuple (ignored if an image is provided).
- **fill**: Whether the circle should be filled (True) or just an outline (False).
- **image**: The file path of an image to texture the circle.
- **section**: Specifies which part of the circle to draw (e.g., "top_left", "bottom_right").
- **rotation**: The rotation angle (in degrees) to apply to the drawn section of the circle.

#### Ellipse
Draw an ellipse with customizable radii, color, and rotation.

```python
ellipse(center=(300, 300), radius_x=150, radius_y=100, color=(0.0, 1.0, 0.0), fill=True, rotation=45, image="ellipse_texture.png")
```

- **center**: The `(x, y)` coordinates of the ellipse's center.
- **radius_x**: The radius along the x-axis.
- **radius_y**: The radius along the y-axis.
- **color**: RGB color tuple (default is white).
- **fill**: Whether the ellipse should be filled (True) or just an outline (False).
- **rotation**: The angle (in degrees) to rotate the ellipse.
- **image**: The file path to an image that will be used as a texture on the ellipse.

#### Heart
Draw a heart shape with customizable size, color, and rotation.

```python
heart(center=(400, 300), size=10, color=(1.0, 0.0, 0.0), fill=True, rotation=45)
```

- **center**: The `(x, y)` coordinates of the heart's center.
- **size**: The size of the heart, affecting both width and height.
- **color**: RGB color tuple (default is red).
- **fill**: Whether the heart should be filled (True) or just an outline (False).
- **rotation**: The angle (in degrees) to rotate the heart.

#### Line
Draw a line between two points with customizable color, thickness, and rotation.

```python
line(start_point=(100, 100), end_point=(200, 200), color=(1.0, 0, 0), thickness=2, rotation=45, dashed=True)
```

- **start_point**: The starting point of the line as a tuple `(x, y)`.
- **end_point**: The ending point of the line as a tuple `(x, y)`.
- **color**: RGB tuple for the line color (default is white).
- **thickness**: Line thickness (default is 1.0).
- **rotation**: Angle (in degrees) to rotate the line around the start point (default is 0).
- **dashed**: Whether the line should be dashed (True) or solid (False).

#### Polygon
Draw a polygon with customizable sides, radius, color, and rotation.

```python
polygon(center=(400, 300), sides=6, radius=200, color=(0, 1.0, 0), fill=True, rotation=45, image="texture.png")
```

- **center**: The `(x, y)` coordinates of the polygon's center.
- **sides**: The number of sides of the polygon (e.g., 3 for triangle, 6 for hexagon).
- **radius**: The distance from the center to a vertex of the polygon.
- **color**: RGB color tuple (default is white).
- **fill**: Whether the polygon should be filled (True) or outlined (False).
- **rotation**: The angle in degrees to rotate the polygon.
- **image**: An optional texture to apply to the polygon.

#### Square
Draw a square with customizable size, color, and rotation.

```python
square(center=(200, 200), size=100, color=(1.0, 0.0, 0.0), fill=True, rotation=45)
```

- **center**: The center point `(x, y)` of the square.
- **size**: The side length of the square.
- **color**: RGB color tuple (default is red).
- **fill**: Whether the square should be filled (True) or just outlined (False).
- **rotation**: The angle in degrees to rotate the square.
- **rotate_around**: Defines the point around which to rotate the square, typically "center" or "origin".
- **image**: The file path to an image to be used as a texture for the square.

#### Star
Draw a star with customizable radius, points, color, and rotation.

```python
star(center=(400, 300), radius=150, points=6, color=(1.0, 0.5, 0.0), fill=False, rotation=45)
```

- **center**: The center point `(x, y)` of the star.
- **radius**: The outer radius of the star.
- **points**: Number of points on the star (default is 5).
- **color**: RGB color tuple (default is yellow).
- **fill**: Whether the star should be filled (True) or outlined (False).
- **rotation**: The rotation angle of the star in degrees.

#### Triangle
Draw a triangle with customizable size, color, and rotation.

```python
triangle(center=(400, 300), size=100, color=(0.0, 1.0, 0.0), fill=True, rotation=30, rotate_around="center")
```

- **center**: The center of the triangle `(x, y)`.
- **size**: The size of the triangle (typically the length of the sides).
- **color**: RGB color tuple (default is red).
- **fill**: Whether the triangle should be filled (True) or just outlined (False).
- **rotation**: The angle in degrees to rotate the triangle.
- **rotate_around**: The pivot point for rotation. Can be "center", "top", "bottom_left", or "bottom_right".
- **image**: The path to an image to apply as a texture to the triangle.


#### Text
Draw text on the screen with customizable font, color, and background.

```python
text(position=(100, 100), text="Hello", font=None, text_color=(1, 1, 0), background_color=(0, 0.25, 0), size=(100, 50), rotation=0)
```

- **position**: The `(x, y)` coordinates to place the text.
- **text**: The string of text to display.
- **font**: The font object (if None, defaults to Arial 24).
- **text_color**: Color of the text in RGB format (default yellow).
- **background_color**: Background color for the text in RGB (default dark green).
- **size**: Width and height of the text area to scale.
- **rotation**: The angle to rotate the text in degrees.

#### Background
Set a background image for the window.

```python
background(image_path="background_image.png")
```

- **image_path**: The file path to the image you want to use as the background.

#### Move
Move points on the screen with keyboard controls.

```python
move(points=[(100, 100)], speed=2, up=pygame.K_w, down=pygame.K_s, left=pygame.K_a, right=pygame.K_d, boundaries=True, half_raduis=10, max_x=800, max_y=600)
```

- **points**: A list of points `[(x1, y1), (x2, y2)]` to move.
- **speed**: The movement speed of the points.
- **up, down, left, right**: The keys used for movement (defaults to arrow keys).
- **boundaries**: Whether to check screen boundaries to prevent moving off-screen.
- **half_raduis**: Half the radius of the object for boundary checking.
- **max_y, min_y, max_x, min_x**: Custom boundaries for movement on each axis.

#### Magic
Capture mouse clicks and print their positions.

```python
running = magic(mouse_position=True)
```
### Parameters:
- **mouse_position**: Boolean flag to determine if the mouse position should be printed when clicked.

---

To use the `scale` function in one line of Python, you can call it like this:

```python
scale(spacing=50, show_numbers=True, text_color=(1, 0, 0), font=None)
```

### Parameters:
- **spacing**: The distance between grid lines (default is 50).
- **show_numbers**: Boolean flag to indicate whether to display numbers beside the center lines (default is True).
- **text_color**: The color of the text in (1.0, 0.0, 0.0) format (default is red).
- **font**: The Pygame font object to use for rendering the text (default is None).

---
