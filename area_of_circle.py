import math

def calculate_circle_area(rad):
    print('calculating the area of the circle')
    return pow(rad, 2) * math.pi

print('area of circle with diameter', 2, 'is', round(calculate_circle_area(2), 2))
print('area of circle with diameter', 3, 'is', round(calculate_circle_area(3), 2))
print('area of circle with diameter', 4.5, 'is', round(calculate_circle_area(4.5), 2))