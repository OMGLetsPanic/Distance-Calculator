''' This program is a calculator that will be used to determine the distance between
two points on a graph. The math module must be imported in order to for the program to utilize more advanced
math functions beyond basic arithmetic. '''

import math

''' User enters the (x,y) coordinates for both points on the graph. The x-coordinate represents its horizontal 
position while the y-coordinate represents its vertical position. '''

x_first = input("Enter the first point's x-coordinate: ")

y_first = input("Enter the first point's y-coordinate: ")

x_second = input("Enter the second point's x-coordinate: ")

y_second = input("Enter the second point's y-coordinate: ")


''' The "distance" variable represents the formula for Euclidean Distance. It employs the math.sqrt function that we
imported from the math module at the beginning of the source code. '''
distance = math.sqrt((float(x_second) - float(x_first))**2 + (float(y_second) - float(y_first))**2)


print("The distance between the points is:", distance)