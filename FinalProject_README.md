# Documentation:

I coded this without an external resource just used api key from openweather and just wanted to create an task tracker with a weather function
that allows any adult to keep track of their tasks while knowing when to do
them by and the order they should do them by. I feel this program is useful because for college students
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
ex: Here you have to put your api key which i am cutting as i put mine in there currently. It can be seen that you can filter tasks and  you are able to get it to state specific tasks or all by choosing the none option for filter which will show all of the tasks by default. As we entered many different outdoor tasks but it is stating only the filtered task for the outdoor aspect.

![image](https://github.com/subrama2/it3038c-scripts/assets/84252650/f7434dae-af0b-45af-b56b-548c1bbf4f24)

![image](https://github.com/subrama2/it3038c-scripts/assets/84252650/a70c2bf9-72fe-4826-92ed-c9b42be22803)

After that you are able to complete a task by choosing 4 and inputting that and if you check your tasks again that marked task wont be there:
ex:

![image](https://github.com/subrama2/it3038c-scripts/assets/84252650/274743b2-5a4c-4703-b2ac-6c32297223cc)

# steps to run
enter 1 to start the program when you are given the options then enter how many tasks you need to be put in your todolist, then be ready to put details about them like name which can be anything, then put how important it is to get this done or the priority level which is 3 options and any other will lead you to get a repeating message of invalid value and you have to enter again and after that you have to enter when the due date is in the format shown in the prompt or it will make you go back to options screen and you will have reenter the tasks again from step 1. After that you enter task category like is it work, school, grocery related. THen you enter the location again will you do it at home, college, walmart and last add any notes to the task that you need to keep in there.After that you will be led back to option screen which will allow you to view all the tasks by due date descending from the earliest due date. Then you can enter 3 to get asked if you want to filter based on category and you can say none to get all tasks or choose one category that you inputted above which will show just that task and then you will be asked what city you are in which implements an api which then will ask you to enter api key which you will have to get by creating a free acount which is shown in the link below and after that you will get a suggestion to postpone based on weather api or to do it. After that if enter 4 you can mark a task completed which will then not appear in the all tasks option above. Then enter 5 to end program.

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
