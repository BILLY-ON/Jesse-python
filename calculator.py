while True:
    print("Python Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    
    f1=int(input("\nEnter the first number:"))
    f2=int(input("\nEnter the second number:"))
    
    
    choice=int(input("\nPlease Enter the operation you wish to perfom select between 1-5\n"))
    if choice==5:
        print(f"The exponential is: {f1**f2:.6f}")
        break
    if choice==1:
        print(f"The sum of the two numbers is {f1+f2}")
        break
    if choice==2:
        print(f"The difference between the two numbers is: {f1-f2}")
        break
    if choice==3:
        print(f"The product of the two numbers is: {f1*f2}")
        break
    if choice==4:
        try:
         print(f"The division of the two numbers is:{f1/f2}")
        except ZeroDivisionError:
            print("You cannot Divide a number by zero") 
        
        break
    else:
        print("Please enter a number between 1-5 to continue")


