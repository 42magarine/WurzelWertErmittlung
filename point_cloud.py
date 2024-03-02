import csv

def extract_boundry_from_csv(file_path):
    x_values = []
    y_values = []
    
    #the file needs to be a simple csv, like this
    # x,y
    # 508588.91... ,5450792.26...
    # 508732.80... ,5450651.16...
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            # Assuming the x and y columns are the first and second columns in the CSV
            x, y = map(float, row[:2])

            # Round x and y to two decimal places
            x = round(x, 2)
            y = round(y, 2)

            x_values.append(x)
            y_values.append(y)

    return x_values, y_values