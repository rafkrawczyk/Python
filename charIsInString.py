def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        return char == aStr[0]
    mid_index = len(aStr) // 2
    mid_char = aStr[mid_index]
    
    if char == mid_char:
        return True
    elif char < mid_char:
        return isIn(char, aStr[:mid_index])
    else:
        return isIn(char, aStr[mid_index+1:])