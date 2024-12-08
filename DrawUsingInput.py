import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageTk

# Generate Canvas
width, height = 900, 400
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Function to draw point
def draw_point(x, y, color="black"):
    draw.rectangle([x, y, x + 1, y + 1], fill=color)

# Algorithm DDA
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
    update_image()

# Algorithm Brute Force
def draw_line_brute_force(x1, y1, x2, y2, color="blue"):
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0:  # Vertical line
        for y in range(y1, y2 + 1):
            draw_point(x1, y, color)
    else:
        m = dy / dx
        for x in range(x1, x2 + 1):
            y = y1 + round(m * (x - x1))
            draw_point(x, y, color)
    update_image()

# Algorithm Bresenham
def draw_line_bresenham(x1, y1, x2, y2, color="green"):
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
    update_image()

# Draw using click
start_point = None
def on_canvas_click(event):
    global start_point
    if start_point is None:
        # First click: record the starting point
        start_point = (event.x, event.y)
    else:
        # Second click: draw the line and reset the start point
        end_point = (event.x, event.y)
        draw_line_dda(start_point[0], start_point[1], end_point[0], end_point[1])
        start_point = None


# Algorithm Circle Bresenham
def draw_circle_bresenham(xc, yc, r, color="purple"):
    x = 0
    y = r
    d = 3 - 2 * r
    while y >= x:
        # Draw eight symmetrical points for each octant
        points = [
            (xc + x, yc + y), (xc - x, yc + y), (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x), (xc + y, yc - x), (xc - y, yc - x)
        ]
        for px, py in points:
            draw_point(px, py, color)
        x += 1
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
    update_image()

# Function to update and display image on canvas
def update_image():
    global photo_image
    photo_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo_image)

# Function to clear canvas
def clear_canvas():
    global image, draw, start_point
    start_point = None
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    update_image()


def validate_line_input():
    if not entry_x1.get() or not entry_y1.get() or not entry_x2.get() or not entry_y2.get():
        messagebox.showerror("Input Error", "Please enter all coordinates for the line.")
        return False
    return True


def validate_circle_input():
    if not entry_xc.get() or not entry_yc.get() or not entry_r.get():
        messagebox.showerror("Input Error", "Please enter center and radius for the circle.")
        return False
    return True

# Functions to handle button clicks
def display_dda():
    if not validate_line_input():
        return
    x1, y1, x2, y2 = int(entry_x1.get()), int(entry_y1.get()), int(entry_x2.get()), int(entry_y2.get())
    draw_line_dda(x1, y1, x2, y2, color="black")

def display_brute_force():
    if not validate_line_input():
        return
    x1, y1, x2, y2 = int(entry_x1.get()), int(entry_y1.get()), int(entry_x2.get()), int(entry_y2.get())
    draw_line_brute_force(x1, y1, x2, y2, color="blue")

def display_bresenham():
    if not validate_line_input():
        return
    x1, y1, x2, y2 = int(entry_x1.get()), int(entry_y1.get()), int(entry_x2.get()), int(entry_y2.get())
    draw_line_bresenham(x1, y1, x2, y2, color="green")

def display_circle():
    if not validate_circle_input():
        return
    xc, yc, r = int(entry_xc.get()), int(entry_yc.get()), int(entry_r.get())
    draw_circle_bresenham(xc, yc, r, color="purple")

# Setup GUI
root = tk.Tk()
root.title("Line and Circle Drawing Algorithms")



# Canvas widget for displaying image
canvas = tk.Canvas(root, width=width, height=height)
canvas.grid(row=0, column=0, columnspan=6)

# Input fields for line coordinates
tk.Label(root, text="x1:").grid(row=1, column=0)
entry_x1 = tk.Entry(root, width=5)
entry_x1.grid(row=1, column=1)

tk.Label(root, text="y1:").grid(row=1, column=2)
entry_y1 = tk.Entry(root, width=5)
entry_y1.grid(row=1, column=3)

tk.Label(root, text="x2:").grid(row=1, column=4)
entry_x2 = tk.Entry(root, width=5)
entry_x2.grid(row=1, column=5)

tk.Label(root, text="y2:").grid(row=1, column=6)
entry_y2 = tk.Entry(root, width=5)
entry_y2.grid(row=1, column=7)

# Input fields for circle center and radius
tk.Label(root, text="xc:").grid(row=2, column=0)
entry_xc = tk.Entry(root, width=5)
entry_xc.grid(row=2, column=1)

tk.Label(root, text="yc:").grid(row=2, column=2)
entry_yc = tk.Entry(root, width=5)
entry_yc.grid(row=2, column=3)

tk.Label(root, text="r:").grid(row=2, column=4)
entry_r = tk.Entry(root, width=5)
entry_r.grid(row=2, column=5)

# Buttons for each algorithm
button_dda = tk.Button(root, text="DDA Line", command=display_dda)
button_dda.grid(row=4, column=0, columnspan=2, padx=3, pady=5)

button_brute = tk.Button(root, text="Brute Force Line", command=display_brute_force)
button_brute.grid(row=4, column=1, columnspan=2, padx=3, pady=10)

button_bresenham = tk.Button(root, text="Bresenham Line", command=display_bresenham)
button_bresenham.grid(row=4, column=2, columnspan=2, padx=3, pady=10)

button_circle = tk.Button(root, text="Bresenham Circle", command=display_circle)
button_circle.grid(row=4, column=3, columnspan=2, padx=3, pady=10)

# Button to clear canvas
button_clear = tk.Button(root, text="Clear Canvas", command=clear_canvas)
button_clear.grid(row=5, column=0, columnspan=6, padx=10, pady=20)

# Bind mouse click to canvas
canvas.bind("<Button-1>", on_canvas_click)

# Initialize and show
update_image()
root.mainloop()
