# Main program
from count_trees import count_points_in_radius
from point_cloud import generate_point_cloud, plot_point_cloud, plot_gradient_map

if __name__ == "__main__":
    file_path_1 = 'bodenrichtwerte.csv'
    folder_path = 'trees'
    x_col_name = 'X-Koordinate'
    y_col_name = 'Y-Koordinate'
    radius = 200000

    points = count_points_in_radius(file_path_1, folder_path, radius, x_col_name, y_col_name)

    polygon, point_cloud = generate_point_cloud("punkte_heilbronn.csv", 500)
    plot_point_cloud(polygon, points)
    # plot_gradient_map(polygon, point_cloud)
    
