# 2. Program to input the centre of a circle, radius of the circle and an arbitrary point P(x,y) and determine whether the point is inside the circle, on the circle or outside the circle.

x,y = int(input("Enter the x coordinate of centre of circle: ")),int(input("Enter the y coordinate of centre of circle: "))
radi = int(input("Enter the radius of circle: "))
a,b = int(input ("Enter the x cordinate of postion of point: ")),int(input("Enter the y cordinate of postion of point: ")) 

if a-x == radi and b-y == radi:
    print(f"The point {a},{b} lies on the circle. ")

elif a-x < radi and b-y < radi:
    print(f"The point {a},{b} lies inside the circle. ")

elif a-x > radi and b-y > radi:
    print(f"The point {a},{b} lies out the circle. ")

else:
    print(f"The point {a},{b} lies out the circle. ")



