# importing modules
import requests
from datetime import datetime, timedelta
# list where we can store our tasks
tasks = []

#function where i ask for the tasks via input and do validation to make to sure they answer properly
def setTasks():
  try:
    numOfTasks = int(input("How many tasks do have scheduled today: "))
  except ValueError:
    print("Invalid input. please enter a valid number")
    return

  for task in range(numOfTasks):
    taskName = input("Please Enter task name: ").lower()
    importance = str(input("Enter priority of the task: (High,Medium,Low) ")).lower()
    while importance not in ["high", "medium", "low"]:
      print("Invalid priority. please enter either high, medium, or low.")
      importance = str(input("Enter priority of the task: (High,Medium,Low) ")).lower()

    taskDueDateStr = str(input("Enter when the task is due or needs to be completed by format(YYYY-MM-DD HH:MM): "))
    try:
      dueDate = datetime.strptime(taskDueDateStr, "%Y-%m-%d %H:%M")
    except ValueError:
      print("Invalid date format. please enter the date in correct format.")
      return
    category = str(input("enter task category ex: school, bill: ")).lower()
    location = str(input("enter task location ex: [home, college, grocery,etc] ")).lower()
    note = str(input("Enter notes for task if any: "))
    #adding each task to the tasks list via as a dictionary
    tasks.append({"name":  taskName, "priority": importance, "Due Date": dueDate, "category": category, "location": location, "Notes": note })
#displaying tasks via by due date and using the due date key to do that and then printing each task and its details to the users
def displayTasks(task_list):
  tasks.sort(key=lambda x: x["Due Date"])
  print("upcoming tasks: ")
  for task in tasks:
    print(f"Name: {task['name']}, priority: {task['priority']}, Due Date: {task['Due Date']}, category: {task['category']}, location: {task['location']}, Notes: {task['Notes']}")
#asking user input to mark tasks as complete and removing from tasks list/dictionary
def markedComplete():
  # adding the option to mark tasks completed and doing validation to make sure the task is removed and that it is present to be removed
  completedTask = input("\n enter a name of a completed task or 'none' if none: ")
  if completedTask.lower() != 'none':
    taskFound = False
    for task in tasks:
      if task['name'].lower() == completedTask.lower():
        tasks.remove(task)
        print(f"{completedTask} marked as completed")
        taskFound = True
        break
    if not taskFound:
      print(f"task {completedTask} not found. please enter valid task that is completed")



#weather implementation based on location
def checkWeather(filteredTasks):
  outdoor_tasks = [task for task in filteredTasks if not'home' in task['location'].lower()]
  if outdoor_tasks:
    apiKey = input("please enter your api key in here: ")
    city = input("enter your city: ")
    #url used to get our weather data via api key
    baseurl = "http://api.openweathermap.org/data/2.5/weather"
    param = {"q": city, "appid" : apiKey, "units": "metric"}
    # try except to make sure no errors come from getting a response back from api
    try:
      response = requests.get(baseurl,params=param)
      data = response.json()
      #making sure the response is successful and if it is print the results relating to the city detailed
      if response.status_code == 200:
        temp,weatherdescription = data['main']['temp'], data['weather'][0]['description']
        print(f"\n current weather in {city}: ")
        print(f"\n current temperature in {city} ")
        print(f"\n weather: {weatherdescription} ")
        #if weather not sunshine then it is assumed to be not good and program suggests to maybe postpone it if outdoor activity
        for task in outdoor_tasks:
          if "sunshine" not in weatherdescription.lower():
            print(f"Suggestion for User: consider postponing the outdoor task '{task['name']}' due to {weatherdescription} weather")
          else:
            print(f"perfect weather for User to do outdoor task '{task['name']}'.")
      else:
        print(f"error: {data['message']}")

    except requests.RequestException as e:
      print(f"error {e}")
#main loop that calls all functions and breaks when exiting program
while True:
  print("\n Choose An option: ")
  print("1. Enter Tasks ")
  print("2. Display All Tasks")
  print("3. Check Weather for tasks ")
  print("4. Mark a task as complete ")
  print("5. Exit")


  try:
    choice = int(input("enter your choice (1-5): "))
  except:
    print("you inputted a non valid input please put valid input")


  if choice == 1:
    setTasks()
  elif choice == 2:
    displayTasks(tasks)
  elif choice == 3:
    #filtering tasks to categories
    selectedCategory = input("enter a task category to filter tasks displayed or 'none' for all: ").lower()
    filteredTasks = tasks if selectedCategory.lower() == 'none' else [task for task in tasks if task['category'].lower() == selectedCategory.lower() ]
    filteredTasks.sort(key=lambda x: x["Due Date"])
    print("\n tasks that are filtered by user chosen category:")
    for task in filteredTasks:
      print(f"Name: {task['name']}, Priority: {task['priority']}, Due Date: {task['Due Date']}, Category: {task['category']}, Location: {task['location']}, Notes: {task['Notes']}")
    checkWeather(filteredTasks)
  elif choice == 4:
    markedComplete()
  elif choice == 5:
    print("\nExiting program")
    break
  else:
    print("Invalid choice. please enter a number between 1-5. ")






