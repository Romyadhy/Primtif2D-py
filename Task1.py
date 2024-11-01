from PIL import Image, ImageDraw

# Canvas
width, height = 500, 500
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Function to draw a point
def draw_point(x, y, color="black"):
    draw.rectangle([x, y, x+1, y+1], fill=color)

# Function to draw a line using DDA algorithm
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

# Function to draw a line using Bresenham's algorithm
def draw_line_bresenham(x1, y1, x2, y2, color="black"):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        draw_point(x1, y1, color)
        if x1 == x2 and y1 == y2:  # Stop if we reached the end point
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

# Draw points and lines using DDA and Bresenham's algorithms
draw_point(30, 50, color="black")

draw_point(50, 50, color="blue")
draw_point(51, 50, color="blue")
draw_point(52, 50, color="blue")
draw_point(53, 50, color="blue")
draw_point(54, 50, color="blue")
draw_point(55, 50, color="blue")
draw_point(56, 50, color="blue")
draw_point(57, 50, color="blue")
draw_point(58, 50, color="blue")
draw_point(59, 50, color="blue")
draw_point(60, 50, color="blue")
draw_point(61, 50, color="blue")
draw_point(62, 50, color="blue")


# Draw lines using DDA and Bresenham's algorithms
draw_line_dda(100, 100, 400, 300, color="red")      
draw_line_bresenham(50, 200, 200, 50, color="green") 

# Show and save the image
image.show()      
image.save("titik_dan_garis.png") 
