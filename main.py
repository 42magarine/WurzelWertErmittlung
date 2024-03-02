# Main program
from count_trees import count_points_in_radius
from point_cloud import generate_point_cloud, extract_boundry_from_csv

if __name__ == "__main__":
    file_path_1 = 'bodenrichtwerte.csv'
    folder_path = 'trees'
    x_col_name = 'X-Koordinate'
    y_col_name = 'Y-Koordinate'
    radius = 250000

    count_points_in_radius(file_path_1, folder_path, radius, x_col_name, y_col_name)

    x_values, y_values = extract_boundry_from_csv('punkte_heilbronn.csv')
    generate_point_cloud(x_values, y_values)
    
