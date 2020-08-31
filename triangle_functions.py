#Carina Tam and Kinza Ali
import math
def first_number():
    """()->float
    Asks users to input the first side length of the triangle,
    and return the first side length of the triangle

    """
    a=float(input("Enter the first side length: "))
    return a
            

def second_number():
    """()->float
    Asks users to input the second side length of the triangle,
    and return the second side length of the triangle

    """
    b=float(input("Enter the second side length: "))
    return b

def third_number():
    """()->float
    Asks users to input the third side length of the triangle,
    and return the third side length of the triangle

    """
    c=float(input("Enter the third side length: "))
    return c

def is_triangle(a, b, c):
    """(number, number, number)->bool
    The parameter refers to the 3 side lengths of the triangle.
    The function will return true if 3 side lengths can form a triangle,
    and false if 3 side lengths cannot form a triangle

    >>> is_triangle(1, 3, 3)
    True

    >>> is_triangle(1, 2, 56)
    False
    """
    if(max(a,b,c)==a):
        if(b+c>a):
            return True
        else: return False
    elif(max(a,b,c)==b):
        if(a+c>b):
            return True
        else:
            return False
    else:
        if(a+b>c):
            return True
        else:
            return False

def triangle_type(a, b, c):
    """(number, number, number)->str
    The parameter refers to the 3 side lengths of the triangle.
    The function will return “scalene” if it is a scalene triangle,
    “isosceles” if it is an isosceles triangle, and “equilateral”
    if it is an equilateral triangle

    >>> triangle_type(3, 4, 5)
    'scalene'

    >>> triangle_type(2, 2, 3)
    'isosceles'

    >>> triangle_type(10, 10, 10)
    'equilateral'
    """
    if(a==b==c):
        return "equilateral"
    if(a==b and b!=c or a==c and c!=b or b==c and c!=a):
        return "isosceles"
    if(a!=b and b!=c and a!=c):
        return "scalene"

def is_right_angle(a, b, c):
    """(number, number, number)->bool
    The parameter refers to the 3 side lengths of the triangle.
    The function will return true if it is a right angle,
    otherwise the function will return false if it is not a right triangle

    >>> is_right_angle(6, 8, 10)
    True
    
    >>> is_right_angle(5, 6, 7)
    False
    """
    if(a>b and a>c):
        temp=c
        c=a
        a=temp
    if(b>a and b>c):
        temp=c
        b=a
        b=temp
    if(c>a and c>b):
        if(a**2+b**2==c**2):
            return True
    return False


def triangle_angle(a, b, c):
    """(number, number, number)->float
    The parameter refers to the 3 side lengths of the triangle.
    The function will return the angle (in degree) opposite to the length a in
    2 decimal places

    >>> triangle_angle(2, 3, 4)
    28.96

    >>> triangle_angle(12, 15, 17)
    43.49

    """
    x=math.acos((b**2+c**2-a**2)/(2*b*c))*180/math.pi
    x=round(x,2)
    return x
    
    

def angle_type(a1, a2, a3):
    """(angle, angle, angle)->int
    The parameter refers to the 3 angles (in degrees) of the triangle.
    The function will return “acute” if it is an acute triangle,
    “obtuse” if it is an obtuse triangle,
    and “right” if it is an right triangle

    >>> angle_type(60, 60, 60)
    'acute'

    >>> angle_type(20, 30, 130)
    'obtuse'

    >>> angle_type(45, 45, 90)
    'right'
    """
    if(max(a1,a2,a3)<90):
        return "acute"
    elif(max(a1,a2,a3)>90):
        return "obtuse"
    elif(max(a1,a2,a3)==90):
        return "right"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
