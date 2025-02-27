balance=100000
correct_pin=1234
attempts=3
def display_menu():
    """Display ATM service Menu"""
    print("1.Withdraw")
    print("2.Deposit")
    print("3.Check balance")
    print("4.Exit")
while attempts>0:
    try:
        entered_pin=input("\n Please Enter your PIN to proceed(4-digit pin)")
        if len(entered_pin) !=4 or not entered_pin.isdigit():
            raise ValueError("PIN must be 4 digits")
        
        if entered_pin==correct_pin:
            print("PIN accepted you can proceed!")
        else:
            attempts-=1
            print(f"Incorrect PIN please try again. You have {attempts} remaining")   
            if attempts==0:
                print("Account blocked.Please contact your Bank!!")
                exit()
    except ValueError as e:
        attempts-=1
        print(f"Invalid format:{e}.{attempts}attempts remaining")
        if attempts==0:
            print("Account Locked. Please contact your Bank")
            exit() 
            
                        
def handle_withdrawal(): 
    global balance 
    try:     
       choice=int(input("Please Enter your choice (1-4)" ))
       if choice==1:
        amount=float(input("Enter the Amount you wish to withdraw\n"))
       if amount>balance:
        print("Insufficinet Funds please deposit to your account")
       else:
        balance-=amount
        print(f"Confirm you have withdrawn ${amount:.2f}.Your new balance is ${balance:.2f}")
    except ValueError:
        print("Invalid Input Please Enter Number only")
    
def handle_deposit():
    global balance
    global choice
    try:      
       if choice==2:
          fdeposit=int(input("Please enter the amount you wish to Deposit\n"))
       if fdeposit<0:
          print("Enter a valid Sum to deposit")
       else:
          balance+=fdeposit
          print(f"You have Successfully deposited ${fdeposit:.2f}to your bank account.Your new bank account balance is${balance:.2f}") 
    except ValueError:
        print("Invalid Input Please Enter Number only")  
        
elif choice==3:
    print(f"Your Current Bank account balance is ${balance:.2f}")  
while True:   
    if choice==4:
     print("Thank you for Using our Banking system.Goodbye")
    break

else:
     print("Please an option (1-4)")
     
        




