import random

guess_range = input("Type a number: ")
guesses = 0

if guess_range.isdigit():
    guess_range = int(guess_range)
    
    if guess_range <= 0:
        print("Enter a positive number!")
        quit()
else:
    print("Enter a number!")
    quit()

random_num = random.randint(0, guess_range)

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a number!")
        continue

    if user_guess == random_num:
        print("You got it right!")
        break
    else:
        if user_guess > random_num:
            print("You were above the number!")
        else:
            print("You were below the number!")

print("You got it in", guesses, "guesses")