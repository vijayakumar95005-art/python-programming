balance=5000
password=9500
while True:
    print("1.Deposit\n2.Withdrawal \n3.Check Balance \n4.Exit")
    choice=int(input())
    if choice==1:
        amount=int(input("Enter the Depoist Amount:"))
        balance+=amount
        print(f"Amount {amount} Successfully Deposited in your Account")
    elif choice==2:
        pin=int(input("Enter the Pin:"))
        if pin==password:
            amount=int(input("Enter your Amount:"))
            balance-=amount
            print(f"Amount {amount} debited from your Account")
        else:
            print("Pin is Incorrect")
    elif choice==3:
        print("Balance:",balance)
    elif choice==4:
        print("Thank You")
        break
    else:
        print("Invalid choice")

