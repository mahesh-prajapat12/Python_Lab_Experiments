import math

# Input coordinates of point 1
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Input coordinates of point 2
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Compute distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Print result
print(f"Distance between the two points: {distance:.2f}")
