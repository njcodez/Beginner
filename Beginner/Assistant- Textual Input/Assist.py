# building a virtual assistant
# notes for adding function
import random
import string


class virtualassist:
    def helpuser():
        def pattern():
            print("Glad you initiated this function.. Letss goo..")
            infinity = 10e5000
            qa = input("Enter 'n' for row number pattern 's' for desired symbol  ")
            qa = qa.lower()
            rows = int(
                input(
                    "Enter the desired number of rows(Type 'infinity' to print infinitely!!)  "
                )
            )
            if qa == "s":
                symbol = input("What symbol do you want to print?  ")
                for i in range(rows + 1):
                    for j in range(i):
                        print(symbol, end=" ")
                    print("")
            elif qa == "n":
                for i in range(rows + 1):
                    for j in range(i):
                        print(i, end=" ")
                    print("")

        def hackervfx():
            rows = 10e453
            for i in range(rows + 1):
                for j in range(i):
                    print("10101010", end="")
                print("")

        def genpwd():
            length = int(input("Enter the desired length "))
            letters = string.ascii_lowercase
            result_str = "".join(random.choice(letters) for i in range(length))
            print("Random string of length", length, "is:", result_str)

        print(
            "Here's what I can do \npattern - Generate pattern\nhackervfx - Create a binary background as shown in movies\npassword - Generate a complex password for internet users"
        )
        desired = input("What do you want me to do? ").lower()
        if desired == "pattern":
            pattern()
        elif desired == "hackervfx":
            hackervfx()
        elif desired == "password":
            genpwd()

    name = input(
        "Hello! This is Xnora your virtual assistant What should I call you?  "
    )
    inhelp = input(f"Hey {name}!! type helpme to pull up navigation menu ")
    if inhelp.lower() == "helpme":
        helpuser()


virtualassist()
