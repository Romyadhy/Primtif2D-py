import numpy as np
from PIL import Image, ImageDraw

# Input File txt
points_file = "ScriptPrimtif2D/point3D.txt"
lines_file = "ScriptPrimtif2D/lines3D.txt"

# Read Points
def read_points(file_path):
    points = []
    with open(file_path, "r") as file:
        for line in file:
            x, y, z = map(int, line.strip().split(','))  # Membaca x, y, z
            points.append((x, y, z))
    return points

# Read Lines
def read_lines(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            start, end = map(int, line.strip().split())  
            lines.append((start, end))  
    return lines

# Proyeksi Perspektif 3D ke 2D
def project_3d_to_2d(points, fov=500, viewer_distance=1000):
    projected_points = []
    for x, y, z in points:
        factor = fov / (viewer_distance + z)
        x_2d = int(x * factor + 450)  # Menyesuaikan posisi tengah gambar
        y_2d = int(-y * factor + 400)
        projected_points.append((x_2d, y_2d))
    return projected_points

# Translasi 3D
def translation_3d(points, dx, dy, dz):
    T = np.array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ])
    points_homogeneous = np.array([[x, y, z, 1] for x, y, z in points]).T
    translated_points = T @ points_homogeneous
    return [tuple(translated_points[:3, i]) for i in range(translated_points.shape[1])]

# Skala 3D
def scale_3d(points, sx, sy, sz):
    S = np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])
    points_homogeneous = np.array([[x, y, z, 1] for x, y, z in points]).T
    scaled_points = S @ points_homogeneous
    return [tuple(scaled_points[:3, i]) for i in range(scaled_points.shape[1])]

# Rotasi 3D
def rotate_3d(points, angle, axis):
    angle_radians = np.radians(angle)
    if axis == 'x':
        R = np.array([
            [1, 0, 0, 0],
            [0, np.cos(angle_radians), -np.sin(angle_radians), 0],
            [0, np.sin(angle_radians), np.cos(angle_radians), 0],
            [0, 0, 0, 1]
        ])
    elif axis == 'y':
        R = np.array([
            [np.cos(angle_radians), 0, np.sin(angle_radians), 0],
            [0, 1, 0, 0],
            [-np.sin(angle_radians), 0, np.cos(angle_radians), 0],
            [0, 0, 0, 1]
        ])
    elif axis == 'z':
        R = np.array([
            [np.cos(angle_radians), -np.sin(angle_radians), 0, 0],
            [np.sin(angle_radians), np.cos(angle_radians), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    points_homogeneous = np.array([[x, y, z, 1] for x, y, z in points]).T
    rotated_points = R @ points_homogeneous
    return [tuple(rotated_points[:3, i]) for i in range(rotated_points.shape[1])]

# Draw Line 3D
def draw_line_3d(lines, points, image_size=(900, 800), output_file=None):
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)

    projected_points = project_3d_to_2d(points)

    # for x, y in projected_points:
    #     draw.ellipse([(x - 2, y - 2), (x + 2, y + 2)], fill="red")
    
    for start, end in lines:
        draw.line([projected_points[start], projected_points[end]], fill="red")

    if output_file:
        image.save(output_file)
        print(f"Image saved: {output_file}")
    return image

# Fungsi untuk membuat GIF dari transformasi geometri
def generate_transformations_gif(points, lines, output_gif="transformations.gif"):
    frames = []

    # # Translasi
    # for dx in range(0, 200, 20):  # Translasi ke kanan
    #     translated_points = translation_3d(points, dx, 0, 0)
    #     frame = draw_line_3d(lines, translated_points)
    #     frames.append(frame)

    # # Skala
    # for scale_factor in np.linspace(1, 2, 10):  # Membesarkan ukuran
    #     scaled_points = scale_3d(points, scale_factor, scale_factor, scale_factor)
    #     frame = draw_line_3d(lines, scaled_points)
    #     frames.append(frame)

    # Rotasi sumbu X
    for angle in range(0, 361, 5):  # Rotasi penuh (360 derajat)
        rotated_points = rotate_3d(points, angle, axis='x')
        frame = draw_line_3d(lines, rotated_points)
        frames.append(frame)

    # # Rotasi sumbu Y
    # for angle in range(0, 180, 5):  # Rotasi penuh (360 derajat)
    #     rotated_points = rotate_3d(points, angle, axis='y')
    #     frame = draw_line_3d(lines, rotated_points)
    #     frames.append(frame)

    # # Rotasi sumbu Z
    # for angle in range(0, 361, 30):  # Rotasi penuh (360 derajat)
    #     rotated_points = rotate_3d(points, angle, axis='z')
    #     frame = draw_line_3d(lines, rotated_points)
    #     frames.append(frame)

    # Membuat GIF
    frames[0].save(
        output_gif,
        save_all=True,
        append_images=frames[1:],
        optimize=False,
        duration=100,  # Durasi antar frame dalam milidetik
        loop=0  # Looping terus-menerus
    )
    print(f"GIF saved: {output_gif}")

# Call the function to draw the 3D shape
points = read_points(points_file)
lines = read_lines(lines_file)

draw_line_3d(lines, points, output_file="output_3d.png")

# Generate GIF
generate_transformations_gif(points, lines)
