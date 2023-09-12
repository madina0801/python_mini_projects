password = input("What is the master password? ")

mode = input("Would you like to add a new password or view existing ones? (view/add) or q to quit ").lower()

def view():
	pass

def add():
	pass

while True:
	if mode == 'q':
		break
	elif mode == 'view':
		view()
	elif mode == 'add':
		add()
	else:
		print("Invalid mode!")
		continue