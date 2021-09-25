#3. Program to find the Simple Interest and the total amount when the Principal, Rate of Interest and Time are entered by the user.
pa = int(input("Enter the principal amount: "))
r = int(input("Enter the rate of intrest: "))
t = int(input("Enter the time period: "))
SI = ((pa*r)*t)/100
print("Simple intrest is: ",SI)
print("Total amount is: ",(SI + pa))