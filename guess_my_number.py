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

random_num = random.randint(guess_range)

print(random_num)