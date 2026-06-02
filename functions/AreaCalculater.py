'''
    Area Calculator - Write functions to calculate area of circle, rectangle, and triangle 
'''
import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

# random samples

circle_radius = 5
rectangle_length = 10
rectangle_width = 4
triangle_base = 8
triangle_height = 6 

print("Area of circle with radius", circle_radius, "is:", calculate_circle_area(circle_radius))
print("Area of rectangle with length", rectangle_length, "and width", rectangle_width, "is:", calculate_rectangle_area(rectangle_length, rectangle_width))
print("Area of triangle with base", triangle_base, "and height", triangle_height, "is:", calculate_triangle_area(triangle_base, triangle_height))
