# 1. Program to find the maximum of the three entered numbers.

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))

if a > b and a > c:
    print(f"{a} is greatest number.")

elif b > a and b > c:
    print(f"{b} is greatest number.")

elif c > a and c > a:
    print(f"{c} is greatest number.")
