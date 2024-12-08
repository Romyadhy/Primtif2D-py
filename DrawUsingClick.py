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

# Function to update and display image on canvas
def update_image():
    global photo_image
    photo_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo_image)

# Function to clear canvas
def clear_canvas():
    global image, draw, start_point, click_log
    start_point = None
    click_log = []
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    update_image()

# Function to handle canvas click for drawing lines and logging
start_point = None  # To store the first click point
click_log = []  # To log click coordinates

def on_canvas_click(event):
    global start_point
    # Log the click coordinates
    click_log.append((event.x, event.y))
    print(f"Clicked at: ({event.x}, {event.y})")  # Print coordinates in console
    if start_point is None:
        # First click: record the starting point
        start_point = (event.x, event.y)
    else:
        # Second click: draw the line and reset the start point
        end_point = (event.x, event.y)
        draw_line_dda(start_point[0], start_point[1], end_point[0], end_point[1])
        start_point = None

# Function to display logged coordinates
def show_click_log():
    if click_log:
        log_message = "\n".join([f"Point {i+1}: {coord}" for i, coord in enumerate(click_log)])
        messagebox.showinfo("Click Log", f"Coordinates of clicks:\n\n{log_message}")
    else:
        messagebox.showinfo("Click Log", "No clicks logged yet.")

# Setup GUI
root = tk.Tk()
root.title("Interactive Line Drawing with Click Coordinates")

# Canvas widget for displaying image
canvas = tk.Canvas(root, width=width, height=height)
canvas.grid(row=0, column=0, columnspan=6)

# Bind mouse click to canvas
canvas.bind("<Button-1>", on_canvas_click)

# Buttons
button_clear = tk.Button(root, text="Clear Canvas", command=clear_canvas)
button_clear.grid(row=1, column=0, padx=10, pady=20)

button_show_log = tk.Button(root, text="Show Click Log", command=show_click_log)
button_show_log.grid(row=1, column=1, padx=10, pady=20)

# Initialize and show
update_image()
root.mainloop()