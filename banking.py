
print(40*'=')

customerNames = ['Kumar','Abhilash','Srikanth','Prakash','Vishwa']
customerPins = ['1234','5678','0123','4567','8901']
customerBalances = [5000,10000,15000,20000,25000]
deposition = 0
withdrawl = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0

while True:
    print(40*'=')
    print("-----Welcome to ATM Bank-----")
    print(40*'*')
    print("=<< 1. Open anAccount            >>=")
    print("=<< 2. Withdraw Money            >>=")
    print("=<< 3. Deposit Money             >>=")
    print("=<< 4. Check customers Balance   >>=")
    print("=<< 5. Exit/Quit                 >>=")
    print(40*'*')

    choiceNumber = input("Select your choice number from the above")
    if choiceNumber =="1":
        print("Choice number 1 is selected by the user")

        NOC = eval(input("Number of customers :"))

        i = i + NOC
        if i > 5:
            print("\n")
            print("user registration exceed reached")
            i = i - NOC  
        else:
            while counter_1 <= i:
                name = input("Input Fullname :")
                customerNames.append(name)
                pin = str(input("please input apin of your choice"))
                customerPins.append(pin)
                balance = 0
                deposition = eval(input("please input a value"))
                balance = balance + deposition
                customerBalances.append(balance)
                print("\nName=", end=" ")
                print(customerNames[counter_2])
                print("pin=", end=" ")
                print(customerPins[counter_2])  
                print("balance=", end=" ")
                print(customerBalances[counter_2], end=" ")
                print("-/RS")
                conuter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("\n Your name is added to customers system")
                print("Your pin is added to customers system")
                print("your balance is added to customers system")
                print("-----New Account created successfully-----")
                print("\n")
                print("Your name is now available in the customers list:")
                print(customerNames)
                print("\n")
                print("Please remember name and your pin")
                print(40*"=")
        mainMenu = input("please press enter key to go back to main menu")
    elif choiceNumber == "2":
        j = 0
        print("Choice number 2 is selected by the user")
        while j < 1:
            k = -1
            name = input("please input name : ")
            pin = input("please input pin: ")

            while k <len(customerNames) - 1:
                k = k + 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1
                        print("Your current balance:", end="")
                        print(customerBalances[k], end=" ")
                        print("-/Rs\n")
                        balance = (customerBalances[k])
                        withdrawl = eval(input("input the value of amount to withdraw : "))
                        if withdrawl > balance:
                            deposition = eval(input("you dont have enough balance to withdraw the amount you want"))
                            balance = balance + deposition
                            print("Your current balance is: ", end=" ")
                            print(balance, end=" ")
                            print("-/Rs\n")
                            balance = balance - withdrawl
                            print("-\n")
                            print("----- Withdrawl Successful -----")
                            customerBalances[k] = balance
                            print("youe new balance: ", balance, end=" ")
                            print("-/Rs\n\n")
                        else:
                            balance = balance - withdrawl
                            print("\n")
                            print("----- Withdrawl successful----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
            if j < 1:
                print("Name and pin entered does not match\n")
                break
        mainmenu = input ("press enter key to go back to main menu")
    elif choiceNumber =="3":
        print("Choice number 3 is selected by the user")
        n = 0
        while n < 1:
            k = -1
            name = input("please input name: ")
            pin = input("please enter your pin: ")
            while k < len(customerNames) - 1:
                k = k + 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n = n + 1
                        print("Your current Balance: ", end=" ") 
                        print(customerBalances[k], end=" ") 
                        print("-/Rs")
                        balance = (customerBalances[k])
                        deposition = eval(inpur("Enter the value of money you want to deposit"))
                        balance = balance + deposition
                        customerBalances[k] = balance
                        print("\n")
                        print("-----Deposition Sucessfully completed -----")
                        print("Your current balance is: ",balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("Name and pin entered does not match\n")
                break

        mainmenu = input ("press enter key to go back to main menu")
    elif choiceNumber =="4":
        print("Choice number 4 is selected by the user")
        k = 0
        print("customer name list and balances mentioned below :")
        print("-\n")
        while k <= len(customerNames) - 1:
            print(" ->.customer =", customerNames[k])  
            print(" ->.Balance =", customerBalances[k], end=" ") 
            print("-/Rs") 
            print("\n")
            k =  k + 1
        mainmenu = input ("press enter key to go back to main menu")
    elif choiceNumber =="5":    
        print("Choice number 5 has been selected")  
        print("Thankyou for using our bank services")
        print("\n")
        print("------Come Again------")
        break
    else:
        print("Invalid option is selected")
        print("please try again")
        mainmenu = input ("press enter key to go back to main menu")

    


