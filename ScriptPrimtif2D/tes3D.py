import numpy as np
from PIL import Image, ImageDraw

# Input file paths
points_file = "ScriptPrimtif2D/point3D.txt"
lines_file = "ScriptPrimtif2D/lines3D.txt"

# Utility functions
# Read points from file (with homogeneous coordinate)
def read_points(file_path):
    points = []
    with open(file_path, "r") as file:
        for line in file:
            x, y, z = map(int, line.strip().split(','))
            points.append((x, y, z, 1))  # Add homogeneous coordinate (w=1)
    return points

# Read lines from file (indices of start and end points)
def read_lines(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            start, end = map(int, line.strip().split())
            lines.append((start, end))
    return lines

# Transformation matrices
def translation_matrix(dx, dy, dz):
    return np.array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ])

def scaling_matrix(sx, sy, sz):
    return np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])

def rotation_matrix(angle_degrees, axis='z'):
    angle_radians = np.radians(angle_degrees)
    if axis == 'z':
        return np.array([
            [np.cos(angle_radians), -np.sin(angle_radians), 0, 0],
            [np.sin(angle_radians), np.cos(angle_radians), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    elif axis == 'x':
        return np.array([
            [1, 0, 0, 0],
            [0, np.cos(angle_radians), -np.sin(angle_radians), 0],
            [0, np.sin(angle_radians), np.cos(angle_radians), 0],
            [0, 0, 0, 1]
        ])
    elif axis == 'y':
        return np.array([
            [np.cos(angle_radians), 0, np.sin(angle_radians), 0],
            [0, 1, 0, 0],
            [-np.sin(angle_radians), 0, np.cos(angle_radians), 0],
            [0, 0, 0, 1]
        ])

# Apply transformation matrix to points
def apply_transformation(points, transformation_matrix):
    transformed_points = [
        tuple(np.dot(transformation_matrix, point)) for point in points
    ]
    return [(x, y, z) for x, y, z, _ in transformed_points]  # Drop homogeneous coordinate

# Project 3D points to 2D plane
def project_points(points, width, height, scale=500):
    projected_points = []
    for x, y, z in points:
        px = int(width / 2 + scale * x / (z + scale))
        py = int(height / 2 - scale * y / (z + scale))
        projected_points.append((px, py))
    return projected_points

# Draw lines between points on an image
def draw_lines(points, lines, image):
    draw = ImageDraw.Draw(image)
    for start, end in lines:
        draw.line([points[start], points[end]], fill="red", width=2)

# Generate animation frames with transformations
def generate_frames(points, lines, num_frames=60, dx=0, dy=0, dz=0, sx=1.0, sy=1.0, sz=1.0, rotation_angle=0, axis='z', imgsize=(800, 800)):
    width, height = imgsize
    images = []

    for frame in range(num_frames):
        # Create transformation matrix for the current frame
        translation = translation_matrix(dx * frame, dy * frame, dz * frame)
        scaling = scaling_matrix(sx ** frame, sy ** frame, sz ** frame)
        rotation = rotation_matrix(rotation_angle * frame, axis)

        # Combine transformations
        transformation_matrix = translation @ scaling @ rotation

        # Apply transformations to points
        transformed_points = apply_transformation(points, transformation_matrix)

        # Project 3D points to 2D
        projected_points = project_points(transformed_points, width, height)

        # Create image for the current frame
        image = Image.new("RGB", (width, height), "white")
        draw_lines(projected_points, lines, image)
        images.append(image)

    return images

# Save animation as GIF
def save_gif(images, output_path="3D_transformations.gif", duration=100):
    images[0].save(output_path, save_all=True, append_images=images[1:], duration=duration, loop=0)
    print(f"GIF saved as {output_path}")

# Main execution
if __name__ == "__main__":
    # Read input files
    points = read_points(points_file)
    lines = read_lines(lines_file)

    # Static visualization
    width, height = 800, 800
    projected_points = project_points(points, width, height)
    image = Image.new("RGB", (width, height), "white")
    draw_lines(projected_points, lines, image)
    image.save("3D_initial.png")
    print("Initial 3D shape saved as 3D_initial.png")

    # Animated transformations
    frames = generate_frames(
        points, lines, num_frames=60, dx=2, dy=1, dz=0, 
        sx=1.01, sy=1.01, sz=1.01, rotation_angle=3, axis='y'
    )
    save_gif(frames)
