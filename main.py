import random

print("Dice Rolling Stimulator\n")
x = 'y'
while x == 'y':
    n = random.randint(1, 6)

    if n == 1:
        print("-----------")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print("-----------")

    elif n==2:
        print("-----------")
        print("|       O |")
        print("|         |")
        print("| O       |")
        print("-----------")

    elif n==3:
        print("-----------")
        print("|       O |")
        print("|    O    |")
        print("| O       |")
        print("-----------")

    elif n==4:
        print("-----------")
        print("| O     O |")
        print("|         |")
        print("| O     O |")
        print("-----------")

    elif n==5:
        print("-----------")
        print("| O     O |")
        print("|    O    |")
        print("| O     O |")
        print("-----------")

    elif n==6:
        print("-----------")
        print("| O     O |")
        print("| O     O |")
        print("| O     O |")
        print("-----------")

    x = input("Press 'y' to input Again:\n")