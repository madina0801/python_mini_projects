print("Welcome to the Capitals quiz!")

playing = input("Do you want to play? Y / N: ")

if playing != "Y":
    quit()

score = 0

answer = input("Capital of Austria: ")
if answer == "Vienna":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Capital of Bulgaria: ")
if answer == "Sofia":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Capital of Canada: ")
if answer == "Ottawa":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Capital of Norway: ")
if answer == "Oslo":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Capital of Japan: ")
if answer == "Tokyo":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("You got " + str(score) + " question correct!")
print("You got " + str(score/5 * 100) + "%")