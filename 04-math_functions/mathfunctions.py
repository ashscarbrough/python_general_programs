'''
Area of a pentagon
'''
from ast import literal_eval
import math

length = literal_eval(input("Enter the distance from the length from the center to the vertex: "))

side = (2*length) * math.sin(math.pi/5)
area = ((3*math.sqrt(3))/2) * pow(side, 2)

print("The area of the pentagon is: ", area)
