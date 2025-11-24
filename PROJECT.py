print("========== WELCOME TO THE ATM MACHINE ==========\n")



#Default PIN and Balance

pin = "1234"

balance = 5000


EnteredPIN = input("Please enter your 4 digit ATM PIN: ")



if EnteredPIN != pin:

    print("❌ Incorrect PIN! Access Denied. Please try again later.")

    exit()

else:

   print("\n🎉 Login Successful! Welcome to your ATM Dashboard. \n")



while True:

    print("\n----------- ATM MAIN MENU -----------")

    print("1. Check Account Balance")

    print("2. Deposit Money")

    print("3. Withdraw money")
    print("4. Change Your PIN")

    print("5. Exit ATM")

    print("-------------------------------------")



    choice = input("Choose an option (1-5): ")

#OPTION 1: Check Balance

    if choice == "1":

     print(f"\n💰 Your Current Balance is: ₹{balance}")
     
    #OPTION 2: Deposit

    elif choice == "2":

       amount = float(input("Enter amount you want to deposit : ₹"))

       if amount <= 0:

            print("❌ Invalid Amount! Please enter a positive value.")

       else:

            balance += amount

            print(f"✅ Successfully deposited ₹{amount}.")

            print(f"💼 Updated Balance: ₹{balance}")

    #OPTION 3: Withdraw
    elif choice == "3":

      amount = float(input("Enter amount you like to withdraw: ₹"))

      if amount  > balance:

        print("❌ Insufficient Balance! Please try a smaller amount.")

      else:

        balance -= amount

        print(f"💳 ₹{amount} withdrawn successfully!")

        print(f"💼 Updated Balance: ₹{balance}")



    #OPTION 4: Change PIN

    elif choice == "4":

      new_pin = input("Enter your new 4-digit PIN: ")

      if len(new_pin) !=4:

        print("❌ PIN must be 4 digits and only numbers!")

      else:

        pin = new_pin

        print("🔐 Successfully updated your PIN!")



    #OPTION 5: Exit

    elif choice == "5":

      print("\n🙏 Thanksfor Banking with our ATM Service! Have a great day! 👋")
      break
                                                                                     
    else:
     print("invalid option")
