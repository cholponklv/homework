import math

diameter = float(input("Enter the diameter of the sphere in metres: "))
radius = diameter / 2
volume = (4/3) * math.pi * (radius ** 3)
print(f"The volume of the sphere is {volume} cubic metres")