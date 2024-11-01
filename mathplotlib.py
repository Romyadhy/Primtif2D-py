import matplotlib.pyplot as plt

# Fungsi untuk menggambar titik dan garis
def plot_points_and_lines():
    plt.axhline(0, color='black',linewidth=0.5)  # Sumbu x
    plt.axvline(0, color='black',linewidth=0.5)  # Sumbu y
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

    # Menambahkan titik
    plt.plot(5, 5, 'o', color='red', label="Titik (5,5)")
    
    # Menggambar garis
    x1, y1 = -10, -5
    x2, y2 = 15, 7
    plt.plot([x1, x2], [y1, y2], color="blue", label=f"Garis dari ({x1},{y1}) ke ({x2},{y2})")

    # Pengaturan grafik
    plt.xlim(-20, 20)
    plt.ylim(-10, 10)
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Grafik dengan Titik dan Garis")
    plt.show()

# Panggil fungsi untuk menggambar grafik
plot_points_and_lines()













import matplotlib.pyplot as plt

# Algoritma Bresenham untuk menghasilkan titik-titik pada garis
def bresenham_line(x1, y1, x2, y2):
    points = []  # List untuk menyimpan titik-titik garis
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))  # Tambahkan titik ke daftar
        if x1 == x2 and y1 == y2:  # Jika mencapai titik akhir, keluar dari loop
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    return points

# Fungsi untuk menggambar garis dengan matplotlib
def plot_bresenham_line(x1, y1, x2, y2):
    points = bresenham_line(x1, y1, x2, y2)  # Hitung titik-titik dengan algoritma Bresenham
    x_values, y_values = zip(*points)  # Pisahkan koordinat x dan y

    # Plot titik-titik menggunakan matplotlib
    plt.figure(figsize=(6, 6))
    plt.plot(x_values, y_values, 'o', color='blue', markersize=5, label="Garis Bresenham")
    
    # Tambahkan sumbu x dan y
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    
    # Pengaturan grafik
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.xlim(min(x_values) - 1, max(x_values) + 1)
    plt.ylim(min(y_values) - 1, max(y_values) + 1)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Garis dari ({x1}, {y1}) ke ({x2}, {y2}) dengan Algoritma Bresenham")
    plt.legend()
    plt.show()

# Contoh menggambar garis dari titik (2, 2) ke (15, 10)
plot_bresenham_line(2, 2, 15, 10)



import matplotlib.pyplot as plt

# Fungsi untuk menggambar titik
def draw_point(x, y):
    plt.plot(x, y, marker="s", color="green", markersize=5)  # markersize dapat diatur untuk tampilan yang lebih halus

# Membuat figure dan axis
fig, ax = plt.subplots()

# Menggambar titik-titik pada garis
for x in range(100, 111):  # Rentang titik dari x=100 hingga x=110 pada y=20
    draw_point(x, 20)

# Pengaturan tampilan grafik agar titik-titik terlihat seperti garis
ax.set_aspect('equal')
ax.set_xlim(90, 120)  # Rentang x-axis agar tampilan fokus pada garis
ax.set_ylim(10, 30)   # Rentang y-axis agar tampilan fokus pada garis

# Menghilangkan sumbu dan bingkai
plt.axis('off')
plt.show()
