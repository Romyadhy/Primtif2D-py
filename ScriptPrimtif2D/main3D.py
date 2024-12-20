import numpy as np
from PIL import Image, ImageDraw


points_file = "ScriptPrimtif2D/point3D.txt"
lines_file = "ScriptPrimtif2D/lines3D.txt"

# Point
def read_points(file_path):
    points = []
    with open(file_path, "r") as file:
        for line in file:
            x, y, z = map(int, line.strip().split(','))  
            points.append((x, y, z))  
    return points

# Line
def read_lines(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            start, end = map(int, line.strip().split())  
            lines.append((start, end))  
    return lines


points = read_points(points_file)
lines = read_lines(lines_file)

# Translation Function
def translationFunc(points, dx, dy, dz):
    T = np.array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ])
    points_homogeneous = np.array([[x, y, z, 1] for x, y, z in points]).T
    translated_points = T @ points_homogeneous
    return translated_points[:3].T

# Scale Function
def scaleFunc(points, sx, sy, sz):
    S = np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])
    points_homogeneous = np.array([[x, y, z, 1] for x, y, z in points]).T
    scaled_points = S @ points_homogeneous
    return scaled_points[:3].T

# Rotate Function 
def rotateFunc(points, angle_degrees, axis, rotation_center=(0, 0, 0)):
    angle_radians = np.radians(angle_degrees)
    cx, cy, cz = rotation_center

    # Translation into the origin
    T_to_origin = np.array([
        [1, 0, 0, -cx],
        [0, 1, 0, -cy],
        [0, 0, 1, -cz],
        [0, 0, 0, 1]
    ])

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
    else:
        raise ValueError("Invalid axis, choose from 'x', 'y', or 'z'.")

    # Translation back
    T_back = np.array([
        [1, 0, 0, cx],
        [0, 1, 0, cy],
        [0, 0, 1, cz],
        [0, 0, 0, 1]
    ])

    transform_matrix = T_back @ R @ T_to_origin

    points_homogeneous = np.array([[x, y, z, 1] for x, y, z in points]).T
    rotated_points = transform_matrix @ points_homogeneous
    return rotated_points[:3].T

# Perspective Pojection
def PersprectiveProj(points, fov=500, viewer_distance=1000):
    projected_points = []
    for x, y, z in points:
        factor = fov / (viewer_distance + z)
        x2d = int(x * factor + 450) 
        y2d = int(-y * factor + 400)
        projected_points.append((x2d, y2d))
    return projected_points

# Draw Object
def drawObject(lines, points, image_size=(900, 800), output_file=None):
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)
    
    projected_points = PersprectiveProj(points)
    
    for start, end in lines:
        draw.line([projected_points[start], projected_points[end]], fill="red")

    if output_file:
        image.save(output_file)
        print(f"Image saved: {output_file}")
    return image

# Transformation 
def transformations3D(points, lines, image_size=(900, 900), num_frames=0, dx=0, dy=0, dz=0, 
                       sx=1.0, sy=1.0, sz=1.0, rotation_angle=0, rotation_axis="", rotation_center=(0, 0, 0), 
                       output_file=""):
    frames = []
    for frame in range(num_frames):
        translated_points = translationFunc(points, dx * frame, dy * frame, dz * frame)
        scaled_points = scaleFunc(translated_points, sx ** frame, sy ** frame, sz ** frame)
        rotated_points = rotateFunc(scaled_points, rotation_angle * frame, rotation_axis, rotation_center)
        frame_image = drawObject(lines, rotated_points, image_size=image_size)
        frames.append(frame_image)

    frames[0].save(
        output_file,
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0
    )
    print(f"3D Transformation saved: {output_file}")

# Output
drawObject(lines, points, output_file="img/output_static_3D.png")
transformations3D(points, lines, num_frames=30, dx=0, dy=0, dz=0, sx=1.0, sy=1.0, sz=1.0, rotation_angle=12, rotation_axis="x", rotation_center=(100, 100, 100), output_file="img/TransformasiGeo/3DTransformation.gif")
