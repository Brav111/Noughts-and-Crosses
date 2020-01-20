#!/bin/python3

from random import randint

def restart():
    restart = input("DO YOU WANT TO RESTART?(yes/no): ")

    if restart == "yes":
        main()
    else:
        exit()

def main():
    player = input("ROCK(r), PAPER(p), Scissors(s)?: ")
    chosen = randint(1,3)
    computer = ""

    if chosen == 1:
        computer = "r"
    elif chosen == 2:
        computer = "p"
    else:
        computer = "s"

    if player == computer:
        print(player + " vs " + computer)
        print("DRAW!")
        restart()
    elif player == "r" and computer == "s":
        print(player + " vs " + computer)
        print("ROCK BEATS SCISSORS. YOU WIN!")
        restart()
    elif player == "r" and computer == "p":
        print(player + " vs " + computer)
        print("PAPER BEATS ROCK. YOU LOSE!")
        restart()
    elif player == "p" and computer == "r":
        print(player + " vs " + computer)
        print("PAPER BEATS ROCK. YOU WIN!")
        restart()
    elif player == "p" and computer == "s":
        print(player + " vs " + computer)
        print("SCISSORS BEATS ROCK. YOU LOSE!")
        restart()
    elif player == "s" and computer == "p":
        print(player + " vs " + computer)
        print("SCISSORS BEATS PAPER. YOU WIN!")
        restart()
    elif player == "s" and computer == "r":
        print(player + " vs " + computer)
        print("ROCK BEATS SCISSORS. YOU LOSE!")
        restart()
    else:
        print("INVALID INPUT")
        restart()
main()