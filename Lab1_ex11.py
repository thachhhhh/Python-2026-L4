import math
# Input coordinates for Point 1
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Input coordinates for Point 2
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"The distance between the two points is {distance:.2f}")