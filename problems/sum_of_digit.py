#2. Program to find the factorial of an entered number.

n = int(input("Enter the number."))

sum = 0
while (n != 0):
 
    sum = sum + int(n % 10)
    n = int(n/10)
 
    print(sum)
 
 

