def is_inside_area(x, y):
    # Define the bounding coordinates for the area
    x_min, y_min = 502481.266, 5437546.859
    x_max, y_max = 522194.589, 5451251.841

    # Check if the coordinates are inside the specified area
    return x_min <= x <= x_max and y_min <= y <= y_max


def get_coordinates():
    try:
        # Get x and y coordinates as input from the user
        print("X-Min: 502481   X-Max: 522194")
        print("Example X: 516815")
        x = float(input("Enter the x coordinate: "))
        print("Y-Min: 5437546   Y-Max: 5451251")
        print("Example X: 5442613")
    
        y = float(input("Enter the y coordinate: "))
        return x, y
    except ValueError:
        print("Invalid input. Please enter numerical values for coordinates.")
        return get_coordinates()

# Main program
if __name__ == "__main__":
    # Get coordinates from the user
    x_coord, y_coord = get_coordinates()

    # Display the coordinates
    print(f"Entered coordinates: ({x_coord}, {y_coord})")
