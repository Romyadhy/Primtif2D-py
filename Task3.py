import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageTk

# Fungsi untuk membuat canvas
width, height = 500, 500
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Function to draw a point
def draw_point(x, y, color="black"):
    draw.rectangle([x, y, x + 1, y + 1], fill=color)

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

# Function to draw a line using Brute Force algorithm
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

# Function to draw a line using Bresenham's algorithm
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

# Function to draw a circle using Bresenham's algorithm
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

# Function to update and display image on canvas
def update_image():
    global photo_image
    photo_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo_image)

# Error checking for line drawing
def validate_line_input():
    if not entry_x1.get() or not entry_y1.get() or not entry_x2.get() or not entry_y2.get():
        messagebox.showerror("Input Error", "Please enter all coordinates for the line.")
        return False
    return True

# Error checking for circle drawing
def validate_circle_input():
    if not entry_xc.get() or not entry_yc.get() or not entry_r.get():
        messagebox.showerror("Input Error", "Please enter center and radius for the circle.")
        return False
    return True

# Functions to handle button clicks
def display_dda():
    if not validate_line_input():
        return
    image.paste("white", [0, 0, width, height])  # Clear canvas
    x1, y1, x2, y2 = int(entry_x1.get()), int(entry_y1.get()), int(entry_x2.get()), int(entry_y2.get())
    draw_line_dda(x1, y1, x2, y2, color="red")
    update_image()

def display_brute_force():
    if not validate_line_input():
        return
    image.paste("white", [0, 0, width, height])  # Clear canvas
    x1, y1, x2, y2 = int(entry_x1.get()), int(entry_y1.get()), int(entry_x2.get()), int(entry_y2.get())
    draw_line_brute_force(x1, y1, x2, y2, color="blue")
    update_image()

def display_bresenham():
    if not validate_line_input():
        return
    image.paste("white", [0, 0, width, height])  # Clear canvas
    x1, y1, x2, y2 = int(entry_x1.get()), int(entry_y1.get()), int(entry_x2.get()), int(entry_y2.get())
    draw_line_bresenham(x1, y1, x2, y2, color="green")
    update_image()

def display_circle():
    if not validate_circle_input():
        return
    image.paste("white", [0, 0, width, height])  # Clear canvas
    xc, yc, r = int(entry_xc.get()), int(entry_yc.get()), int(entry_r.get())
    draw_circle_bresenham(xc, yc, r, color="purple")
    update_image()

# Setup GUI
root = tk.Tk()
root.title("Line Drawing Algorithms")

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
button_dda.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

button_brute = tk.Button(root, text="Brute Force Line", command=display_brute_force)
button_brute.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

button_bresenham = tk.Button(root, text="Bresenham Line", command=display_bresenham)
button_bresenham.grid(row=3, column=4, columnspan=2, padx=5, pady=5)

button_circle = tk.Button(root, text="Bresenham Circle", command=display_circle)
button_circle.grid(row=3, column=6, columnspan=2, padx=5, pady=5)

# Initialize and show
update_image()
root.mainloop()
