username = input("What's your name? ")
print("Welcome", username + "!")

answer = input("You are on the road! Which way would you like to turn left or right? ").lower()

if answer=='left':
	answer = input("You see an apple in front of you! Type eat to eat it or leave to keep going! ").lower()
	if answer == "eat":
		print("Now you have energy to keep going! :) ")

		answer = input("You walk for a long time and now there's a river on your way! Type bridge if you want to go across the bridge and swim if you want to swim across! ").lower()

		if answer == 'swim':
			print("You ran out of energy and couldn't swim! Sorry, but you lose :) ")
		
		if answer == 'bridge':
			print("You're on the other side of river! Good job! :) ")

			answer = input("Now there's a car in front of you! Type drive to use a car or leave to keep going! ").lower()

			if answer == "car":
				print("There's only enough fuel to get you home! Sorry, but adventure is over! :) ")
			
			if answer == "leave":
				print("You walked for too long and ran out of energy! Sorry, but you lose! :( ")

	if answer == "leave":
		print("You ran out of energy and collapsed! Sorry, but you lose :( ")

elif answer == 'right':
	print("You shoul've turned left! :( ")
	print("Sorry, but game over!")

else:
	print("No a valid answer. You lose! :( ")