from math import pi


def get_area(length,width):
    """
    Returns area given length and width
    Requires int or float inputs >= 0
    Returns -1 if incorrect types are given
    """
    if not isinstance(length,(int,float)) or not isinstance(width,(int,float)):
        return -1
    if isinstance(length,bool) or isinstance(width,bool):
        return -1
    if length < 0 or width < 0:
        return -1
    
    return length * width


def get_circumference(radius):
    if not isinstance(radius,(int,float)):
        return -1
    if isinstance(radius,bool):
        return -1
    if radius < 0:
        return -1
    return 2 * radius * pi


print(get_circumference(5))