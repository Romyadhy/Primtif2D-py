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

draw_line_bresenham(235, 258, 310, 99, color="black")
draw_line_bresenham(312, 102, 352, 246, color="black")
draw_line_bresenham(240, 260, 352, 250, color="black")
draw_line_bresenham(314, 103, 382, 228, color="black")
draw_line_bresenham(355, 247, 380, 228, color="black")
draw_line_bresenham(238, 256, 307, 225, color="black")
draw_line_bresenham(238, 256, 307, 225, color="black")
draw_line_bresenham(312, 108, 307, 227, color="black")
draw_line_bresenham(312, 226, 377, 224, color="black")


draw_line_bresenham(0, 226, 377, 224, color="black")
draw_line_bresenham(312, 226, 377, 224, color="black")
draw_line_bresenham(312, 226, 377, 224, color="black")


# draw_line_bresenham(668, 104, 235, 258, color="black")








# Draw lines using DDA and Bresenham's algorithms
# draw_line_dda(100, 100, 400, 300, color="red")      
# draw_line_bresenham(-10, 100, 100, -10, color="green") 
# RECT INSIDE
# draw_line_bresenham(80, 80, 220, 80, color="green") #atas
# draw_line_bresenham(80, 150, 80, 80, color="green") #kiri
# draw_line_bresenham(220, 150, 220, 80, color="green") #kanan
# draw_line_bresenham(80, 150, 220, 150, color="green") #bawah

# #RECT OUTSIDE
# draw_line_bresenham(50, 50, 250, 50, color="green") #atas
# draw_line_bresenham(50, 50, 50, 300, color="green") #kiri
# draw_line_bresenham(250, 50, 250, 300, color="green") #kanan
# # draw_line_bresenham(50, 300, 250, 300, color="green") #kanan
# # RECT OUTSIDE (Garis Bawah Bergelombang)
# draw_line_bresenham(50, 300, 55, 295, color="green")
# draw_line_bresenham(55, 295, 60, 300, color="green")
# draw_line_bresenham(60, 300, 65, 295, color="green")
# draw_line_bresenham(65, 295, 70, 300, color="green")
# draw_line_bresenham(70, 300, 75, 295, color="green")
# draw_line_bresenham(75, 295, 80, 300, color="green")
# draw_line_bresenham(80, 300, 85, 295, color="green")
# draw_line_bresenham(85, 295, 90, 300, color="green")
# draw_line_bresenham(90, 300, 95, 295, color="green")
# draw_line_bresenham(95, 295, 100, 300, color="green")
# draw_line_bresenham(100, 300, 105, 295, color="green")
# draw_line_bresenham(105, 295, 110, 300, color="green")
# draw_line_bresenham(110, 300, 115, 295, color="green")
# draw_line_bresenham(115, 295, 120, 300, color="green")
# draw_line_bresenham(120, 300, 125, 295, color="green")
# draw_line_bresenham(125, 295, 130, 300, color="green")
# draw_line_bresenham(130, 300, 135, 295, color="green")
# draw_line_bresenham(135, 295, 140, 300, color="green")
# draw_line_bresenham(140, 300, 145, 295, color="green")
# draw_line_bresenham(145, 295, 150, 300, color="green")
# draw_line_bresenham(150, 300, 155, 295, color="green")
# draw_line_bresenham(155, 295, 160, 300, color="green")
# draw_line_bresenham(160, 300, 165, 295, color="green")
# draw_line_bresenham(165, 295, 170, 300, color="green")
# draw_line_bresenham(170, 300, 175, 295, color="green")
# draw_line_bresenham(175, 295, 180, 300, color="green")
# draw_line_bresenham(180, 300, 185, 295, color="green")
# draw_line_bresenham(185, 295, 190, 300, color="green")
# draw_line_bresenham(190, 300, 195, 295, color="green")
# draw_line_bresenham(195, 295, 200, 300, color="green")
# draw_line_bresenham(200, 300, 205, 295, color="green")
# draw_line_bresenham(205, 295, 210, 300, color="green")
# draw_line_bresenham(210, 300, 215, 295, color="green")
# draw_line_bresenham(215, 295, 220, 300, color="green")
# draw_line_bresenham(220, 300, 225, 295, color="green")
# draw_line_bresenham(225, 295, 230, 300, color="green")
# draw_line_bresenham(230, 300, 235, 295, color="green")
# draw_line_bresenham(235, 295, 240, 300, color="green")
# draw_line_bresenham(240, 300, 245, 295, color="green")
# draw_line_bresenham(245, 295, 250, 300, color="green")





# draw_line_bresenham(150, 300, 200, 300, color="green")  # Base
# draw_line_bresenham(150, 300, 130, 250, color="green")  # Left side
# draw_line_bresenham(200, 300, 230, 250, color="green")  # Right side
# draw_line_bresenham(130, 250, 230, 250, color="green")  # Top
# # Show and save the image
image.show()      
image.save("titik_dan_garis.png") 






# Buat code untuk menampiakn garis dengan 3 algoritma DDA, BruteForcem Bresenham, 
# Dalam programnya bisa di buat satu satu atau dibuat jadikan 1 berisi lingkaran di akhir