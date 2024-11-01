import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D

# Fungsi untuk menggambar titik
def draw_point(x, y, color=(1, 1, 1)):
    glColor3f(*color)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

# Algoritma DDA untuk menggambar garis
def draw_line_dda(x1, y1, x2, y2, color=(1, 0, 0)):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    
    x_increment = dx / steps
    y_increment = dy / steps
    
    x = x1
    y = y1
    glColor3f(*color)
    glBegin(GL_POINTS)
    for _ in range(int(steps) + 1):
        glVertex2f(x, y)
        x += x_increment
        y += y_increment
    glEnd()

# Algoritma Brute Force untuk menggambar garis
def draw_line_bruteforce(x1, y1, x2, y2, color=(0, 1, 0)):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):
        slope = dy / dx if dx != 0 else 0
        y = y1
        glColor3f(*color)
        glBegin(GL_POINTS)
        for x in range(x1, x2 + 1 if x2 > x1 else x2 - 1, 1 if x2 > x1 else -1):
            glVertex2f(x, round(y))
            y += slope
    else:
        slope = dx / dy if dy != 0 else 0
        x = x1
        glColor3f(*color)
        glBegin(GL_POINTS)
        for y in range(y1, y2 + 1 if y2 > y1 else y2 - 1, 1 if y2 > y1 else -1):
            glVertex2f(round(x), y)
            x += slope
    glEnd()

# Algoritma Bresenham untuk menggambar garis
def draw_line_bresenham(x1, y1, x2, y2, color=(0, 0, 1)):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    
    glColor3f(*color)
    glBegin(GL_POINTS)
    while True:
        glVertex2f(x1, y1)
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    glEnd()

# Fungsi utama untuk inisialisasi Pygame dan OpenGL
def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500), DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 500, 0, 500)  # Mengatur viewport OpenGL agar sesuai dengan ukuran layar

    # Loop untuk menjalankan aplikasi
    running = True
    while running:
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Menggambar titik dan garis menggunakan tiga algoritma
        draw_point(50, 50, color=(1, 1, 0))           # Titik pada koordinat (50, 50) warna kuning
        draw_line_dda(100, 100, 400, 300, color=(1, 0, 0))      # Garis DDA warna merah
        draw_line_bruteforce(50, 200, 200, 50, color=(0, 1, 0)) # Garis Brute Force warna hijau
        draw_line_bresenham(300, 300, 400, 400, color=(0, 0, 1)) # Garis Bresenham warna biru
        
        pygame.display.flip()
        
        # Event handler untuk keluar dari aplikasi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()

# Jalankan program
main()
