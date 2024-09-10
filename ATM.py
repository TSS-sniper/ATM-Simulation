#A simple Program to Simulate ATM
def main():
    print("Welcome to the ATM!")
    password=1234
    transaction_history=[]
    pin=int(input("Enter your ATM pin: "))
    balance=0

    if pin==password:
        while True:
            print("""
                1 ==> Check balance
                2 ==> Withdraw balance
                3 ==> Deposit balance
                4 ==> Change pin
                5 ==> View Transaction History
                6 ==> Exit
                """)
            try:
                option=int(input("Please Enter your Choice : "))
            except:
                print("Invalid input")
            
            if option==1:
                print(f"Your current balance is ₹{balance}")
                transaction_history.append("Balance inquiry")
            elif option==2:
                withdraw_amt=int(input("Please enter the Withdrawing Amount: "))
                if withdraw_amt>balance:
                    print("Insufficient Balance")
                    transaction_history.append(f"Insufficient Balance")
                else:
                    balance=balance-withdraw_amt
                    print(f"₹{withdraw_amt} is debited from your Account\nYour current Balance is ₹{balance}")
                    transaction_history.append(f"Cash withdrawal: ₹{withdraw_amt}")
            elif option==3:
                deposit_amt=int(input("Please enter the Depositing Amount: "))
                balance=balance+deposit_amt
                print(f"₹{deposit_amt} is credited to your Account\nYour updated Balance is ₹{balance}")
                transaction_history.append(f"Cash deposited: ₹{deposit_amt}")
            elif option==4:
                check=int(input("Enter your current pin: "))
                if pin==check:
                    new_pin=int(input("Enter your new pin: "))
                    pin=new_pin
                    print("PIN changed Succesfully.")
                    transaction_history.append("PIN Change")
                else:
                    print("Access denied")
            elif option==5:
                print("\nTransaction History:\n")
                print("*"*19,"HISTORY","*"*19)
                for i in transaction_history:
                    print(i)
                print("*"*47)
                transaction_history.append("Viewed Transaction History")
            elif option==6:
                print("Thank you for using the ATM!")
                transaction_history.append("Exited the ATM")
                break
            else:
                print("Invalid Choice")
                print("Please Enter Correct Choice...")
    else:
        print("Entered pin is wrong.")

if __name__ == "__main__":
    main()