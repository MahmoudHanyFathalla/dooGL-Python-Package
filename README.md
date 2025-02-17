# DooGL - 2D & 3D Graphics Library

## Overview

**DooGL** is a Python-based graphics library designed for rendering **2D and 3D objects** using OpenGL and Pygame. It provides an easy-to-use API for drawing and manipulating geometric shapes, integrating textures, handling interactive movements, and setting up custom camera controls. Ideal for **game development, simulations, and data visualization**, DooGL simplifies graphics programming while offering extensive customization options.

---
## Features

### 2D Functions
DooGL includes a wide range of 2D drawing functions for rendering shapes, text, and backgrounds with rotation, colors, and texture support.

#### **Basic Shapes**
- **Arc**: Draws an arc with customizable center, radius, angles, and rotation.
- **Bezier Curve**: Renders a smooth curve using control points.
- **Circle**: Creates a filled or outlined circle with optional texture.
- **Ellipse**: Draws an ellipse with adjustable radii, rotation, and optional texture.
- **Heart**: Generates a heart shape with customizable size and fill options.
- **Line**: Draws a straight or dashed line between two points.
- **Polygon**: Creates multi-sided polygons with optional texture.
- **Square**: Renders a square with customizable size, rotation, and texture.
- **Star**: Generates a star with a specified number of points.
- **Triangle**: Draws an equilateral triangle with rotation and texture options.
- **Shape**: For making and creating your own shapes.

#### **Text and Background**
- **Text**: Displays text with customizable font, color, background, size, and rotation.
- **Background**: Sets an image as the background for the rendering window.

#### **Interactive Features**
- **Move**: Enables object movement using keyboard controls with boundary checking.
- **Magic**: Captures mouse clicks and prints their positions for interaction handling.
- **Scale**: Draws a coordinate grid with adjustable spacing and labeled axes.

---

### 3D Functions
DooGL offers advanced 3D rendering capabilities, including shape drawing, camera control, and object transformations.

#### **3D Camera & Environment**
- **d3_camera**: Implements a 3D camera with movement, rotation, and boundary limits.
- **d3_background**: Sets a background image for the 3D scene.
- **d3_scale**: Draws a 3D coordinate system with X, Y, and Z axes.
- **d3_init_window**: Initializes an OpenGL-powered Pygame window with customizable depth and title.

#### **3D Shapes**
- **d3_cube**: Creates a 3D cube with size, color, and rotation controls.
- **d3_cylinder**: Generates a cylinder with adjustable height and radius.
- **d3_diamond**: Draws a diamond-shaped 3D object.
- **d3_plane**: Renders a flat 3D plane with color and rotation.
- **d3_prism**: Creates a triangular prism with depth and color options.
- **d3_pyramid**: Draws a pyramid with customizable base width and height.
- **d3_sphere**: Generates a sphere with adjustable radius and rotation.
- **d3_torus**: Creates a torus with customizable ring and tube radius.

#### **3D Interactivity**
- **d3_move**: Enables keyboard-controlled movement of points in 3D space.

---

## Getting Started
To use DooGL, ensure you have **Python** installed. Then, integrate DooGL into your project using:

```
pip install dooGL

```
---

## Applications
- **Game Development**: Easily create and manipulate 2D/3D objects for game environments.
- **Simulations**: Visualize physics-based models and interactive scenarios.
- **Data Visualization**: Render 3D graphs and charts with ease.

---

## Conclusion

DooGL is a powerful and flexible Python library designed for 2D and 3D graphics rendering using OpenGL and Pygame. It provides an extensive set of functions for creating and manipulating geometric shapes, including arcs, curves, polygons, and complex 3D objects like cubes, spheres, and toruses. With built-in support for transformations, textures, and interactive camera controls, DooGL simplifies graphical programming, making it ideal for game development, simulations, and visualizations. Its intuitive API allows developers to efficiently render high-quality graphics while maintaining full control over colors, rotations, and animations.
