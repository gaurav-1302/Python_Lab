#Program to find the area and perimeter of a rectangle, when the required input (Length and Breadth) are entered by the user.

a = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))
c = 2*(a+b) #for perimeter
d = a*b #for area
print(f"""perimeter of rectangle with legth {a} and bredth {b} is - """,c)
print(f"""area of rectangle with legth {a} and bredth {b} is - """,d)