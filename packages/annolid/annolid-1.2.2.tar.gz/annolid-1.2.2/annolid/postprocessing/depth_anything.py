import argparse
import cv2
import numpy as np
import onnxruntime as ort
from transform import load_image
# Visualize point cloud
import matplotlib.pyplot as plt
# from vtk import vtkDataSet, vtkPointData, vtkPoints, vtkPolyData, vtkXMLUnstructuredGridWriter
import csv
import json
from shapely.geometry import Point, Polygon


def point_in_polygon(point, polygon):
    point = Point(point)
    polygon = Polygon(polygon)
    return polygon.contains(point)


def load_shapes_from_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
    shapes = data['shapes']
    return shapes


def save_point_cloud_to_csv(point_cloud, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y', 'z', 'label'])  # header row
        for point in point_cloud:
            writer.writerow(list(point))  # save point coordinates and label


def infer_depth(image, model_path, orig_w, orig_h):
    session = ort.InferenceSession(
        model_path, providers=["CUDAExecutionProvider", "CPUExecutionProvider"])
    depth = session.run(None, {"image": image})[0]
    depth = cv2.resize(depth[0, 0], (orig_w, orig_h))
    return depth


def generate_point_cloud(depth_map, json_file_path):
    height, width = depth_map.shape[:2]
    u, v = np.meshgrid(np.arange(width), np.arange(height))
    x = (u - width/2) / width
    y = (v - height/2) / height
    z = depth_map / np.max(depth_map)  # Scale depth values to [0, 1]
    point_cloud = np.dstack((x, y, z))
    point_cloud = point_cloud.reshape(-1, 3)

    # Load shapes from JSON file
    shapes = load_shapes_from_json(json_file_path)

    # Add shape information
    # Initialize with default label
    shape_labels = np.zeros((len(point_cloud), 1), dtype=object)

    for shape in shapes:
        points = shape['points']
        label = shape['label']
        # Rescale points in shape to [0, 1] range
        points = np.array(points)
        points[:, 0] = (points[:, 0] - width/2) / width
        points[:, 1] = (points[:, 1] - height/2) / height
        for i, point in enumerate(point_cloud):
            if point_in_polygon(point[:2], points):
                shape_labels[i] = label

    point_cloud = np.concatenate((point_cloud, shape_labels), axis=1)
    return point_cloud


def visualize_point_cloud(rgb_image, point_cloud):
    print(point_cloud)
    # Calculate new size based on point cloud shape
    new_size = (point_cloud.shape[0], 3)
    rgb_image = cv2.resize(rgb_image, (new_size[0], 1))  # Resize rgb_image
    rgb_image_normalized = np.clip(rgb_image.astype(np.float32) / 255.0, 0, 1)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(point_cloud[:, 0], point_cloud[:, 1],
               point_cloud[:, 2], c=rgb_image_normalized.reshape(point_cloud.shape[0], 3), s=1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


def save_point_cloud_to_vtu(point_cloud, filename):
    # Create a vtkPoints object to store the point cloud data
    points = vtkPoints()

    # Add the point cloud data to the vtkPoints object
    for x, y, z in point_cloud:
        points.InsertNextPoint(x, y, z)

    # Create a vtkPolyData object to store the point cloud data
    poly_data = vtkPolyData()
    poly_data.SetPoints(points)

    # Create a vtkXMLUnstructuredGridWriter object to write the VTU file
    writer = vtkXMLUnstructuredGridWriter()
    writer.SetFileName(filename)
    writer.SetInputData(poly_data)
    writer.Write()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--img",
        type=str,
        required=True,
        help="Path to input image.",
    )
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="Path to ONNX model.",
    )
    parser.add_argument(
        "--viz", action="store_true", help="Whether to visualize the results."
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    img_path = args.img
    model_path = args.model
    visualize = args.viz

    image, (orig_h, orig_w) = load_image(img_path)
    depth_map = infer_depth(image, model_path, orig_w, orig_h)
    point_cloud = generate_point_cloud(
        depth_map, img_path.replace('.png', '.json'))
    # save_point_cloud_to_vtu(point_cloud, 'point_cloud.vtu')
    save_point_cloud_to_csv(point_cloud, 'mouse_point_cloud.csv')
    if visualize:
        visualize_point_cloud(image, point_cloud)
