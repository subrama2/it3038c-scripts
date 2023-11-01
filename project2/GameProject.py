#importing modules
import random

list1 = [0,1,2]
winC = 0
loseC = 0
drawC = 0
repeat = True
print("welcome to 2 game")
while repeat == True
gameChoice = str(input("Do you want to play rock,paper,scissors [rps] or choose right number game [n] (Enter one of the two of whats is in bracket):  "))

if(gameChoice == "rps"):
	playerChoice = str(input("do you choose rock [r], paper [p], or scissors [s]: "))
	cpuchoice = random.choice(list1)
	if cpuchoice == 0:
		#print("compter chooses rock")
		if playerChoice == "r":
			print("its a tie  [rock draws against rock]")
			drawC+=1
		elif playerChoice == "p":
			print("its a win congrats  [rock gets covered by paper]")
			winC+=1
		else:
			print("its a loss [rock smashes scissors]")
			loseC+=1
			
	elif cpuchoice == 1:
		#print("computer chooses paper")
		if playerChoice == "r":
			print("its a loss [paper covers rock]")
			loseC+=1
		elif playerChoice == "p":
			print("its a tie  [paper draws against paper]")
			drawC+=1
		else:
			print("its a Win [scissors cuts paper]")
			winC+=1
	else:
		#print("scissors")
		if playerChoice == "r":
			print("its a win congrats [rock breaks scissors]")
			winC+=1
		elif playerChoice == "p":
			print("its a loss  [paper gets cut by scissors]")
			loseC+=1
		else:
			print("its a draw [scissors draws against scissors]")
			drawC+=1
	
else:
	print("Thanks for playing")
print("You won ", winC, "time(s) but lost ", loseC, "time(s) but you draw ", drawC, " time(s) out of playing both rps, and n")
