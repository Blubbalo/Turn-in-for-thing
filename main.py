print("You lost your job at Burger King because literally nobody eats there, and they went out of business. You need to pay your rent soon.")

choice1 = input("Get a job? (yes/no): ")

if choice1 == "yes":
    print("You start making money! And are able to pay your rent.")
    print("You find it hard to get around.")
    choice3 = input("Choose 1 to Buy a car, or 2 to Buy video games: ")

    if choice3 == "1":
        print("You grow your money and are able to live happily ever after.")
    elif choice3 == "2":
        print("You feel you could start streaming with video games.")
        choice4 = input("Choose 1 to Buy horror games, or 2 to buy Fortnite: ")

        if choice4 == "1":
            print("You become rich and famous!")
        elif choice4 == "2":
            print("You got no views and instantly got evicted.")

else:
    print("You are going broke and need to take action quick.")
    choice2 = input("Choose 1 to Get a job, or 2 to Start streaming: ")

    if choice2 == "1":
        print("You start making money. Enough to pay off rent in the nick of time.")
        print("You find it hard to get around.")
        choice3 = input("Choose 1 to Buy a car, or 2 to Buy video games: ")

        if choice3 == "1":
            print("You grow your money and are able to live happily ever after.")
        elif choice3 == "2":
            print("You feel you could start streaming with video games.")
            choice4 = input("Choose 1 to Buy horror games, or 2 to buy Fortnite: ")

            if choice4 == "1":
                print("You become rich and famous!")
            elif choice4 == "2":
                print("You got no views and instantly got evicted.")

    elif choice2 == "2":
        print("You got no views and instantly got evicted.")
