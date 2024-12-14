import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Input File txt
points_file = "ScriptPrimtif2D/point3D.txt"
lines_file = "ScriptPrimtif2D/lines3D.txt"

# Read Points
def read_points(file_path):
    points = []
    with open(file_path, "r") as file:
        for line in file:
            x, y, z = map(int, line.strip().split(','))
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

# Read file input
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
    translated_points = [(x, y, z) for x, y, z in translated_points[:3].T]

    return translated_points

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
    scaled_points = [(x, y, z) for x, y, z in scaled_points[:3].T]

    return scaled_points

# Rotate Function (Around Z-Axis)
def rotateFunc(points, angle_degrees, axis='z', rotation_center=(0, 0, 0)):
    angle_radians = np.radians(angle_degrees)
    cx, cy, cz = rotation_center

    # Translation into the origin
    T_to_origin = np.array([
        [1, 0, 0, -cx],
        [0, 1, 0, -cy],
        [0, 0, 1, -cz],
        [0, 0, 0, 1]
    ])

    # Rotation Matrix
    if axis == 'z':
        R = np.array([
            [np.cos(angle_radians), -np.sin(angle_radians), 0, 0],
            [np.sin(angle_radians), np.cos(angle_radians), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    elif axis == 'x':
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

    # Translation back
    T_back = np.array([
        [1, 0, 0, cx],
        [0, 1, 0, cy],
        [0, 0, 1, cz],
        [0, 0, 0, 1]
    ])

    # Combination Transformation
    transform_matrix = T_back @ R @ T_to_origin

    points_homogeneous = np.array([[x, y, z, 1] for x, y, z in points]).T
    rotated_points = transform_matrix @ points_homogeneous
    rotated_points = [(x, y, z) for x, y, z in rotated_points[:3].T]

    return rotated_points

# Draw Line in 3D
def drawLine3D(points, lines, ax):
    for start, end in lines:
        x_coords = [points[start][0], points[end][0]]
        y_coords = [points[start][1], points[end][1]]
        z_coords = [points[start][2], points[end][2]]
        ax.plot(x_coords, y_coords, z_coords, color='red')

# Generate Transformation Animation
def transformationsGeo3D(points, lines, num_frames=60, dx=0, dy=0, dz=0, sx=1.0, sy=1.0, sz=1.0, rotation_angle=0, rotation_axis='z', rotation_center=(0, 0, 0)):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for frame in range(num_frames):
        ax.clear()
        ax.set_xlim([-200, 200])
        ax.set_ylim([-200, 200])
        ax.set_zlim([-200, 200])

        translated_points = translationFunc(points, dx * frame, dy * frame, dz * frame)
        scaled_points = scaleFunc(translated_points, sx ** frame, sy ** frame, sz ** frame)
        rotated_points = rotateFunc(scaled_points, rotation_angle * frame, rotation_axis, rotation_center)

        drawLine3D(rotated_points, lines, ax)
        plt.pause(0.1)

    plt.show()

# Static Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-200, 200])
ax.set_ylim([-200, 200])
ax.set_zlim([-200, 200])
drawLine3D(points, lines, ax)
plt.show()

# Animated Transformations
transformationsGeo3D(points, lines, num_frames=60, dx=2, dy=1, dz=0, sx=1.01, sy=1.01, sz=1.01, rotation_angle=3, rotation_axis='y', rotation_center=(100, 100, 0))
