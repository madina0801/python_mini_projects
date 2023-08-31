import random

user_score = 0
computer_score = 0
options = ['rock', 'paper', 'scissors']

while True:
	user_choice = input("Rock/Paper/Scissors or !! to quit: ").lower()

	if user_choice == "!!":
		break

	if user_choice not in options:
		continue

	random_num = random.randint(0, 2)

	# rock - 0, paper - 1, scissors - 2
	computer_choice = options[random_num]
	print("Computer choice is", computer_choice + '.')
	
	if user_choice == 'rock' and computer_choice == 'scissors':
		print("You won!")
		user_score += 1

	elif user_choice == 'paper' and computer_choice == 'rock':
		print("You won!")
		user_score += 1

	elif user_choice == 'scissors' and computer_choice == 'paper':
		print("You won!")
		user_score += 1

	else:
		print("Computer won!")
		computer_score += 1

print("You won", user_score, "times.")
print("Computer won", computer_score, "times.")
print("Goodbye!")