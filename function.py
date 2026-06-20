import math
radius = int(input("What is the radius ?"))
degree = int(input("What is the degree"))

def area(radius,degree):
    return 0.5 * (radius ** 2) * degree

def arc(radius,degree):
    return radius * degree

area = area(radius,degree)
arc = arc(radius,degree)

print(f"The area is {area} and the arc is {arc }")
    