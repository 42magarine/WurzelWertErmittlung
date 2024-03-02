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


import numpy as np
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

    x = [point[0] for point in point_cloud]
    y = [point[1] for point in point_cloud]

    plt.scatter(x, y, color='blue', label='Point Cloud')

    # Add labels and show the plot
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Custom Polygon')
    plt.legend()
    plt.show()

