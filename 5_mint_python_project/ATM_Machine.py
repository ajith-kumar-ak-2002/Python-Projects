#ATM Machine Python Project


Balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        print(f"Your Current Balance is: ${Balance}")

    elif choice == 2:
        amount = float(input("Enter the amount to deposit: $"))
        Balance += amount
        print(f"${amount} has been deposited. Your New Balance is: ${Balance}")

    elif choice == 3:
        amount = float(input("Enter the amount to Withdraw: $"))

        if amount <= Balance:
            Balance -= amount
            print(f"${amount} has been withdrawn. Your New Balance is: ${Balance}")
        else:
            print("Insufficient funds. Please check Your balance and try again..... ")