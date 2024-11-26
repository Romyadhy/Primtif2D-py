import numpy as np
from PIL import Image, ImageDraw, ImageSequence

# Fungsi membaca points
def read_points(file_path):
    points = []
    with open(file_path, "r") as file:
        for line in file:
            x, y, z = map(int, line.strip().split(','))  # Baca x, y, z
            points.append((x, y))  # Abaikan z
    return points

# Fungsi membaca pairs
def read_pairs(file_path):
    pairs = []
    with open(file_path, "r") as file:
        for line in file:
            x1, y1, z1, x2, y2, z2 = map(int, line.strip().split(','))  # Baca x, y, z
            pairs.append(((x1, y1), (x2, y2)))  # Abaikan z
    return pairs

# Fungsi translasi menggunakan matriks
def translate_with_matrix(points, pairs, dx, dy):
    # Matriks translasi
    T = np.array([
        [1, 0, dx],
        [0, 1, dy],
        [0, 0, 1]
    ])
    
    # Translasi untuk points
    points_homogeneous = np.array([[x, y, 1] for x, y in points]).T  # Ubah ke bentuk homogen
    translated_points = T @ points_homogeneous  # Matriks dikali
    translated_points = [(int(x), int(y)) for x, y in translated_points[:2].T]

    # Translasi untuk pairs
    translated_pairs = []
    for (x1, y1), (x2, y2) in pairs:
        pair_points = np.array([[x1, y1, 1], [x2, y2, 1]]).T  # Dua titik dalam bentuk homogen
        translated_pair_points = T @ pair_points  # Matriks dikali
        translated_pairs.append((
            (int(translated_pair_points[0][0]), int(translated_pair_points[1][0])),  # (x1', y1')
            (int(translated_pair_points[0][1]), int(translated_pair_points[1][1]))   # (x2', y2')
        ))

    return translated_points, translated_pairs

# Fungsi scaling menggunakan matriks
def scale_with_matrix(points, pairs, sx, sy):
    S = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])
    
    # Scaling untuk points
    points_homogeneous = np.array([[x, y, 1] for x, y in points]).T
    scaled_points = S @ points_homogeneous
    scaled_points = [(int(x), int(y)) for x, y in scaled_points[:2].T]
    
    # Scaling untuk pairs
    scaled_pairs = []
    for (x1, y1), (x2, y2) in pairs:
        pair_points = np.array([[x1, y1, 1], [x2, y2, 1]]).T
        scaled_pair_points = S @ pair_points
        scaled_pairs.append((
            (int(scaled_pair_points[0][0]), int(scaled_pair_points[1][0])),
            (int(scaled_pair_points[0][1]), int(scaled_pair_points[1][1]))
        ))
    
    return scaled_points, scaled_pairs

# Fungsi rotasi menggunakan matriks
def rotate_with_matrix(points, pairs, angle_degrees):
    angle_radians = np.radians(angle_degrees)
    R = np.array([
        [np.cos(angle_radians), -np.sin(angle_radians), 0],
        [np.sin(angle_radians), np.cos(angle_radians), 0],
        [0, 0, 1]
    ])
    
    # Rotasi untuk points
    points_homogeneous = np.array([[x, y, 1] for x, y in points]).T
    rotated_points = R @ points_homogeneous
    rotated_points = [(int(x), int(y)) for x, y in rotated_points[:2].T]
    
    # Rotasi untuk pairs
    rotated_pairs = []
    for (x1, y1), (x2, y2) in pairs:
        pair_points = np.array([[x1, y1, 1], [x2, y2, 1]]).T
        rotated_pair_points = R @ pair_points
        rotated_pairs.append((
            (int(rotated_pair_points[0][0]), int(rotated_pair_points[1][0])),
            (int(rotated_pair_points[0][1]), int(rotated_pair_points[1][1]))
        ))
    
    return rotated_points, rotated_pairs



# Fungsi menggambar frame
def draw_2d_primitives(pairs, points, image_size=(400, 500), output_file=None):
    # Buat gambar kosong
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)
    
    # Gambar garis dari pairs
    for (x1, y1), (x2, y2) in pairs:
        draw.line([(x1, y1), (x2, y2)], fill="green", width=2)

    # Gambar titik dari points
    for x, y in points:
        draw.ellipse([(x-1, y-1), (x+1, y+1)], fill="green")

    if output_file:
        image.save(output_file)
        print("Gambar di simpan di: {output_file}")
    return image

# # Fungsi animasi translasi
# def animate_translation_with_matrix(points, pairs, image_size=(400, 500), num_frames=20, dx=5, dy=5, output_file="img/TransformasiGeo/translation_animation.gif"):
#     frames = []

#     for frame in range(num_frames):
#         # Lakukan translasi menggunakan matriks
#         translated_points, translated_pairs = translate_with_matrix(points, pairs, dx * frame, dy * frame)
        
#         # Gambar frame
#         frame_image = draw_2d_primitives(translated_pairs, translated_points, image_size=image_size)
#         frames.append(frame_image)

#     # Simpan sebagai animasi GIF
#     frames[0].save(
#         output_file,
#         save_all=True,
#         append_images=frames[1:],
#         duration=100,
#         loop=0
#     )
#     print(f"Animasi translasi telah disimpan sebagai: {output_file}")

# Fungsi animasi gabungan
def animate_combined_transformations(points, pairs, image_size=(900, 600), num_frames=30, dx=5, dy=5, sx=1.05, sy=1.05, rotation_angle=5, output_file="img/TransformasiGeo/combined_animation.gif"):
    frames = []

    for frame in range(num_frames):
        # Translasi
        translated_points, translated_pairs = translate_with_matrix(points, pairs, dx * frame, dy * frame)
        
        # Skalar
        scaled_points, scaled_pairs = scale_with_matrix(translated_points, translated_pairs, sx ** frame, sy ** frame)
        
        # Rotasi
        rotated_points, rotated_pairs = rotate_with_matrix(scaled_points, scaled_pairs, rotation_angle * frame)
        
        # Gambar frame
        frame_image = draw_2d_primitives(rotated_pairs, rotated_points, image_size=image_size)
        frames.append(frame_image)

    # Simpan animasi sebagai GIF
    frames[0].save(
        output_file,
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0
    )
    print(f"Animasi gabungan telah disimpan sebagai: {output_file}")

# File input
points_file = "NewTask/points.txt"  # Sesuaikan dengan lokasi file
pairs_file = "NewTask/pairs.txt"    # Sesuaikan dengan lokasi file

# Baca data
points = read_points(points_file)
pairs = read_pairs(pairs_file)

draw_2d_primitives(pairs, points, output_file="img/output_static.png")
# Jalankan animasi translasi
# animate_translation_with_matrix(points, pairs, num_frames=30, dx=0, dy=5)  # dx positif: kanan, dy negatif: atas

animate_combined_transformations(points, pairs, num_frames=30, dx=0, dy=0, sx=1.01, sy=1.01, rotation_angle=0)













# from PIL import Image, ImageDraw

# # Fungsi membaca points
# def read_points(file_path):
#     points = []
#     with open(file_path, "r") as file:
#         for line in file:
#             x, y, z = map(int, line.strip().split(','))  # Baca x, y, z
#             points.append((x, y))  # Abaikan z, gunakan x dan y
#     return points

# # Fungsi membaca pairs
# def read_pairs(file_path):
#     pairs = []
#     with open(file_path, "r") as file:
#         for line in file:
#             x1, y1, z1, x2, y2, z2 = map(int, line.strip().split(','))  # Baca x, y, z
#             pairs.append(((x1, y1), (x2, y2)))  # Abaikan z
#     return pairs

# # Fungsi menggambar
# def draw_2d_primitives(pairs, points, image_size=(400, 500), output_file="img/output.png"):
#     # Buat gambar kosong
#     image = Image.new("RGB", image_size, "white")
#     draw = ImageDraw.Draw(image)
    
#     # Gambar garis dari pairs
#     for (x1, y1), (x2, y2) in pairs:
#         draw.line([(x1, y1), (x2, y2)], fill="green", width=3)

#     # Gambar titik dari points
#     for x, y in points:
#         draw.ellipse([(x-1, y-1), (x+1, y+1)], fill="green")

#     # Simpan gambar
#     image.save(output_file)
#     print(f"Gambar telah disimpan ke {output_file}")

# # File input
# points_file = "NewTask\points.txt"
# pairs_file = "NewTask\pairs.txt"

# # Baca data
# points = read_points(points_file)
# pairs = read_pairs(pairs_file)

# # Gambar hasil
# draw_2d_primitives(pairs, points)