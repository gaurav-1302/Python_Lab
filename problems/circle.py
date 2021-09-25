# Program to find the area and circumference of a circle, when the radius is entered by the user. However, the user can input radius in integer or float.

a = float(input("Enter the radius: "))
c = (2*(22/7))*a #for circumference
d = ((22/7)*a)*a #for area

print(f"""perimeter of circle with radius {a} is - """,c)
print(f"""area of circle with radius {a} is - """,d)