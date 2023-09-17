def are_coordinates_on_same_side(x1, y1, x2, y2, coordinates):
    slope = (y2 - y1) / (x2 - x1)
    expected_y = y1 + slope * (x2 - x1)

    #placeholders
    above_line = True 
    below_line = True

    for xi, yi in coordinates:
        expected_yi = y1 + slope * (xi - x1)
        if yi > expected_yi:
            below_line = False
        elif yi < expected_yi:
            above_line = False

    return above_line or below_line

# Example usage:
x1, y1 = 0, 0
x2, y2 = 1, 1
coordinates = [[2, 2], [-1, -1], [3, 3], [-2, -2], [5,1], [5,4]]
result = are_coordinates_on_same_side(x1, y1, x2, y2, coordinates)
print(result)  
