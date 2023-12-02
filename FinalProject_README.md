# Documentation:

I coded this without an external resource and just wanted to create an task tracker with a weather function
that allows any adult to keep track of their tasks while knowing when to do
them by and the order they should do them by. It is useful because for college students
like me time management is hard and with this program that becomes a little bit easier
and also this program helps to track tasks with due dates and it becomes one 
area where people or students can manage their tracks without worries. The program
priortises based of date due and how urgent it needs to be done which is decided by user of program

# example of the expectation of script:

After you run the TaskCheckList.py in terminal it will start off by allowing you to have 5 options: 
1. Enter Tasks
2. Display All Tasks
3. Check Weather for tasks
4. Mark a task as complete
5. Exit

Here you have to input 1-5 where 1 allows you to add how many ever tasks you want and after you add it will go back to the options screen:
ex:
![image](https://github.com/subrama2/it3038c-scripts/assets/84252650/779887d4-1832-450a-b2e2-40dc018291ac)
Next you are able to input 2 to see what tasks you have scheduled:
ex:
![image](https://github.com/subrama2/it3038c-scripts/assets/84252650/2705704d-b750-47db-a600-153cbedf2e37)
Then you are able to input 3 to check weather and if you have any outdoor tasks like grocery and the weather is bad the program will suggest to postpone it
ex: Here you have to put your api key which i am cutting as i put mine in there currently
![image](https://github.com/subrama2/it3038c-scripts/assets/84252650/f7434dae-af0b-45af-b56b-548c1bbf4f24)
![image](https://github.com/subrama2/it3038c-scripts/assets/84252650/a70c2bf9-72fe-4826-92ed-c9b42be22803)
After that you are able to complete a task by choosing 4 and inputting that and if you check your tasks again that marked task wont be there:
ex:
![image](https://github.com/subrama2/it3038c-scripts/assets/84252650/274743b2-5a4c-4703-b2ac-6c32297223cc)



The goal of the script is having a task manager that helps keep stay on top of things in their life as that is a common problem for everyone having to much stuff to do and not knowing if you
forgot to do something or not.


if you enter any other thing than expected it will return error and it will keep asking you until you enter acceptable values

how to run the script in desktop powershell:
download python and put it in path
then open terminal
go to the folder where the script is present
then enter this command pip install requests 
to install the required module for the program in terminal
then sign up on [openweathermap](https://home.openweathermap.org/)
to obtain a free api key which you will need to run this program
put the command: python TaskCheckList.py
and then the script should run
'''
