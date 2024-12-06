import numpy as np
from PIL import Image, ImageDraw

# Read Points
def read_points(file_path):
    points = []
    with open(file_path, "r") as file:
        for line in file:
            x, y, z = map(int, line.strip().split(','))  
            points.append((x, y))  
    return points

# Read Lines
def read_lines(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            start, end = map(int, line.strip().split())  
            lines.append((start, end))  
    return lines

# Translation Function
def translationFunc(points, lines, dx, dy):
    T = np.array([
        [1, 0, dx],
        [0, 1, dy],
        [0, 0, 1]
    ])
    
    points_homogeneous = np.array([[x, y, 1] for x, y in points]).T
    translated_points = T @ points_homogeneous
    translated_points = [(int(x), int(y)) for x, y in translated_points[:2].T]

    return translated_points, lines

# Scale Function
def scaleFunc(points, lines, sx, sy):
    S = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])
    
    points_homogeneous = np.array([[x, y, 1] for x, y in points]).T
    scaled_points = S @ points_homogeneous
    scaled_points = [(int(x), int(y)) for x, y in scaled_points[:2].T]
    
    return scaled_points, lines

# Rotate Function
def rotateFunc(points, lines, angle_degrees, rotation_center=(0, 0)):
    angle_radians = np.radians(angle_degrees)
    cx, cy = rotation_center

    # Translasi ke origin
    T_to_origin = np.array([
        [1, 0, -cx],
        [0, 1, -cy],
        [0, 0, 1]
    ])

    # Matriks rotasi
    R = np.array([
        [np.cos(angle_radians), -np.sin(angle_radians), 0],
        [np.sin(angle_radians), np.cos(angle_radians), 0],
        [0, 0, 1]
    ])

    # Translasi kembali
    T_back = np.array([
        [1, 0, cx],
        [0, 1, cy],
        [0, 0, 1]
    ])
    
    # Gabungkan transformasi
    transform_matrix = T_back @ R @ T_to_origin

    points_homogeneous = np.array([[x, y, 1] for x, y in points]).T
    rotated_points = transform_matrix @ points_homogeneous
    rotated_points = [(int(x), int(y)) for x, y in rotated_points[:2].T]
    
    return rotated_points, lines

# Draw Line using input file
def drawLine2D(lines, points, image_size=(400, 500), output_file=None):
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)
    
    for start, end in lines:
        draw.line([points[start], points[end]], fill="green")

    for x, y in points:
        draw.ellipse([(x, y), (x, y)], fill="green") 

    if output_file:
        image.save(output_file)
        print(f"Gambar berhasil disimpan: {output_file}")
    return image

# Call all function in transformations
def tranformationsGeo(points, lines, image_size=(900, 600), num_frames=0, dx=0, dy=0, sx=1.0, sy=1.0, rotation_angle=0, rotation_center=None, output_file="img/TransformasiGeo/combined_animation.gif"):
    frames = []

    for frame in range(num_frames):
        translated_points, translated_lines = translationFunc(points, lines, dx * frame, dy * frame)
        scaled_points, scaled_lines = scaleFunc(translated_points, translated_lines, sx ** frame, sy ** frame)
        rotated_points, rotated_lines = rotateFunc(scaled_points, scaled_lines, rotation_angle * frame, rotation_center)
        frame_image = drawLine2D(rotated_lines, rotated_points, image_size=image_size)
        frames.append(frame_image)

    frames[0].save(
        output_file,
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0
    )
    print(f"Animasi gabungan telah disimpan sebagai: {output_file}")

# Input File txt
points_file = "NewTask/points.txt"
lines_file = "NewTask/lines.txt"

# Read file input
points = read_points(points_file)
lines = read_lines(lines_file)

# Call a function to display and to doing a transformations 
drawLine2D(lines, points, output_file="img/output_static.png")
tranformationsGeo(points, lines, num_frames=60, dx=0, dy=0, sx=1.0, sy=1.01, rotation_angle=-1.5, rotation_center=(200, 200))
