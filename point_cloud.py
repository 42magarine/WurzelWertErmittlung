import csv

def extract_boundry_from_csv(file_path):
    x_values = []
    y_values = []
    
    #the file needs to be a simple csv, like this
    # x,y
    # 508588.91... ,5450792.26...
    # 508732.80... ,5450651.16...
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            x_values.append(float(row[0]))
            y_values.append(float(row[1]))

    return x_values, y_values


from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt

def generate_point_cloud(file_path, distance_between_points):
    x_values, y_values = extract_boundry_from_csv(file_path)
    polygon = Polygon(zip(x_values, y_values))
    
    point_cloud = []
    next_point = Point(polygon.bounds[0], polygon.bounds[1])
    i = 0;
    while next_point.y < polygon.bounds[3]:
        while next_point.x < polygon.bounds[2]:
            if polygon.contains(next_point):
                point_cloud.append(next_point)
            next_point = Point(next_point.x + distance_between_points, next_point.y)
        next_point = Point(polygon.bounds[0], next_point.y + distance_between_points)
    return polygon, point_cloud
    

def plot_point_cloud(polygon, point_cloud):
    x, y = polygon.exterior.xy

    plt.plot(x, y, color='blue', label='Custom Polygon')
    plt.fill(x, y, color='lightgray', alpha=0.5)

    # x = [point.x for point in point_cloud]
    # y = [point.y for point in point_cloud]

    x = [point[0] / 1000 for point in point_cloud]
    y = [point[1] / 1000 for point in point_cloud]
    count_trees = [point[2] for point in point_cloud]
    print(count_trees)
    scatter = plt.scatter(x, y, c=count_trees, cmap='viridis')
    # plt.scatter(x, y, color='blue', label='Point Cloud')


    # Add labels and show the plot
    cbar = plt.colorbar(scatter)
    cbar.set_label('Trees')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Custom Polygon')
    # plt.legend()
    plt.show()

from matplotlib.patches import PathPatch
from matplotlib.path import Path
from numpy import np

def plot_gradient_map(polygon, point_cloud):
    polygon_vertices = np.array(polygon.boundary.xy).T
    
    polygon_path = Path(polygon_vertices)
    polygon_patch = PathPatch(polygon_path, facecolor="none", edgecolor="black")
    
    fig, ax = plt.subplots()
    ax.add_patch(polygon_patch)
    