print("THIS IS THE ULTIMATE CALCULATOR FOR SOLVING 2 NUMBERS")
a =int(input("Enter first number: "))
b =int(input("Enter second number: "))
c =int(input("Enter \n1 for addition, \n2 for subtraction, \n3 for multiplication, \n4 for division: "))

if (c==1):
    print("The sum of", a, "and", b, "is", a+b)
elif (c==2):
    print("The difference of", a, "and", b, "is", a-b)  
elif (c==3):
    print("The product of", a, "and", b, "is", a*b)
elif (c==4):
    if (b==0):
        print("Division by zero is not allowed")
    else:
        print("The division of", a, "and", b, "is", a/b)
else:
    print("Invalid input")