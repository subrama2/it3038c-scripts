#importing modules
import random

list1 = [0,1,2]
winC = 0
loseC = 0
chances = 5
drawC = 0
playagain = ""
repeat = True
try:
	print("welcome to two game collection")
	while repeat == True:
		gameChoice = str(input("Do you want to play rock,paper,scissors [rps] or choose right number game [n] (Enter one of the two of whats is in bracket):  ")).lower()
		if(gameChoice == "rps"):
			playerChoice = str(input("do you choose rock [r], paper [p], or scissors [s]: ")).lower()
			cpuchoice = random.choice(list1)
			if cpuchoice == 0:
				#print("compter chooses rock")
				if playerChoice == "r":
					print("its a tie  [rock draws against rock]")
					drawC+=1
				elif playerChoice == "p":
					print("its a win congrats  [rock gets covered by paper]")
					winC+=1
				elif playerChoice == "s":
					print("its a loss [rock smashes scissors]")
					loseC+=1
				else:
					print("you have inputted incorrect or invalid choice try again")
					
			elif cpuchoice == 1:
				#print("computer chooses paper")
				if playerChoice == "r":
					print("its a loss [paper covers rock]")
					loseC+=1
				elif playerChoice == "p":
					print("its a tie  [paper draws against paper]")
					drawC+=1
				elif playerChoice == "s":
					print("its a Win [scissors cuts paper]")
					winC+=1
				else:
					print("you have inputted incorrect or invalid choice try again")
			else:
				#print("scissors")
				if playerChoice == "r":
					print("its a win congrats [rock breaks scissors]")
					winC+=1
				elif playerChoice == "p":
					print("its a loss  [paper gets cut by scissors]")
					loseC+=1
				elif playerChoice == "s":
					print("its a draw [scissors draws against scissors]")
					drawC+=1
				else:
					print("you have inputted incorrect or invalid choice try again")
				
		elif gameChoice == "n":
			randomNumber = random.randrange(1,10000)
			print("Here is a hint for the game the number is between: ", randomNumber-10, "-", randomNumber+10)
			while chances != 0:
				print("you have", chances ," chance(s) to guess left")
				GuessNum = int(input("guess the number i am thinking it: "))
				if 	randomNumber == GuessNum:
					winC+=1
					print("congrats you guessed right the number is ", GuessNum)
					break
				else:
					if chances == 1:
						loseC+=1
						print("sorry you guessed wrong the actual number is ", randomNumber)
						break
					print("sorry you guessed wrong try again")
					chances -= 1	
		else:
			print("you have inputted incorrect or invalid choice try again")
		playagain = input("do you want to play rps or number guess game again [y/n]: ")
		if playagain == "n":
			repeat = False
	print("Thanks for playing")
	print("You won ", winC, "time(s) but lost ", loseC, "time(s) and you draw ", drawC, " time(s) out of playing both rps, and n")
except:
	print("Unknown error occured")