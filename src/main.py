# Main program

from src.count_trees import count_points_in_radius, read_coordinates_from_file, shortest_distance, division
from src.point_cloud import generate_point_cloud, plot_point_cloud, plot_gradient_map
# from shapely.geometry import Point

if __name__ == "__main__":
    # Define file paths and parameters
    file_path = 'data/bodenrichtwerte.csv'		# CSV file containing land value data
    folder_path = 'data/trees/'					# Folder containing tree point data
    x_col_name = 'X-Koordinate'					# Column name for X coordinates in CSV
    y_col_name = 'Y-Koordinate'					# Column name for Y coordinates in CSV
    boden_col_name = 'Bodenrichtwert'			# Column name for land value in CSV
    point_density = 500							# Distance between points in the generated point cloud
    radius = 500								# Radius for counting points

    # Generate a polygon and point cloud from a CSV file
    polygon, point_cloud = generate_point_cloud("data/punkte_heilbronn.csv", point_density)

    # Read land value points from the CSV file
    bodenwert_points = read_coordinates_from_file(file_path, x_col_name, y_col_name, boden_col_name)

    # Count the number of points (trees) within a given radius for each point in the point cloud
    count_points_in_radius(folder_path, radius, x_col_name, y_col_name, point_cloud)

    # Calculate a custom value (WurzelWert) based on the number of trees and the closest land value
    for point in point_cloud:
        closest_bodenwert = shortest_distance(point[0], point[1], bodenwert_points)
        point[3] = division(point[2], closest_bodenwert)
        print(point)

    # Plot the point cloud with the calculated values
    plot_point_cloud(polygon, point_cloud)
    # plot_gradient_map(polygon, point_cloud)
