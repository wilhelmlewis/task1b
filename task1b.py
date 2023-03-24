import math

# prompt user for parameters of polygon
num_sides = eval(input("Enter the number of sides: "))
side_length = eval(input("Enter the length of each side: "))

# do math
area = num_sides * math.pow(side_length, 2) / (4 * math.tan(math.pi / num_sides))
result = round(area, 5)

# show output to user
print("The area of this polygon is approximately: " + str(result))