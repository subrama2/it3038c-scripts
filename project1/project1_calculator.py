def calculator():
	result = 0
	try:
		num1 = int(input("Enter first number: "))
		num2 =  int(input("Enter second number: "))
		whatToDo = str(input("how to calc: Enter(+,-,*,/): "))
		if whatToDo == "+":
			result = num1 + num2
			return result
		elif whatToDo == "-":
			result = num1 - num2
			return result
		elif whatToDo == "*":
			result = num1 * num2
			return result
		elif whatToDo == "/":
			result = num1 / num2
			return result
	except:
		print("unknown error happened")

print(calculator())

