**2D Primitives with OpenGL in Python**

_Overview_

Welcome to the 2D Primitives with OpenGL project! This project demonstrates how to create and render basic 2D shapes—points, lines, squares, triangles, and circles—using Python's OpenGL and Pygame libraries. Whether you're a beginner in computer graphics or just exploring OpenGL for fun, this project provides a solid foundation for understanding how 2D shapes are constructed and displayed on screen.

**Prerequisites**
  - Python 3.11 or above (this library do not has specific version of python)
  - Pygame: pip install pygame
  - PyOpenGL: pip install PyOpenGL
  - Mathplolib: pip install Matplolib


_Note: If you encounter issues with PyOpenGL_accelerate, you can proceed without it, as it's an optional optimization library._


**Functions:**
  - draw_point(): Draws multiple points at different locations on the screen.
  - draw_line(): Draws a straight line from one point to another.
  - draw_square(): Draws a square by specifying the coordinates of its vertices in a counter-clockwise manner.
  - draw_triangle(): Draws an equilateral triangle by specifying the coordinates of its vertices.
  - draw_circle(radius, num_segments): Draws a circle using a fan of triangles. The circle is approximated by breaking it down into num_segments triangles.
