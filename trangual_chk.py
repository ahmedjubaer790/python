x=float(input("Enter the value of x: "))
y=float(input("Enter the value of y: "))
z=float(input("Enter the value of z: "))

if x==y==z:
    print('Its an equilateral triangle')
elif x==y or y==z or x==z:
    print('Its an isosceles triangle')
else:
    print('Its a scalene triangle')