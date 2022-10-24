def Flames():
    print("Enter names without spaces")
    person1 = input("Enter you name: ")
    person2 = input("Enter your crush's name: ")
    namestr = person1 + person2

    # eliminating common letters
    for i in namestr:
        if namestr.count(i) != 1:
            namestr = namestr.replace(i, "")

    print("...........FLAMES...........")
    print(
        "\tF = Friend \n\tL = Love \n\tA = Affection \n\tM = Marriage \n\tE = Enemy \n\tS = Siblings \n\t\n"
    )

    number = len(namestr) % 6
    # getting modulo for picking the letter
    if number == 4:
        rel = f"You and {person2} are Friends"
    elif number == 5:
        rel = f"You and {person2} are in love"
    elif number == 0:
        rel = f"You and {person2} are affectionate towards each other"
    elif number == 1:
        rel = f"You and {person2} will get married"
    elif number == 2:
        rel = f"Uh oh! Sorry to say .. you and {person2} will be enemies :("
    elif number == 3:
        rel = f"Treat {person2} like your sibling "
    print(rel)
    choice = input(
        "Do you want to try with someone else ;) \nEnter y for yes and n for no : "
    )
    if choice.lower() == "y":
        Flames()
    elif choice.lower() == "n":
        print(
            "Great now move on... \nInitiate this program anytime\nWaiting for new crushes ;)"
        )
    else:
        print("Invalid input")


Flames()
