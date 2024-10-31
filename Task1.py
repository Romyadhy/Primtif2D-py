from PIL import Image, ImageDraw

# Ukuran kanvas
width, height = 500, 500
# Buat kanvas kosong (background putih)
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Fungsi untuk menggambar titik
def draw_point(x, y, color="black"):
    # Menggambar titik sebagai persegi kecil 1x1 pixel
    draw.rectangle([x, y, x+1, y+1], fill=color)

# Fungsi untuk menggambar garis menggunakan algoritma DDA
def draw_line(x1, y1, x2, y2, color="black"):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    
    x_increment = dx / steps
    y_increment = dy / steps
    
    x = x1
    y = y1
    
    for _ in range(steps):
        draw_point(round(x), round(y), color)  # Gunakan fungsi draw_point untuk setiap titik pada garis
        x += x_increment
        y += y_increment

# Menggambar beberapa titik dan garis
draw_point(50, 50, color="blue")           # Titik di (50, 50)
draw_line(100, 100, 400, 300, color="red") # Garis dari (100, 100) ke (400, 300)
# draw_line(50, 200, 200, 50, color="green") # Garis dari (50, 200) ke (200, 50)
# draw_line(300, 300, 400, 400, color="purple") # Garis dari (300, 300) ke (400, 400)

# Tampilkan dan simpan hasil gambar
image.show()       # Menampilkan gambar di viewer default
image.save("/img/titik_dan_garis.png") # Menyimpan gambar
