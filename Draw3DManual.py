from PIL import Image, ImageDraw

# Canvas
width, height = 500, 500
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Function to draw a point
def draw_point(x, y, color="black"):
    draw.rectangle([x, y, x+1, y+1], fill=color)

# 3D DDA Algorithm
def draw_line_dda_3d(x1, y1, z1, x2, y2, z2, color="black"):
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    steps = max(abs(dx), abs(dy), abs(dz))
    
    x_increment = dx / steps
    y_increment = dy / steps
    z_increment = dz / steps
    
    x = x1
    y = y1
    z = z1
    
    for _ in range(steps):
        draw_point(round(x), round(y), color)
        x += x_increment
        y += y_increment
        z += z_increment

# 3D Bresenham's Algorithm
def draw_line_bresenham_3d(x1, y1, z1, x2, y2, z2, color="black"):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    dz = abs(z2 - z1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    sz = 1 if z1 < z2 else -1
    err = dx - dy - dz

    while True:
        draw_point(x1, y1, color)
        if x1 == x2 and y1 == y2 and z1 == z2:  # Stop if we reached the end point
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
        if e2 < dz:
            err += dz
            z1 += sz

# 3D Brute Force Line Algorithm
def draw_line_bruteforce_3d(x1, y1, z1, x2, y2, z2, color="black"):
    steps = max(abs(x2 - x1), abs(y2 - y1), abs(z2 - z1))
    for i in range(steps+1):
        x = x1 + (x2 - x1) * i / steps
        y = y1 + (y2 - y1) * i / steps
        z = z1 + (z2 - z1) * i / steps
        draw_point(round(x), round(y), color)

# Example usage for 3D lines

# 3D DDA
draw_line_dda_3d(50, 50, 50, 200, 200, 200, color="red")

# 3D Bresenham
draw_line_bresenham_3d(100, 100, 100, 300, 200, 300, color="blue")

# 3D Brute Force
draw_line_bruteforce_3d(150, 150, 150, 350, 250, 350, color="green")

# Show and save the image
image.show()
image.save("3d_lines.png")
