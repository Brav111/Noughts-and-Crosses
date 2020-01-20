def main():
    print("""
    (1) NEW GAME
    (2) RULES
    (3) EXIT""")

    command = input("ENTER: ")

    if command == "1":
        newgame()
    elif command == "2":
        print("""
        Rules
        """)
    elif command == "3":
        exit()
    else:
        print("INVALID INPUT")
        main()

def newgame():
    print("""
    (1) SINGLE PLAYER
    (2) MULTIPLAYER
    (3) MENU
    (4) EXIT""")

    command = input("ENTER: ")

    if command == "1":
        singleplayer()
    elif command == "2":
        multiplayer()
    elif command == "3":
        main()
    elif command == "4":
        exit()
    else:
        print("INVALID INPUT")
        newgame()

def multiplayer():
    print("\n" + "1" + "|" + "2" + "|" + "3")
    print("_ _ _")
    print("4" + "|" + "5" + "|" + "6")
    print("_ _ _")
    print("7" + "|" + "8" + "|" + "9")

    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    six = "6"
    seven = "7"
    eight = "8"
    nine = "9"

    player1_num = input("ENTER PLAYER 1: ")

    if player1_num == "1":
        if one == "O":
            print("ALREADY TAKEN")
        else:
            one = "X"
    elif player1_num == "2":
        if two == "O":
            print("ALREADY TAKEN")
        else:
            two = "X"
    elif player1_num == "3":
        if three == "O":
            print("ALREADY TAKEN")
        else:
            three = "X"
    elif player1_num == "4":
        if four == "O":
            print("ALREADY TAKEN")
        else:
            four = "X"
    elif player1_num == "5":
        if five == "O":
            print("ALREADY TAKEN")
        else:
            five = "X"
    elif player1_num == "6":
        if six == "O":
            print("ALREADY TAKEN")
        else:
            six = "X"
    elif player1_num == "7":
        if seven == "O":
            print("ALREADY TAKEN")
        else:
            seven = "X"
    elif player1_num == "8":
        if eight == "O":
            print("ALREADY TAKEN")
        else:
            eight = "X"
    elif player1_num == "9":
        if nine == "O":
            print("ALREADY TAKEN")
        else:
            nine = "X"

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

    player2_num = input("ENTER PLAYER 2: ")

    if player2_num == "1":
        if one == "X":
            print("ALREADY TAKEN")
        else:
            one = "O"
    elif player2_num == "2":
        if two == "X":
            print("ALREADY TAKEN")
        else:
            two = "O"
    elif player2_num == "3":
        if three == "X":
            print("ALREADY TAKEN")
        else:
            three = "O"
    elif player2_num == "4":
        if four == "X":
            print("ALREADY TAKEN")
        else:
            four = "O"
    elif player2_num == "5":
        if five == "X":
            print("ALREADY TAKEN")
        else:
            five = "O"
    elif player2_num == "6":
        if six == "X":
            print("ALREADY TAKEN")
        else:
            six = "O"
    elif player2_num == "7":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"
    elif player2_num == "8":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"
    elif player2_num == "9":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

    player1_num = input("ENTER PLAYER 1: ")

    if player1_num == "1":
        if one == "O":
            print("ALREADY TAKEN")
        else:
            one = "X"
    elif player1_num == "2":
        if two == "O":
            print("ALREADY TAKEN")
        else:
            two = "X"
    elif player1_num == "3":
        if three == "O":
            print("ALREADY TAKEN")
        else:
            three = "X"
    elif player1_num == "4":
        if four == "O":
            print("ALREADY TAKEN")
        else:
            four = "X"
    elif player1_num == "5":
        if five == "O":
            print("ALREADY TAKEN")
        else:
            five = "X"
    elif player1_num == "6":
        if six == "O":
            print("ALREADY TAKEN")
        else:
            six = "X"
    elif player1_num == "7":
        if seven == "O":
            print("ALREADY TAKEN")
        else:
            seven = "X"
    elif player1_num == "8":
        if eight == "O":
            print("ALREADY TAKEN")
        else:
            eight = "X"
    elif player1_num == "9":
        if nine == "O":
            print("ALREADY TAKEN")
        else:
            nine = "X"

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

    player2_num = input("ENTER PLAYER 2: ")

    if player2_num == "1":
        if one == "X":
            print("ALREADY TAKEN")
        else:
            one = "O"
    elif player2_num == "2":
        if two == "X":
            print("ALREADY TAKEN")
        else:
            two = "O"
    elif player2_num == "3":
        if three == "X":
            print("ALREADY TAKEN")
        else:
            three = "O"
    elif player2_num == "4":
        if four == "X":
            print("ALREADY TAKEN")
        else:
            four = "O"
    elif player2_num == "5":
        if five == "X":
            print("ALREADY TAKEN")
        else:
            five = "O"
    elif player2_num == "6":
        if six == "X":
            print("ALREADY TAKEN")
        else:
            six = "O"
    elif player2_num == "7":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"
    elif player2_num == "8":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"
    elif player2_num == "9":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

    player1_num = input("ENTER PLAYER 1: ")

    if player1_num == "1":
        if one == "O":
            print("ALREADY TAKEN")
        else:
            one = "X"
    elif player1_num == "2":
        if two == "O":
            print("ALREADY TAKEN")
        else:
            two = "X"
    elif player1_num == "3":
        if three == "O":
            print("ALREADY TAKEN")
        else:
            three = "X"
    elif player1_num == "4":
        if four == "O":
            print("ALREADY TAKEN")
        else:
            four = "X"
    elif player1_num == "5":
        if five == "O":
            print("ALREADY TAKEN")
        else:
            five = "X"
    elif player1_num == "6":
        if six == "O":
            print("ALREADY TAKEN")
        else:
            six = "X"
    elif player1_num == "7":
        if seven == "O":
            print("ALREADY TAKEN")
        else:
            seven = "X"
    elif player1_num == "8":
        if eight == "O":
            print("ALREADY TAKEN")
        else:
            eight = "X"
    elif player1_num == "9":
        if nine == "O":
            print("ALREADY TAKEN")
        else:
            nine = "X"

    if one == "X" and two == "X" and three == "X":
        print("X WINS!")

        exit()
    elif one == "X" and five == "X" and nine == "X":
        print("X WINS!")

        exit()
    elif one == "X" and four == "X" and seven == "X":
        print("X WINS!")

        exit()
    elif two == "X" and five == "X" and eight == "X":
        print("X WINS!")

        exit()
    elif three == "X" and six == "X" and nine == "X":
        print("X WINS!")

        exit()
    elif three == "X" and five == "X" and seven == "X":
        print("X WINS!")

        exit()
    elif four == "X" and five == "X" and six == "X":
        print("X WINS!")

        exit()
    elif seven == "X" and eight == "X" and nine == "X":
        print("X WINS!")

        exit()

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

    player2_num = input("ENTER PLAYER 2: ")

    if player2_num == "1":
        if one == "X":
            print("ALREADY TAKEN")
        else:
            one = "O"
    elif player2_num == "2":
        if two == "X":
            print("ALREADY TAKEN")
        else:
            two = "O"
    elif player2_num == "3":
        if three == "X":
            print("ALREADY TAKEN")
        else:
            three = "O"
    elif player2_num == "4":
        if four == "X":
            print("ALREADY TAKEN")
        else:
            four = "O"
    elif player2_num == "5":
        if five == "X":
            print("ALREADY TAKEN")
        else:
            five = "O"
    elif player2_num == "6":
        if six == "X":
            print("ALREADY TAKEN")
        else:
            six = "O"
    elif player2_num == "7":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"
    elif player2_num == "8":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"
    elif player2_num == "9":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"

    if one == "O" and two == "O" and three == "O":
        print("X WINS!")

        exit()
    elif one == "O" and five == "O" and nine == "O":
        print("X WINS!")

        exit()
    elif one == "O" and four == "O" and seven == "O":
        print("X WINS!")

        exit()
    elif two == "O" and five == "O" and eight == "O":
        print("X WINS!")

        exit()
    elif three == "O" and six == "O" and nine == "O":
        print("X WINS!")

        exit()
    elif three == "O" and five == "O" and seven == "O":
        print("X WINS!")

        exit()
    elif four == "O" and five == "O" and six == "O":
        print("X WINS!")

        exit()
    elif seven == "O" and eight == "O" and nine == "O":
        print("X WINS!")

        exit()

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

    player1_num = input("ENTER PLAYER 1: ")

    if player1_num == "1":
        if one == "O":
            print("ALREADY TAKEN")
        else:
            one = "X"
    elif player1_num == "2":
        if two == "O":
            print("ALREADY TAKEN")
        else:
            two = "X"
    elif player1_num == "3":
        if three == "O":
            print("ALREADY TAKEN")
        else:
            three = "X"
    elif player1_num == "4":
        if four == "O":
            print("ALREADY TAKEN")
        else:
            four = "X"
    elif player1_num == "5":
        if five == "O":
            print("ALREADY TAKEN")
        else:
            five = "X"
    elif player1_num == "6":
        if six == "O":
            print("ALREADY TAKEN")
        else:
            six = "X"
    elif player1_num == "7":
        if seven == "O":
            print("ALREADY TAKEN")
        else:
            seven = "X"
    elif player1_num == "8":
        if eight == "O":
            print("ALREADY TAKEN")
        else:
            eight = "X"
    elif player1_num == "9":
        if nine == "O":
            print("ALREADY TAKEN")
        else:
            nine = "X"

    if one == "X" and two == "X" and three == "X":
        print("X WINS!")

        exit()
    elif one == "X" and five == "X" and nine == "X":
        print("X WINS!")

        exit()
    elif one == "X" and four == "X" and seven == "X":
        print("X WINS!")

        exit()
    elif two == "X" and five == "X" and eight == "X":
        print("X WINS!")

        exit()
    elif three == "X" and six == "X" and nine == "X":
        print("X WINS!")

        exit()
    elif three == "X" and five == "X" and seven == "X":
        print("X WINS!")

        exit()
    elif four == "X" and five == "X" and six == "X":
        print("X WINS!")

        exit()
    elif seven == "X" and eight == "X" and nine == "X":
        print("X WINS!")

        exit()

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

    player2_num = input("ENTER PLAYER 2: ")

    if player2_num == "1":
        if one == "X":
            print("ALREADY TAKEN")
        else:
            one = "O"
    elif player2_num == "2":
        if two == "X":
            print("ALREADY TAKEN")
        else:
            two = "O"
    elif player2_num == "3":
        if three == "X":
            print("ALREADY TAKEN")
        else:
            three = "O"
    elif player2_num == "4":
        if four == "X":
            print("ALREADY TAKEN")
        else:
            four = "O"
    elif player2_num == "5":
        if five == "X":
            print("ALREADY TAKEN")
        else:
            five = "O"
    elif player2_num == "6":
        if six == "X":
            print("ALREADY TAKEN")
        else:
            six = "O"
    elif player2_num == "7":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"
    elif player2_num == "8":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"
    elif player2_num == "9":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"

    if one == "O" and two == "O" and three == "O":
        print("X WINS!")

        exit()
    elif one == "O" and five == "O" and nine == "O":
        print("X WINS!")

        exit()
    elif one == "O" and four == "O" and seven == "O":
        print("X WINS!")

        exit()
    elif two == "O" and five == "O" and eight == "O":
        print("X WINS!")

        exit()
    elif three == "O" and six == "O" and nine == "O":
        print("X WINS!")

        exit()
    elif three == "O" and five == "O" and seven == "O":
        print("X WINS!")

        exit()
    elif four == "O" and five == "O" and six == "O":
        print("X WINS!")

        exit()
    elif seven == "X" and eight == "X" and nine == "X":
        print("X WINS!")

        exit()

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

    player1_num = input("ENTER PLAYER 1: ")

    if player1_num == "1":
        if one == "O":
            print("ALREADY TAKEN")
        else:
            one = "X"
    elif player1_num == "2":
        if two == "O":
            print("ALREADY TAKEN")
        else:
            two = "X"
    elif player1_num == "3":
        if three == "O":
            print("ALREADY TAKEN")
        else:
            three = "X"
    elif player1_num == "4":
        if four == "O":
            print("ALREADY TAKEN")
        else:
            four = "X"
    elif player1_num == "5":
        if five == "O":
            print("ALREADY TAKEN")
        else:
            five = "X"
    elif player1_num == "6":
        if six == "O":
            print("ALREADY TAKEN")
        else:
            six = "X"
    elif player1_num == "7":
        if seven == "O":
            print("ALREADY TAKEN")
        else:
            seven = "X"
    elif player1_num == "8":
        if eight == "O":
            print("ALREADY TAKEN")
        else:
            eight = "X"
    elif player1_num == "9":
        if nine == "O":
            print("ALREADY TAKEN")
        else:
            nine = "X"
    if one == "X" and two == "X" and three == "X":
        print("X WINS!")

        exit()
    elif one == "X" and five == "X" and nine == "X":
        print("X WINS!")

        exit()
    elif one == "X" and four == "X" and seven == "X":
        print("X WINS!")

        exit()
    elif two == "X" and five == "X" and eight == "X":
        print("X WINS!")

        exit()
    elif three == "X" and six == "X" and nine == "X":
        print("X WINS!")

        exit()
    elif three == "X" and five == "X" and seven == "X":
        print("X WINS!")

        exit()
    elif four == "X" and five == "X" and six == "X":
        print("X WINS!")

        exit()
    elif seven == "X" and eight == "X" and nine == "X":
        print("X WINS!")

        exit()

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

    player2_num = input("ENTER PLAYER 2: ")

    if player2_num == "1":
        if one == "X":
            print("ALREADY TAKEN")
        else:
            one = "O"
    elif player2_num == "2":
        if two == "X":
            print("ALREADY TAKEN")
        else:
            two = "O"
    elif player2_num == "3":
        if three == "X":
            print("ALREADY TAKEN")
        else:
            three = "O"
    elif player2_num == "4":
        if four == "X":
            print("ALREADY TAKEN")
        else:
            four = "O"
    elif player2_num == "5":
        if five == "X":
            print("ALREADY TAKEN")
        else:
            five = "O"
    elif player2_num == "6":
        if six == "X":
            print("ALREADY TAKEN")
        else:
            six = "O"
    elif player2_num == "7":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"
    elif player2_num == "8":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"
    elif player2_num == "9":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"

    if one == "O" and two == "O" and three == "O":
        print("X WINS!")

        exit()
    elif one == "O" and five == "O" and nine == "O":
        print("X WINS!")

        exit()
    elif one == "O" and four == "O" and seven == "O":
        print("X WINS!")

        exit()
    elif two == "O" and five == "O" and eight == "O":
        print("X WINS!")

        exit()
    elif three == "O" and six == "O" and nine == "O":
        print("X WINS!")

        exit()
    elif three == "O" and five == "O" and seven == "O":
        print("X WINS!")

        exit()
    elif four == "O" and five == "O" and six == "O":
        print("X WINS!")

        exit()
    elif seven == "X" and eight == "X" and nine == "X":
        print("X WINS!")

        exit()

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

    player1_num = input("ENTER PLAYER 1: ")

    if player1_num == "1":
        if one == "O":
            print("ALREADY TAKEN")
        else:
            one = "X"
    elif player1_num == "2":
        if two == "O":
            print("ALREADY TAKEN")
        else:
            two = "X"
    elif player1_num == "3":
        if three == "O":
            print("ALREADY TAKEN")
        else:
            three = "X"
    elif player1_num == "4":
        if four == "O":
            print("ALREADY TAKEN")
        else:
            four = "X"
    elif player1_num == "5":
        if five == "O":
            print("ALREADY TAKEN")
        else:
            five = "X"
    elif player1_num == "6":
        if six == "O":
            print("ALREADY TAKEN")
        else:
            six = "X"
    elif player1_num == "7":
        if seven == "O":
            print("ALREADY TAKEN")
        else:
            seven = "X"
    elif player1_num == "8":
        if eight == "O":
            print("ALREADY TAKEN")
        else:
            eight = "X"
    elif player1_num == "9":
        if nine == "O":
            print("ALREADY TAKEN")
        else:
            nine = "X"

    if one == "X" and two == "X" and three == "X":
        print("X WINS!")

        exit()
    elif one == "X" and five == "X" and nine == "X":
        print("X WINS!")

        exit()
    elif one == "X" and four == "X" and seven == "X":
        print("X WINS!")

        exit()
    elif two == "X" and five == "X" and eight == "X":
        print("X WINS!")

        exit()
    elif three == "X" and six == "X" and nine == "X":
        print("X WINS!")

        exit()
    elif three == "X" and five == "X" and seven == "X":
        print("X WINS!")

        exit()
    elif four == "X" and five == "X" and six == "X":
        print("X WINS!")

        exit()
    elif seven == "X" and eight == "X" and nine == "X":
        print("X WINS!")

        exit()

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

def singleplayer():
    print("""
    (1) X
    (2) O
    """)

    command = input("ENTER: ")

    if command == "1":
        xbot()
    elif command == "2":
        obot()
    else:
        print("INVALID INPUT")
        singleplayer()

def xbot():
    print("\n" + "1" + "|" + "2" + "|" + "3")
    print("_ _ _")
    print("4" + "|" + "5" + "|" + "6")
    print("_ _ _")
    print("7" + "|" + "8" + "|" + "9")

    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    six = "6"
    seven = "7"
    eight = "8"
    nine = "9"

    player1_num = input("ENTER PLAYER 1: ")

    if player1_num == "1":
        if one == "O":
            print("ALREADY TAKEN")
        else:
            one = "X"
    elif player1_num == "2":
        if two == "O":
            print("ALREADY TAKEN")
        else:
            two = "X"
    elif player1_num == "3":
        if three == "O":
            print("ALREADY TAKEN")
        else:
            three = "X"
    elif player1_num == "4":
        if four == "O":
            print("ALREADY TAKEN")
        else:
            four = "X"
    elif player1_num == "5":
        if five == "O":
            print("ALREADY TAKEN")
        else:
            five = "X"
    elif player1_num == "6":
        if six == "O":
            print("ALREADY TAKEN")
        else:
            six = "X"
    elif player1_num == "7":
        if seven == "O":
            print("ALREADY TAKEN")
        else:
            seven = "X"
    elif player1_num == "8":
        if eight == "O":
            print("ALREADY TAKEN")
        else:
            eight = "X"
    elif player1_num == "9":
        if nine == "O":
            print("ALREADY TAKEN")
        else:
            nine = "X"

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

def obot():
    one = "X"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    six = "6"
    seven = "7"
    eight = "8"
    nine = "9"

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

    player2_num = input("ENTER PLAYER 2: ")

    if player2_num == "1":
        if one == "X":
            print("ALREADY TAKEN")
        else:
            one = "O"
    elif player2_num == "2":
        if two == "X":
            print("ALREADY TAKEN")
        else:
            two = "O"
    elif player2_num == "3":
        if three == "X":
            print("ALREADY TAKEN")
        else:
            three = "O"
    elif player2_num == "4":
        if four == "X":
            print("ALREADY TAKEN")
        else:
            four = "O"
    elif player2_num == "5":
        if five == "X":
            print("ALREADY TAKEN")
        else:
            five = "O"
    elif player2_num == "6":
        if six == "X":
            print("ALREADY TAKEN")
        else:
            six = "O"
    elif player2_num == "7":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"
    elif player2_num == "8":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"
    elif player2_num == "9":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

    if two == "O":
        nine = "X"
    elif three == "O":
        nine = "X"
    elif four == "O":
        nine = "X"
    elif five == "O":
        nine = "X"
    elif six == "O":
        nine = "X"
    elif seven == "O":
        nine = "X"
    elif eight == "O":
        nine = 'X'
    elif nine == 'O':
        five = "X"
    else:
        nine = "X"

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

    player2_num = input("ENTER PLAYER 2: ")

    if player2_num == "1":
        if one == "X":
            print("ALREADY TAKEN")
        else:
            one = "O"
    elif player2_num == "2":
        if two == "X":
            print("ALREADY TAKEN")
        else:
            two = "O"
    elif player2_num == "3":
        if three == "X":
            print("ALREADY TAKEN")
        else:
            three = "O"
    elif player2_num == "4":
        if four == "X":
            print("ALREADY TAKEN")
        else:
            four = "O"
    elif player2_num == "5":
        if five == "X":
            print("ALREADY TAKEN")
        else:
            five = "O"
    elif player2_num == "6":
        if six == "X":
            print("ALREADY TAKEN")
        else:
            six = "O"
    elif player2_num == "7":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"
    elif player2_num == "8":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"
    elif player2_num == "9":
        if seven == "X":
            print("ALREADY TAKEN")
        else:
            seven = "O"

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

    if two == "O":
        nine = "X"
    elif three == "O":
        nine = "X"
    elif four == "O":
        nine = "X"
    elif five == "O":
        nine = "X"
    elif six == "O":
        nine = "X"
    elif seven == "O":
        nine = "X"
    elif eight == "O":
        nine = 'X'
    elif nine == 'O':
        five = "X"
    else:
        nine = "X"

    print("\n" + one + "|" + two + "|" + three)
    print("_ _ _")
    print(four + "|" + five + "|" + six)
    print("_ _ _")
    print(seven + "|" + eight + "|" + nine)

main()