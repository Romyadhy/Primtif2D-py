from PIL import Image, ImageDraw

def read_points(file_path):
    """
    Membaca file titik (points) dan mengembalikan list koordinat.
    """
    points = []
    with open(file_path, 'r') as f:
        for line in f:
            x, y, _ = map(int, line.strip().split(','))  # Abaikan nilai Z
            points.append((x, y))
    return points

def read_lines(file_path):
    """
    Membaca file garis (lines) dan mengembalikan list pasangan indeks.
    """
    lines = []
    with open(file_path, 'r') as f:
        for line in f:
            start, end = map(int, line.strip().split())  # Gunakan spasi sebagai pemisah
            lines.append((start, end))
    return lines

def draw_lines(points, lines, output_file):
    """
    Menggambar garis berdasarkan titik dan koneksi.
    """
    # Tentukan ukuran gambar berdasarkan titik maksimum
    max_x = max([p[0] for p in points]) + 50
    max_y = max([p[1] for p in points]) + 50

    # Buat gambar kosong
    img = Image.new('RGB', (max_x, max_y), 'white')
    draw = ImageDraw.Draw(img)

    # Gambar garis
    for start, end in lines:
        draw.line([points[start], points[end]], fill='black', width=2)

    # Simpan gambar
    img.save(output_file)
    print(f"Gambar berhasil disimpan di {output_file}")

# File input
points_file = "NewTask/points.txt"
lines_file = "NewTask/lines.txt"
output_file = "output_image1.png"

# Baca data dari file
points = read_points(points_file)
lines = read_lines(lines_file)

# Gambar garis
draw_lines(points, lines, output_file)
