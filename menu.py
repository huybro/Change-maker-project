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
            elif selection == "c":
