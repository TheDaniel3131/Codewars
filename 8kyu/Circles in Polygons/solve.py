import math

def circle_diameter(sides, side_length): 
    return side_length / math.tan(math.pi / sides)


from math import tan, pi

def circle_diameter(s, s_l): 
    r = s_l / (2 * tan(pi / s))
    return 2 * r


from math import tan, pi


def circle_diameter(sides, side_length):
    """
    A Regular polygon (see: https://en.wikipedia.org/wiki/Regular_polygon)
    includes 360°/sides isosceles triangles.
    The height of an isosceles triangle divides its vertex angle into two equal angles.
    The tangent of this angle is the ratio of the half of the side of
    the regular polygon to the height of the isosceles triangle.
    And the height of an isosceles triangle is the radius of the circle inscribed in a regular polygon.
    Note that the tangent is computed in radians.
    """
    if type(sides) in (int, float) and type(side_length) in (int, float):
        if sides > 2:
            if side_length > 0:
                return round(side_length / tan(pi/sides), 3)
            else:
                raise ValueError("The side of a box should be a positive number!")
        else:
            raise ValueError("The minimum numbers of sides of a box should be 3!")
    else:
        raise ValueError("The parameters should be a number!")
        

        
from math import pi, sin, cos

def circle_diameter(sides, side_length):
    deg = pi / sides
    return side_length * cos(deg) / sin(deg)