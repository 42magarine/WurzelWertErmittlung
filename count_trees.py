import csv
import os
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

import math

def division(baume, bodenwert):
    if bodenwert != 0 and baume != 0:
        wurzelwert = math.log(baume / bodenwert)
    else:
        wurzelwert = 0
    return wurzelwert


def shortest_distance(x1, y1, comparison_points):
    shortest_distance = float('inf')  # Set the shortest distance to infinity
    for comparison_point in comparison_points:
        x2, y2, wert = comparison_point
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        if distance < shortest_distance:
            bodenwert = wert
            shortest_distance = distance

    return bodenwert


def read_coordinates_from_file(file_path, x_col_name, y_col_name, boden_col_name):
    points = []

    # Lese Koordinaten aus der Datei ein
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Überspringe Header (falls vorhanden)
        header = next(csv_reader, None)
        x_col_index = header.index(x_col_name)
        y_col_index = header.index(y_col_name)
        bodenwert = header.index(boden_col_name)
        nutzen = header.index("Art der Nutzung")

        for row in csv_reader:
            # if row[nutzen] != "A" and "AB" and "F" and "GR" and "PG" and "WG":
                x1, y1, wert = map(float, [row[x_col_index], row[y_col_index], row[bodenwert]])

                # Füge Koordinaten zur Liste hinzu
                points.append((x1 / 1000, y1 / 1000, wert)) 
                # Der dritte Wert ist die Anzahl der gefundenen Punkte

    return points


from shapely.geometry import Point

def count_points_in_radius(folder_path, radius, x_col_name, y_col_name, points):

    # Zähle Punkte in Radius aus den Dateien im Ordner
    for filename in os.listdir(folder_path):
        file_path_2 = os.path.join(folder_path, filename)
        print(file_path_2)
        with open(file_path_2, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            # Überspringe Header (falls vorhanden)
            header_2 = next(csv_reader, None)
            x_col_index_2 = header_2.index(x_col_name)
            y_col_index_2 = header_2.index(y_col_name)
            for row in csv_reader:
                # print(row)
                x2, y2 = map(float, [row[x_col_index_2], row[y_col_index_2]])
                # print(x2, y2)
                # Überprüfe, ob die Distanz innerhalb des Radius liegt
                for point in points:
                    # print(point)
                    if calculate_distance(point[0], point[1], x2 / 1000, y2 / 1000) <= radius:
                        point[2] += 1
    # Gebe die Koordinaten aus der ersten Datei und die Anzahl der gefundenen Punkte aus
    # for x, y, count in points:
    #     print(f"Koordinate: ({x}, {y}), Anzahl der gefundenen Punkte im Radius: {count}")