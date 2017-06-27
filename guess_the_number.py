import random

guesses = 0

name = input("What is your name? ")

number = random.randint(1,20)
print("")
print("Well {}, I'm thinking of a number between 1 and 20.".format(name))
print("------------------")
print("")

while guesses < 4:
    print("Please take a guess:")
    guess = input()
    guess = int(guess)
    #Obviously, your math won't work unless you convert guess into an integer.  It arrives as a string

    guesses += 1

    if guess < number:
        print("Your guess is too low!!")

    if guess > number:
        print("Your guess is too high!!")

    if guess == number:
        break

if guess == number:
    good_responses = ("Great job {}.  What are you, some kind of freakin genius?", 
    "Great job {}!  You so smat!!", 
    "I'm so proud of you {}, and so is your mom!  Your dad is still disappointed!!", 
    "This game is too easy {}, so don't start thinkin you're the shit!", 
    "I made this game extremely easy for you {} because you need a confidence boost!",
    "Wow, you got it {}, you fine-ass nerd!!",
    "Well aren't you smart {}.  Just know that you will never be smarter than Talbot Lawrence!!")

    print("")
    print(random.choice(good_responses).format(name))
    print("")

if guess != number:
    bad_responses = ("You're an idiot {}!!  The number was {}.  Not even your parents admit that you're theirs!!",
    "Oh dear {}, the number was {}!!  What were you thinking??",
    "{}, the number was {}.  Are your parents cousins??",
    "What's the matter with you {}??  The number was {}!  Get your head out of your ass!!",
    "Oh dear {}!!  The number was {}.  How many versions of stupid are you??")

    print("")
    print(random.choice(bad_responses).format(name, number))
    print("")