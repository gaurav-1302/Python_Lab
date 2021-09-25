# Program to find the hypotenuse of a right angled triangle, when the base and height are entered by the user.
a = float(input("Enter the base : "))
b = float(input("Enter the height : "))
c = ((a*a) + (b*b))**0.5 #or can use in build function math.sqrt()
print(f"hypotenuse of triangle with base {a} ,and height {b} is ",c)
