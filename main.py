# Main program
from count_trees import count_points_in_radius, read_coordinates_from_file, shortest_distance, division
from point_cloud import generate_point_cloud, plot_point_cloud, plot_gradient_map
from shapely.geometry import Point

if __name__ == "__main__":
    file_path = 'bodenrichtwerte.csv'
    folder_path = 'trees'
    x_col_name = 'X-Koordinate'
    y_col_name = 'Y-Koordinate'
    boden_col_name = 'Bodenrichtwert'
    radius = 200000

    polygon, point_cloud = generate_point_cloud("punkte_heilbronn.csv", 500)
    bodenwert_points = read_coordinates_from_file(file_path, x_col_name, y_col_name, boden_col_name)
    print(bodenwert_points)
    point_cloud_with_value = []
    for point in point_cloud:
        closest_bodenwert = shortest_distance(point.x, point.y, bodenwert_points)
        print("Bodenwert: " + str(closest_bodenwert))
        count_trees = count_points_in_radius(folder_path, radius, x_col_name, y_col_name, point)
        print("Count " + str(count_trees))
        point_cloud_with_value.append(Point(point.x, point.y, division(count_trees, closest_bodenwert)))
        
    # print(point_cloud_with_value)
    plot_point_cloud(polygon, point_cloud_with_value)
    # plot_gradient_map(polygon, point_cloud)
    
