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

# Read Pairs
def read_pairs(file_path):
    pairs = []
    with open(file_path, "r") as file:
        for line in file:
            x1, y1, z1, x2, y2, z2 = map(int, line.strip().split(','))  
            pairs.append(((x1, y1), (x2, y2)))  
    return pairs

# Translation Function
def translationFunc(points, pairs, dx, dy):
    T = np.array([
        [1, 0, dx],
        [0, 1, dy],
        [0, 0, 1]
    ])
    
    points_homogeneous = np.array([[x, y, 1] for x, y in points]).T
    translated_points = T @ points_homogeneous
    translated_points = [(int(x), int(y)) for x, y in translated_points[:2].T]

    translated_pairs = []
    for (x1, y1), (x2, y2) in pairs:
        pair_points = np.array([[x1, y1, 1], [x2, y2, 1]]).T
        translated_pair_points = T @ pair_points
        translated_pairs.append((
            (int(translated_pair_points[0][0]), int(translated_pair_points[1][0])),
            (int(translated_pair_points[0][1]), int(translated_pair_points[1][1]))
        ))

    return translated_points, translated_pairs

# Scale Function
def scaleFunc(points, pairs, sx, sy):
    S = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])
    
    points_homogeneous = np.array([[x, y, 1] for x, y in points]).T
    scaled_points = S @ points_homogeneous
    scaled_points = [(int(x), int(y)) for x, y in scaled_points[:2].T]
    
    scaled_pairs = []
    for (x1, y1), (x2, y2) in pairs:
        pair_points = np.array([[x1, y1, 1], [x2, y2, 1]]).T
        scaled_pair_points = S @ pair_points
        scaled_pairs.append((
            (int(scaled_pair_points[0][0]), int(scaled_pair_points[1][0])),
            (int(scaled_pair_points[0][1]), int(scaled_pair_points[1][1]))
        ))
    
    return scaled_points, scaled_pairs

# Rotate Function
def rotateFunc(points, pairs, angle_degrees, rotation_center=(0, 0)):
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

    rotated_pairs = []
    for (x1, y1), (x2, y2) in pairs:
        pair_points = np.array([[x1, y1, 1], [x2, y2, 1]]).T
        rotated_pair_points = transform_matrix @ pair_points
        rotated_pairs.append((
            (int(rotated_pair_points[0][0]), int(rotated_pair_points[1][0])),
            (int(rotated_pair_points[0][1]), int(rotated_pair_points[1][1]))
        ))
    
    return rotated_points, rotated_pairs

# Draw Frame
def draw_2d_primitives(pairs, points, image_size=(400, 500), output_file=None):
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)
    
    for (x1, y1), (x2, y2) in pairs:
        draw.line([(x1, y1), (x2, y2)], fill="green", width=2)

    for x, y in points:
        draw.ellipse([(x, y), (x, y)], fill="green")

    if output_file:
        image.save(output_file)
        print(f"Gambar berhasil disimpan: {output_file}")
    return image

# Call all function in tranformations
def animate_combined_transformations(points, pairs, image_size=(900, 600), num_frames=0, dx=0, dy=0, sx=1.0, sy=1.0, rotation_angle=0, rotation_center=None, output_file="img/TransformasiGeo/combined_animation.gif"):
    frames = []

    for frame in range(num_frames):
        translated_points, translated_pairs = translationFunc(points, pairs, dx * frame, dy * frame)
        scaled_points, scaled_pairs = scaleFunc(translated_points, translated_pairs, sx ** frame, sy ** frame)
        rotated_points, rotated_pairs = rotateFunc(scaled_points, scaled_pairs, rotation_angle * frame, rotation_center)
        frame_image = draw_2d_primitives(rotated_pairs, rotated_points, image_size=image_size)
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
pairs_file = "NewTask/pairs.txt"

# Read file input
points = read_points(points_file)
pairs = read_pairs(pairs_file)

# Call a function to display and to doing a tranformations 
draw_2d_primitives(pairs, points, output_file="img/output_static.png")
animate_combined_transformations(points, pairs, num_frames=30, dx=0, dy=0, sx=1.0, sy=1.0, rotation_angle=12, rotation_center=(200, 200))
