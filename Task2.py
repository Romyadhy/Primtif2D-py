from PIL import Image, ImageDraw
import math

# Canvas
width, height = 500, 500
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Function to draw a point
def draw_point(x, y, color="black"):
    if 0 <= x < width and 0 <= y < height:
        draw.rectangle([x, y, x+1, y+1], fill=color)

# DDA Line Drawing Algorithm
def draw_line_dda(x1, y1, x2, y2, color="black"):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    
    x_increment = dx / steps
    y_increment = dy / steps
    
    x = x1
    y = y1
    
    for _ in range(steps):
        draw_point(round(x), round(y), color)
        x += x_increment
        y += y_increment

# BruteForce Line Drawing Algorithm
def draw_line_bruteforce(x1, y1, x2, y2, color="black"):
    if x1 == x2:  # Vertical line
        for y in range(min(y1, y2), max(y1, y2) + 1):
            draw_point(x1, y, color)
    else:
        m = (y2 - y1) / (x2 - x1)
        c = y1 - m * x1
        if abs(m) <= 1:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                y = round(m * x + c)
                draw_point(x, y, color)
        else:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                x = round((y - c) / m)
                draw_point(x, y, color)

# Bresenham Line Drawing Algorithm
def draw_line_bresenham(x1, y1, x2, y2, color="black"):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        draw_point(x1, y1, color)
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

# Bresenham Circle Drawing Algorithm
def draw_circle_bresenham(xc, yc, r, color="black"):
    x = 0
    y = r
    d = 3 - 2 * r
    plot_circle_points(xc, yc, x, y, color)
    while y >= x:
        x += 1
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        plot_circle_points(xc, yc, x, y, color)

# Helper function to plot all octant points for a circle
def plot_circle_points(xc, yc, x, y, color):
    draw_point(xc + x, yc + y, color)
    draw_point(xc - x, yc + y, color)
    draw_point(xc + x, yc - y, color)
    draw_point(xc - x, yc - y, color)
    draw_point(xc + y, yc + x, color)
    draw_point(xc - y, yc + x, color)
    draw_point(xc + y, yc - x, color)
    draw_point(xc - y, yc - x, color)

# Draw lines and circle
draw_line_dda(10, 10, 200, 200, color="red")
draw_line_bruteforce(50, 10, 50, 200, color="blue")
draw_line_bresenham(100, 100, 300, 300, color="green")

# Draw circle with center (250, 250) and radius 100
draw_circle_bresenham(250, 250, 100, color="purple")

# Show and save the image
image.show()
image.save("lines_and_circle.png")
