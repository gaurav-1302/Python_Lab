#15. Program that calculates the number of rectangular tiles required to cover a rectangular floor if the dimensions of the floor and the dimensions of a tile are entered by the user
a1 = int(input("Enter the length of floor: "))
b1 = int(input("Enter the breadth of floor: "))
a2 = int(input("Enter the length of tile: "))
b2 = int(input("Enter the breadth of tile: "))
area_f = a1*b1
area_t = a2*b2
print("Number of tiles required: ",(area_f/area_t))