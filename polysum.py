import math

def polysum(n, s):
    '''
    n: integer, number of sides
    s: integer or float, length of each side
    
    returns: float, sum of area + (perimeter^2), rounded to 4 decimals
    '''
    
    # Calculate Area
    area = (0.25 * n * s**2) / math.tan(math.pi / n)
    
    # Calculate Perimeter
    perimeter = n * s
    
    # Sum the area and the square of the perimeter
    result = area + (perimeter ** 2)
    
    # Round to 4 decimal places
    return round(result, 4)