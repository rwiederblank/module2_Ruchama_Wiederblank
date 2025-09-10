"""
Minutes to Hours and Minutes
This program will converts the number of minutes the user puts in into hours and minutes remaining
"""


"""
the function: minutes_to_hours_and_minutes() will take input from the user for a number of minutes, and then calculate it into how many hours and how many minutes it is, and prints it for the user.
Steps:
1.Ask the user how many minutes they would like to calculate, and store as an integer in the variable minutes
2.create a variable hours and store in it the value of minutes divivded by 60
3.create variable minutes_left and have it equal to the remainder of minutes divided by 60
4. print how many hours and minutes can be extracted from the user's minutes entry
"""
def minutes_to_hours_and_minutes():
    minutes = int(input("How many minutes would you like to calculate? ")) #this stores the user input (number of minutes they want to calculat) as an integer
    hours = minutes // 60 #this stores the number of hours caluculated
    minutes_left = minutes % 60 #this stores the remainder of minutes left
    #print the results of the calculations
    print(minutes, " is ", hours, " hours and " , minutes_left, " minutes.")

#calls the function
minutes_to_hours_and_minutes()
