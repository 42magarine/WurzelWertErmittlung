import csv
import os
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def division(baume, bodenwert):
    if bodenwert != 0:
        wurzelwert = baume / bodenwert
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

        for row in csv_reader:
            x1, y1, wert = map(float, [row[x_col_index], row[y_col_index], row[bodenwert]])

            # Füge Koordinaten zur Liste hinzu
            points.append((x1 / 1000, y1 / 1000, wert)) 
            print("hello")
            # Der dritte Wert ist die Anzahl der gefundenen Punkte

    return points


def count_points_in_radius(folder_path, radius, x_col_name, y_col_name, point):

    # Zähle Punkte in Radius aus den Dateien im Ordner
    count = 0;
    for filename in os.listdir(folder_path):
        file_path_2 = os.path.join(folder_path, filename)

        with open(file_path_2, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)

            # Überspringe Header (falls vorhanden)
            header_2 = next(csv_reader, None)
            x_col_index_2 = header_2.index(x_col_name)
            y_col_index_2 = header_2.index(y_col_name)

            for row in csv_reader:
                x2, y2 = map(float, [row[x_col_index_2], row[y_col_index_2]])
                # print(x2, y2)
                # Überprüfe, ob die Distanz innerhalb des Radius liegt
                if calculate_distance(point.x, point.y, x2 / 1000, y2 / 1000) <= radius:
                    count += 1

    # Gebe die Koordinaten aus der ersten Datei und die Anzahl der gefundenen Punkte aus
    # for x, y, count in points:
    #     print(f"Koordinate: ({x}, {y}), Anzahl der gefundenen Punkte im Radius: {count}")
    return count
