print("Welcome to the vending machine change maker program")
print("Change maker initialized.")
nickels =25
dimes =25
quarters =25
ones = 0
fives = 0
user_command = 0


while user_command != "q":
    print("Stock contains:")
    print(f"   {nickels} nickels")
    print(f"   {dimes} dimes")
    print(f"   {quarters} quarters")
    print(f"   {ones} ones")
    print(f"   {fives} fives")
    total = fives + ones + quarters / 4 + dimes / 10 + nickels / 20
    while user_command != "q":
        user_command = input("Enter the purchase price (xx.xx) or `q' to quit:")
        if user_command == "q":
            print(f"Total: {int(total//1)} dollars and {int(total%1)} cents" )
            break
        elif float(user_command)* 100 % 5 != 0:
            print("Illegal price: Must be a non-negative multiple of 5 cents.")
        else:
            break
    menu_list = ["n","d","q","o","f","c"]
    menu_dict = {"n": 5,"d": 10,"q": 25,"o": 100,"f": 500}
    print("Menu for deposits:")
    print("  'n' - deposit a nickel")
    print("  'd' - deposit a dime")
    print("  'q' - deposit a quarter")
    print("  'o' - deposit a one dollar bill")
    print("  'f' - deposit a five dollar bill")
    print("  'c' - cancel the purschase")
    selection = 0
    payment_due = float(user_command) * 100
    while payment_due > 0:
        print(f"Payment due: {int(payment_due // 100) } dollars and {int(payment_due % 100) } cents")
        selection = input("Indicate your deposit: ")
        if selection not in menu_list:
            print(f"Illegal sellection: {selection}")
        if selection in menu_list:
            if selection =="n":
                nickels += 1
            elif selection == "d":
                dimes +=1 
            elif selection == "q":
                quarters +=1
            elif selection == "o":
                ones += 1
            elif selection =="f":
                fives += 1
            payment_due -= menu_dict[selection]
        

   

        
            
