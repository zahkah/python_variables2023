# Python Conditionals

"""
	1.) Below, commented out, is an if else statement created with a
	lot of errors. Uncomment the code and fix the errors.
"""
print("\nQ 1.")

if 5 < 10:
	print("5 is less than 10")
else:
	print("5 is greater than 10")



"""
	2.) Use the bool variable called isMorning below and write an if else 
	statement that checks to see if isMorning is True. If it is True 
	then print "Good Morning". If it is False then print "Good Evening".
"""
print("\nQ 2.")

is_morning = True
if is_morning == True:
	print("Good Morning")
else:
	print("Good Evening")



"""
	3.) Create a bool called isCanadian and assign it a boolean value.
	Create another bool called hasBlackHair and assign it a boolean value.
	Write a conditional statement that will print the sentence "You are
	Canadian and have black hair" if both bools are True. If not, don't
	print anything.
"""
print("\nQ 3.")

is_canadian = True
has_black_hair = True

if is_canadian == True and has_black_hair == True:
	print("You are Canadian and have black hair")



"""
	4.) Ask the user to type in their name (input). Write code to check
	and see if their name:
	- is over 6 characters long
	- contains the letter "a"
	- contains the letter "c"
	If all of the above are true print "You have a long name that contains a and c"
"""
print("\nQ 4.")

name = input("What is your name?: ")
name_length = len(name)

if name_length > 6 and "a" in name and "c" in name:
	print("You have a long name that contains a and c")

# This is a bit more long winded
if name_length > 6:
	if "a" in name:
		if "c" in name:
			print("You have a long name that contains a and c")



"""
	5.) Create a string called day and assign it a value of one of
	the names of the day of the week e.g. "Wednesday". Write a
	conditional statement that will check your variable and print
	either "X is a work day" or "X is a weekend day" where X is
	your day variable.
"""
print("\nQ 5.")

day = "monday".lower()
all_week_days = "monday-tuesday-wednesday-thursday-friday"

# System 1
if day in all_week_days:
	print(f"{day} is a work day")
elif day == "saturday" or day == "sunday":
	print(f"{day}  is a weekend day")
else:
	print(f"{day}  is not a day")


# System 2
# A bit longer
if (day == "monday" or day == "tuesday" or
	day == "wednesday" or day == "thursday" or
	day == "friday"):
	print(day + " is a work day")
else:
	print(day + " is a weekend day")



"""
	6.) The int variable below called current_hour represents an
	hour on the 24 hour clock e.g. either 0 - 23. Write code that
	asks the user to input a number between 0 and 23 to become
	current_hour. If this number cannot be turned into an int, 
	automatically assign it the value of 0. 
	0 to 12 inclusive = "Morning time"
	13 to 16 inclusive = "Afternoon time"
	17 to 20 inclusive = "Evening time"
	21 to 23 inclusive = "Night time"
	any number < 0 or > 23 = "No time"
	Change the current_hour value to make sure all of your code
	is correct
"""
print("\nQ 6.")

current_hour = input("What hour (0-23) is it?: ")
dont_do_this_way_number_string = "0-1-2-3-4-5-6-7-8-9-10-11-12"

try:
	current_hour = int(current_hour)
except:
	current_hour = 0

if current_hour >= 0 and current_hour <= 12:
	print("Morning time")
elif current_hour >= 13 and current_hour <= 16:
	print("Afternoon time")
elif current_hour >= 17 and current_hour <= 20:
	print("Evening time")
elif current_hour >= 21 and current_hour <= 23:
	print("Night time")
else:
	print("No time")





if 0 <= current_hour <= 12:
	print("Morning time")
elif 13 <= current_hour <= 16:
	print("Afternoon time")
elif 17 <= current_hour <= 20:
	print("Evening time")
elif 21 <= current_hour <= 23:
	print("Night time")
else:
	print("No time")



"""
	7.) Below is a nested conditional statement - one where ifs
	are inside other ifs. It is written with some errors. Uncomment
	the code and fix it so that it will work correctly.
"""
print("\nQ 7.")

age = 23
has_money = True

if age >= 19:
	print("You are old enough")
	if has_money == True:
        print("You can buy alcohol")
	else:
		print("You cannot buy alcohol")
else:
	print("You are not old enough to buy alcohol")



"""
	8.) This question is similar to question 6 however this time
	you are dealing with an Am and PM clock time. The variable
	am_pm_time contains the value in a string "4pm"
	
	Print the following based on the value of currentHour
	12am to 12pm inclusive = "Morning time"
	1pm to 4pm inclusive = "Afternoon time"
	5pm to 8pm inclusive = "Evening time"
	9pm to 11pm inclusive = "Night time"

	Change the am_pm_time value to make sure all of your code
	is correct
"""
print("\nQ 8.")

am_pm_time = "4pm"

am_or_pm = am_pm_time[-2:]
num = am_pm_time.replace(am_or_pm, "")

num = int(num)

if am_or_pm == "am" or am_pm_time == "12pm":
	print("Good Morning")
elif num >= 1 and num <= 4:
	print("Afternoon time")
elif num >= 5 and num <= 8:
	print("Evening time")
elif num >= 9 and num <= 11:
	print("Night time")
else:
	print("MISTAKE")



