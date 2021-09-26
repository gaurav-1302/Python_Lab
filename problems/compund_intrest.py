#14. Program to find the Compound Interest compounded annually and the total amount when the Principal, Rate of Interest and Time are entered by the user.
pa = int(input("Enter the principal amount: "))
r = int(input("Enter the rate of intrest: "))
t = int(input("Enter the time period: "))
n = int(input("Enter the number of times interest applied per time period: "))

CI = pa*((1+((r/100)/n))**(n*t))

print("Compound intrest is: ",(CI - pa))
print("Total amount is: ",(CI))