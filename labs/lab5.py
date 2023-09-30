#Write a ‘guess the number game’ where a random number is generated and the user must guess the number. The program says if their number is too high or too low until the right answer is guessed.


import random
randNumber = random.randint(0,100000)
print("guess the number that i am thinking right now: ")
try:
	userGuess = int(input())
	while randNumber != userGuess:
		if randNumber > userGuess:
			print("sorry you guessed too low try again")
			userGuess = int(input())
		elif randNumber < userGuess:
			print("sorry you guessed too high try again")
			userGuess = int(input())
		if randNumber == userGuess:
			print("congrats you guessed the right number which is " + str(randNumber))
except:
	print("unexpected error")