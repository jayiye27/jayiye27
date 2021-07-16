import random

secret = random.randrange(1, 101)

guess = 0
tries = 0
print("I am thinking of a number between 1 and 100. Let's see if you can guess it! ")
while guess != secret:
    guess = int(input("Make your guess: "))
    tries = tries + 1

    if guess > secret:
        print("Too High! Try again")
    elif guess < secret:
        print("Too Low! Try again")
    else:
        print("Ding! You got it!", guess, "is correct!")

print("Number of tries:", tries)

