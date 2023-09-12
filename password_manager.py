password = input("What is the master password? ")

mode = input("Would you like to add a new password or view existing ones? (view/add) or q to quit ").lower()

while True:
	if mode == 'q':
		break
	elif mode == 'view':
		pass
	elif mode == 'add':
		pass
	else:
		print("Invalid mode!")
		continue