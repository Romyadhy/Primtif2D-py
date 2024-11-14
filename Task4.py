import tkinter as tk

def brute_force_line(canvas, x1, y1, x2, y2):
    if x1 == x2:
        # Handle vertical line
        for y in range(min(y1, y2), max(y1, y2) + 1):
            canvas.create_rectangle(x1, y, x1 + 1, y + 1, fill="black")
    else:
        m = (y2 - y1) / (x2 - x1)  # Slope of the line
        c = y1 - m * x1
        for x in range(min(x1, x2), max(x1, x2) + 1):
            y = round(m * x + c)
            canvas.create_rectangle(x, y, x + 1, y + 1, fill="black")

def dda_line(canvas, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1
    for _ in range(steps + 1):
        canvas.create_rectangle(round(x), round(y), round(x) + 1, round(y) + 1, fill="red")
        x += x_increment
        y += y_increment

def bresenham_line(canvas, x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    err = dx - dy

    while True:
        canvas.create_rectangle(x1, y1, x1 + 1, y1 + 1, fill="blue")

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

# Create a Tkinter window
root = tk.Tk()
root.title("Line Drawing Algorithms")

# Create a canvas for drawing
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Example coordinates for the lines (you can change these as needed)
x1, y1, x2, y2 = 50, 50, 350, 300

# Call each line drawing function
brute_force_line(canvas, x1, y1, x2, y2)
dda_line(canvas, 50, 100, 350, 350)
bresenham_line(canvas, 100, 50, 300, 350)

# Run the Tkinter main loop
root.mainloop()
