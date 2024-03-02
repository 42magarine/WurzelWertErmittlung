import csv
import os
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def count_points_in_radius(file_path_1, folder_path_2, radius, x_col_name, y_col_name):
    points = []

    # Lese Koordinaten aus erster Datei ein
    with open(file_path_1, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Überspringe Header (falls vorhanden)
        header = next(csv_reader, None)
        x_col_index = header.index(x_col_name)
        y_col_index = header.index(y_col_name)

        for row in csv_reader:
            x1, y1 = map(float, [row[x_col_index], row[y_col_index]])

            # Füge Koordinaten zur Liste hinzu
            points.append((x1, y1, 0))  # Der dritte Wert ist die Anzahl der gefundenen Punkte

    # Zähle Punkte in Radius aus den Dateien im Ordner
    for filename in os.listdir(folder_path_2):
        if filename.startswith("baum_") and filename.endswith(".csv"):
            file_path_2 = os.path.join(folder_path_2, filename)

            with open(file_path_2, 'r', newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)

                # Überspringe Header (falls vorhanden)
                header_2 = next(csv_reader, None)

                # Definiere x_col_index und y_col_index für die baum_datei
                x_col_index_2 = header_2.index(x_col_name) if x_col_name in header_2 else None
                y_col_index_2 = header_2.index(y_col_name) if y_col_name in header_2 else None

                for row in csv_reader:
                    # Überprüfe, ob die erforderlichen Spalten vorhanden sind
                    if x_col_index_2 is not None and y_col_index_2 is not None:

                        x2, y2 = map(float, [row[x_col_index_2], row[y_col_index_2]])
                        print(x2, y2)
                        # Überprüfe, ob die Distanz innerhalb des Radius liegtsldso
                        for i, (x1, y1, count) in enumerate(points):
                            if calculate_distance(x1, y1, x2, y2) <= radius:
                                points[i] = (x1, y1, count + 1)

    # Gebe die Koordinaten aus der ersten Datei und die Anzahl der gefundenen Punkte aus
    # for x, y, count in points:
        # print(f"Koordinate: ({x}, {y}), Anzahl der gefundenen Punkte im Radius: {count}")

# Beispielaufruf
file_path_1 = 'bodenrichtwerte.csv'  # Passe dies an den tatsächlichen Dateinamen an
folder_path_2 = 'trees'  # Passe dies an den tatsächlichen Ordnerpfad an
radius = 250
x_col_name = 'X-Koordinate'  # Passe dies an den tatsächlichen Spaltennamen an
y_col_name = 'Y-Koordinate'  # Passe dies an den tatsächlichen Spaltennamen an

count_points_in_radius(file_path_1, folder_path_2, radius, x_col_name, y_col_name)
