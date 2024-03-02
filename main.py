from point_cloud import extract_boundry_from_csv 

def is_inside_area(x, y):
    # Define the bounding coordinates for the area
    x_min, y_min = 502481.266, 5437546.859
    x_max, y_max = 522194.589, 5451251.841

    # Check if the coordinates are inside the specified area
    if x_min <= x <= x_max and y_min <= y <= y_max:
        return
    else:
        raise ValueError("Input not inside area")


def get_coordinates():
    try:
        # Get x and y coordinates as input from the user
        print("X-Min: 502481   X-Max: 522194")
        print("Example X: 516815")
        x = float(input("Enter the x coordinate: "))
        print("Y-Min: 5437546   Y-Max: 5451251")
        print("Example X: 5442613")
    
        y = float(input("Enter the y coordinate: "))
        is_inside_area(x, y);
        return x, y
    except ValueError as e:
        print(f"Error: {e}")
        return get_coordinates()

# Main program
if __name__ == "__main__":
    # Get coordinates from the user
    # x_coord, y_coord = get_coordinates()

    # Display the coordinates
    # print(f"Entered coordinates: ({x_coord}, {y_coord})")
    
    x_values, y_values = extract_boundry_from_csv('punkte_heilbronn.csv')
    create_point_cloud(x_values, y_values)

