import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# draw_point
def draw_point():
    glBegin(GL_POINTS)
    glVertex2f(0.0, 0.0)  # Koordinat titik (0, 0)
    glVertex2f(0.0, 0.2)  # Koordinat titik (0, 0)
    glVertex2f(0.0, 0.3)  # Koordinat titik (0, 0)
    glVertex2f(0.0, 0.4)  # Koordinat titik (0, 0)
    glEnd()

# Draw Line
def draw_line():
    glBegin(GL_LINES)
    glVertex2f(-0.5, 0.0)
    glVertex2f(0.5, 0.0)
    glEnd()

# Draw Rectangle
def draw_square():
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5) #kiribawah
    glVertex2f(0.5, -0.5) #kananbawah
    glVertex2f(0.5, 0.5) #kananatas
    glVertex2f(-0.5, 0.5) #kiriatas
    glEnd()

# Draw Triangle
def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 0.5) #atas
    glVertex2f(-0.5, -0.5) #kiribawah
    glVertex2f(0.5, -0.5) #kananbawah
    glEnd()

# Draw Circle
def draw_circle(radius, num_segments):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()


# Fungsi utama untuk inisialisasi dan rendering
def main():
    pygame.init()  # Inisialisasi pygame
    display = (800, 600)  # Resolusi jendela
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Warna background hitam
    gluOrtho2D(-1, 1, -1, 1)  # Setting 2D ortogonal view
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Membersihkan layar
        glColor3f(0.0, 1.0, 0.0)  # Warna titik merah
        glPointSize(3)  # Ukuran titik
        # draw_point()  
        # draw_line()
        draw_square()
        # draw_triangle()
        # draw_circle(0.5, 100)
        
        pygame.display.flip()  # Update display
        pygame.time.wait(10)  # Delay 10ms

# Menjalankan program
main()
