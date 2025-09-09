# 3. Write a program that takes the radius of a sphere (a floating-point number) as input and
# then outputs the sphere’s diameter, circumference, surface area, and volume.
import math as m
radius = float(input("Input radius ? "))
d = radius*radius
circum = 2*m.pi*radius
area = 4*m.pi*radius*radius
vol = (4/3)*m.pi*d*radius
print("the sphere’s diameter", d)
print("the sphere’s circumference", circum)
print("the sphere’s circumference", area)
print("the sphere’s circumference", vol)


