def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test_value = min(a, b)
    
    while test_value > 0:
        if a % test_value == 0 and b % test_value == 0:
            return test_value        
        test_value -= 1