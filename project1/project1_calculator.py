'''
This is my Documentation:
I got creative ideas from
https://www.digitalocean.com/community/tutorials/how-to-make-a-simple-calculator-program-in-python-3 
but i changed the way it looks like and coded it a different way than it is shown here. I made
a calculator that does the basic arithmatic operations like add,minus,divide,or multiply.
The cool thing is you can use it to do these operations how many ever times as you can keep
inputting numbers to compute from. If you input 1 as num1 and 2 as num2 and state you
want to + then you should get 3 and its not shown right way as the program asks if you want
to compute more numbers and if say no then it shows the answer to being 3 as 1 + 2 = 3
and if you say yes then it uses 3 to compute with the next number inputed so if you enter
4 then the next result will be 7. After you run the code with the terminal of desktop it will
start up with asking you to enter first number.

The goal of the script is adding,suptracting, multiplying, dividing numbers.
example of the expectation of script:
first num = 1
second num = 4
operation is +
N to if you want to calculate more
result is 5

other scenario 
first num = 1
second num = 4
operation is +
Y to if you want to calculate more
next number 5
operation is *
result is 25

if you enter any other thing than expected it will return error and you will have to rerun script and enter
correct values.
so when it says to enter number, enter a number
when it say to enter operation please enter a operation shown in screen not something else

how to run the script in desktop powershell
download python and put it in path
then open terminal
go to the folder where the script is present
put the command: python project1_calculator
and then the script should run
'''

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

