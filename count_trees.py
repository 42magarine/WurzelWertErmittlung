import csv
import os
import math

# Calculate the distance between two points (a² + b² = c²)
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate a custom value (WurzelWert) based on the number of trees and the land value
def division(baume, bodenwert):
    if baume != 0 and bodenwert != 0:
        wurzelwert = math.log(baume / bodenwert)
    else:
        wurzelwert = 0
    return wurzelwert

# Find the land value (Bodenwert) for the closeset land value point
def shortest_distance(x1, y1, comparison_points):
    shortest_distance = float('inf')
    bodenwert = 0
    for comparison_point in comparison_points:
        x2, y2, wert = comparison_point
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        # If a closer point is found, update the shortest distance and land value
        if distance < shortest_distance:
               bodenwert = wert
               shortest_distance = distance

    return bodenwert

# Function to read coordinates and land values from a CSV file
def read_coordinates_from_file(file_path, x_col_name, y_col_name, boden_col_name):
    points = []

    # Read the CSV file
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Skip the header row and get the indices of the required columns
        header = next(csv_reader, None)
        x_col_index = header.index(x_col_name)
        y_col_index = header.index(y_col_name)
        bodenwert_index = header.index(boden_col_name)
        nutzen_index = header.index("Art der Nutzung")

        for row in csv_reader:
            x1, y1, wert = map(float, [row[x_col_index], row[y_col_index], row[bodenwert_index]])
            # Add the point to the list
            points.append((x1 / 1000, y1 / 1000, wert))

    return points

# Count the number of points (trees) within a given radius from each point in the point cloud
def count_points_in_radius(folder_path, radius, x_col_name, y_col_name, points):

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path_2 = os.path.join(folder_path, filename)
        print(file_path_2)
        with open(file_path_2, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)

            # Skip the header row and get the indices of the required columns
            header_2 = next(csv_reader, None)
            x_col_index_2 = header_2.index(x_col_name)
            y_col_index_2 = header_2.index(y_col_name)

            # Read each row and check if the point is within the radius
            for row in csv_reader:
                x2, y2 = map(float, [row[x_col_index_2], row[y_col_index_2]])

                for point in points:
                    if calculate_distance(point[0], point[1], x2 / 1000, y2 / 1000) <= radius:
                        point[2] += 1
