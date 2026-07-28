PI = 3.14159

radius = float(input("Radius : "))
diameter = round((2 * radius), 2)
circumference = round((2 * PI * radius), 2)
area = round((PI * pow(radius, 2)), 2)

print(f"Diameter : {diameter}")
print(f"Circumference : {circumference}")
print(f"Area : {area}")
