"""
We'll build a basic calendar that the user will be able to interact with from the command line. The user should be able to choose to:

View the calendar
Add an event to the calendar
Update an existing event
Delete an existing event
"""

#converts a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument.
from time import sleep, strftime

user_first_name = raw_input("Enter your 1st name: ")

# Ideally, a calendar allows users to at least associate an event with a date, as a pair.
calendar = {}

def welcome():
  print "Welcome " + user_first_name + "."
  print "Calendar is loading..."
  sleep(1)
  print "Today is: " + strftime("%A %B, %Y")
  print "Current time is: " + strftime("%H:%M:%S")
  sleep(1)
  print "What would you like to do?"
welcome()

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Enter One of the following letters:    A = Add, U = Update, V = View, D = Delete or X = Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "Calendar is empty."
      else:
        print calendar 
    elif user_choice == "U":
        date = raw_input("What's the date? ")
        update = raw_input("Enter the update: ")
        calendar[date] = update
    elif user_choice == "A":
        event = raw_input("Enter event: ")
        date = raw_input("Enter date (MM/DD/YYYY): ")
        if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
            print "Invalid date has been intered."
            try_again = raw_input("Would you like to try again? Y for Yes, N for No: ")
            try_again = try_again.upper()
            if try_again == "Y":
                continue
            else: 
                start = False
        else:
            calendar[date] = event
            print "Added successfully."
            print calendar
    elif user_choice == "D":
        if len(calendar.keys) < 1:
            print "Calendar is empty."
        else:
            event = raw_input("What event? ")
            for date in calendar.keys():
                if event == calendar[date]:
                    del calendar[date]
                    print "Successfully deleted."
                    print calendar
                else:
                    print "Incorrect event was specified."
    elif user_choice == "X":
        start = False
    else:
        print "Invalid command was entered!"
start_calendar() 



    
  
  