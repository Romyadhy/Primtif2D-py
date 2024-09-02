import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Fungsi untuk menggambar titik-titik
def draw_point():
    glBegin(GL_POINTS)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 0.2)
    glVertex2f(0.0, 0.3)
    glVertex2f(0.0, 0.4)
    glEnd()

# Fungsi untuk menggambar garis
def draw_line():
    glBegin(GL_LINES)
    glVertex2f(-0.5, 0.0)
    glVertex2f(0.5, 0.0)
    glEnd()

# Fungsi untuk menggambar persegi
def draw_square():
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)  # Kiri Bawah
    glVertex2f(0.5, -0.5)   # Kanan Bawah
    glVertex2f(0.5, 0.5)    # Kanan Atas
    glVertex2f(-0.5, 0.5)   # Kiri Atas
    glEnd()

# Fungsi untuk menggambar segitiga
def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 0.5)    # Atas
    glVertex2f(-0.5, -0.5)  # Kiri Bawah
    glVertex2f(0.5, -0.5)   # Kanan Bawah
    glEnd()

# Fungsi untuk menggambar lingkaran
def draw_circle(radius, num_segments):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0.0, 0.0)  # Titik pusat
    for i in range(num_segments + 1):  # +1 untuk menutup lingkaran
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
    gluOrtho2D(-2, 2, -2, 2)  # Setting 2D ortogonal view dengan rentang yang lebih besar
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Membersihkan layar
        
        # Menggambar Titik
        glColor3f(1.0, 0.0, 0.0)  # Warna merah
        glPointSize(5)  # Ukuran titik
        glPushMatrix()  # Simpan matriks saat ini
        glTranslatef(-1.5, 1.5, 0.0)  # Pindahkan titik ke kiri atas
        draw_point()
        glPopMatrix()  # Kembalikan matriks
        
        # Menggambar Garis
        glColor3f(0.0, 1.0, 0.0)  # Warna hijau
        glLineWidth(2)  # Lebar garis
        glPushMatrix()
        glTranslatef(1.5, 1.5, 0.0)  # Pindahkan garis ke kanan atas
        draw_line()
        glPopMatrix()
        
        # Menggambar Persegi
        glColor3f(0.0, 0.0, 1.0)  # Warna biru
        glPushMatrix()
        glTranslatef(-1.5, -1.5, 0.0)  # Pindahkan persegi ke kiri bawah
        draw_square()
        glPopMatrix()
        
        # Menggambar Segitiga
        glColor3f(1.0, 1.0, 0.0)  # Warna kuning
        glPushMatrix()
        glTranslatef(1.5, -1.5, 0.0)  # Pindahkan segitiga ke kanan bawah
        draw_triangle()
        glPopMatrix()
        
        # Menggambar Lingkaran
        glColor3f(1.0, 0.0, 1.0)  # Warna magenta
        glPushMatrix()
        glTranslatef(0.0, 0.0, 0.0)  # Pindahkan lingkaran ke pusat
        draw_circle(0.5, 100)
        glPopMatrix()
        
        pygame.display.flip()  # Update display
        pygame.time.wait(10)  # Delay 10ms

# Menjalankan program
main()
