def calculator():
	result = 0
	try:
		num1 = int(input("Enter first number: "))  #1
		num2 =  int(input("Enter second number: "))  #2
		num3 = 0
		counter = 1
		repeat = True
		whatToDo = str(input("how to calc: Enter(+,-,*,/): "))  # +
		while repeat == True:
			if whatToDo == "+":
				if counter > 1:
					result = result + num3
				else:
					result = num1 + num2
				#return result
			elif whatToDo == "-":
				if counter > 1:
					result = result - num3
				else:
					result = num1 - num2
				#return result
			elif whatToDo == "*":
				if counter > 1:
					result = result * num3
				else:
					result = num1 * num2
				#return result
			elif whatToDo == "/":
				if counter > 1:
					result = result / num3
				else:
					result = num1 / num2
				#return result
			else:
				return "you have inputted invalid operator choose +,-,*,/  next time"
			response = str(input("Do you want to compute another number: [Y/N] ")).upper()
			if response == "Y":
				num3 = int(input("Enter Next number: ")) # Result = 7 and num3 = 4 
				whatToDo = str(input("how to calc: Enter(+,-,*,/): "))  # result + operation
				counter += 1
			elif response == "N":
				repeat = False
				return "the answer is " + str(result)
			else:
				return "error occured as response is inputted incorrectly try again"
				
	except:
		return "unknown error happened"

print(calculator())

