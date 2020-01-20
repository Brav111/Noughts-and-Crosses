def main():
    print("""
    1.NEW GAME (1)
    2.RULES (2)
    3.EXIT (3)""")

    command = input("ENTER: ")

    if command == "1":
        newgame()
    elif command == "2":
        print("""
        RULES:
        
        ALL CAPITALS
        """)
    elif command == "3":
        exit()
    else:
        print("INVALID INPUT")
        main()

def newgame():
    def multiplayer():

        print("Player 1, you have to make sure PLayer 2 doesn't get the answer")

        question = (input("ENTER QUESTION: "))
        answer = (input("ENTER ANSWER: "))
        hint = (input("ENTER HINT: "))
        num_of_guesses = int(input("ENTER NUMBER OF GUESSES: "))

        print("""
        """ * 1000)

        print("Player 2, you have to answer player 1's question")
        print("QUESTION: " + question)
        print("HINT: " + hint)
        print("NUMBER OF GUESSES: " + str(num_of_guesses))

        while num_of_guesses > 0:
            user_answer = (input("ENTER ANSWER: "))

            if user_answer == answer:
                print("CORRECT! PLAYER 2 WINS")
                restart()
            else:
                print("INCORRECT")
                num_of_guesses -= 1

            if num_of_guesses == 0:
                print("RUN OUT OF GUESSES, PLAYER 1 WINS!")
                restart()

    def singleplayer():
        def history():
            #!/bin/python3
            from random import randint
            chosen = randint(1,10)
            guesses = 3

            history_questons = ["QUESTION1","QUESTION2","QUESTION3","QUESTION4","QUESTION5","QUESTION6","QUESTION7","QUESTION8","QUESTION9","QUESTION10","QUESTION11",]
            history_answers = ["ANSWER1","ANSWER2","ANSWER3","ANSWER4","ANSWER5","ANSWER6,""ANSWER7","ANSWER8","ANSWER9","ANSWER10","ANSWER11",]

            print(history_questons[chosen])
            print(history_questons[chosen])


            user_input = input("ENTER ANSWER: ")

            answer = history_answers[chosen]

            while guesses > 0:
                if user_input == answer:
                    print("CORRECT, YOU WIN")
                    main()
                else:
                    print("INCORRECT")
                    guesses -= 1

                if guesses == 0:
                    print("YOU RAN OUT OF GUESSES, YOU LOSE")
                    print("THE ANSWER WAS " + answer)
                    main()

        def science():
            #!/bin/python3
            from random import randint
            chosen = randint(1,10)

            science_questons = ["QUESTION1","QUESTION2","QUESTION3","QUESTION4","QUESTION5","QUESTION6","QUESTION7","QUESTION8","QUESTION9","QUESTION10","QUESTION11",]
            science_answers = ["ANSWER1","ANSWER2","ANSWER3","ANSWER4","ANSWER5","ANSWER6,""ANSWER7","ANSWER8","ANSWER9","ANSWER10","ANSWER11",]

            print(science_questons[chosen])
            print(science_questons[chosen])


            user_input = input("ENTER ANSWER: ")

            answer = science_answers[chosen]

            while guesses > 0:
                if user_input == answer:
                    print("CORRECT, YOU WIN")
                    main()
                else:
                    print("INCORRECT")
                    guesses -= 1

                if guesses == 0:
                    print("YOU RAN OUT OF GUESSES, YOU LOSE")
                    print("THE ANSWER WAS " + answer)
                    main()

        def maths():
            #!/bin/python3
            from random import randint
            chosen = randint(1,10)

            maths_questons = ["QUESTION1","QUESTION2","QUESTION3","QUESTION4","QUESTION5","QUESTION6","QUESTION7","QUESTION8","QUESTION9","QUESTION10","QUESTION11",]
            maths_answers = ["ANSWER1","ANSWER2","ANSWER3","ANSWER4","ANSWER5","ANSWER6,""ANSWER7","ANSWER8","ANSWER9","ANSWER10","ANSWER11",]

            print(maths_questons[chosen])
            print(maths_questons[chosen])


            user_input = input("ENTER ANSWER: ")

            answer = maths_answers[chosen]

            while guesses > 0:
                if user_input == answer:
                    print("CORRECT, YOU WIN")
                    main()
                else:
                    print("INCORRECT")
                    guesses -= 1

                if guesses == 0:
                    print("YOU RAN OUT OF GUESSES, YOU LOSE")
                    print("THE ANSWER WAS " + answer)
                    main()

        def geography():
            #!/bin/python3
            from random import randint
            chosen = randint(1,10)

            geography_questons = ["QUESTION1","QUESTION2","QUESTION3","QUESTION4","QUESTION5","QUESTION6","QUESTION7","QUESTION8","QUESTION9","QUESTION10","QUESTION11",]
            geography_answers = ["ANSWER1","ANSWER2","ANSWER3","ANSWER4","ANSWER5","ANSWER6,""ANSWER7","ANSWER8","ANSWER9","ANSWER10","ANSWER11",]

            print(geography_questons[chosen])
            print(geography_questons[chosen])


            user_input = input("ENTER ANSWER: ")

            answer = geography_answers[chosen]

            while guesses > 0:
                if user_input == answer:
                    print("CORRECT, YOU WIN")
                    main()
                else:
                    print("INCORRECT")
                    guesses -= 1

                if guesses == 0:
                    print("YOU RAN OUT OF GUESSES, YOU LOSE")
                    print("THE ANSWER WAS " + answer)
                    main()

        print("""
        WHICH CATEGORY DO YOU WANT?:

        1. HISTORY
        2. SCIENCE
        3. MATHS
        4. GEOGRAPHY""")

        command = input("ENTER: ")

        if command == "1":
            history()
        elif command == "2":
            science()
        elif command == "3":
            maths()
        elif command == "4":
            geography()
        else:
            print("INVALID INPUT")
            singleplayer()

    print("""
    1.MULTIPLAYER(1)
    2.SINGLE PLAYER(2)
    3.EXIT(3)
    4.MENU(4)""")

    command = input("ENTER: ")

    if command == "1":
        multiplayer()
    elif command == "2":
        singleplayer()
    elif command == "3":
        exit()
    elif command == "4":
        main()
    else:
        print("INVALID INPUT")
        newgame()

def restart():
    restart = (input("Do you want to play  again?(yes/no): "))

    if restart == "yes":
        multiplayer()
    else:
        main()

main()