import random
import time

def displayIntro():
    print()
    print("You are in a land full of Aardvarks.  In front of you,")
    print("you see two caves.  In one cave, the Aardvark is friendly")
    print("and will share his treasure with you.  The other Aardvark")
    print("is greedy and hungry, and will eat you on sight.")
    print()

def chooseCave():
    """The return of this method will always be the number 1 or 2"""
    cave = ""
    while cave != "1" and cave != "2":
        cave = input("Which cave will you go into? (1 or 2)")

    return cave

#chosenCave in the checkCave method below could be potato
def checkCave(potato):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large Aardvark jumps out in front of you!!  He opens his jaws and...")
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if potato == str(friendlyCave):
        print("########################################")
        print("########################################")
        print("Yay!!  You just got some treasure fool!!")
        print("########################################")
        print("########################################")
    else:
        print("######################################")
        print("######################################")
        print("Well, you just got eaten!!  Sorry bro!")
        print("######################################")
        print("######################################")


#Below kicks off the whole game
#None of the methods get called until the lines below

play_again = "yes"
versions_of_yes = ("Yes", "yes", "y")

for a_yes_answer in versions_of_yes:
    while play_again == a_yes_answer:
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)
        play_again = input("Do you want to play again stupid?  (yes or no)")