'''
Determine the area and volume of a cylinder
'''
from ast import literal_eval
import math

radius, length = literal_eval(input("Please provide a cylinder radius and a length:"))

area = radius * radius * math.pi
volume = area * length

print("The cylinder has an area of", round(area, 4))
print("The volume of the cylindar is", round(volume, 1), ".")
