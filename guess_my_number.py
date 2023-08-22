import random

guess_range = input("Type a number: ")

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
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess <= 0:
            print("Enter a positive number!")
            quit()
    else:
        print("Enter a number!")
        quit()
        


print(random_num)