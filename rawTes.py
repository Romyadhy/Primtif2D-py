# Function to draw empty grid
def create_grid(width, height):
    return [[" " for _ in range(width)] for _ in range(height)]

# function draw point
def draw_point(grid, x, y):
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):  # Pastikan titik ada di dalam batas grid
        grid[y][x] = "-"  

# function draw line
def draw_line(grid, x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        draw_point(grid, x1, y1)  # Gambar titik di koordinat (x1, y1)
        if x1 == x2 and y1 == y2:  # Jika sudah sampai di titik akhir, berhenti
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

# function to show grid
def print_grid(grid):
    for row in grid:
        print("".join(row))

# Grid size
width, height = 50, 50
grid = create_grid(width, height)  # Buat grid kosong

# call function
draw_point(grid, 4, 2)          
draw_line(grid, 4, 4, 30, 4)      


print_grid(grid)
