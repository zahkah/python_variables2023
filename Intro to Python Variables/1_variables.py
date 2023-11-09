# Python Variables
import math

"""
	1.) Create three string variables called myName, parentName1 
	and parentName2 and assign them values. Then in a single sentence 
	print out "My name is X. My parents' names are Y and Z"
"""
print("\nQ 1.")
my_name = "zach"
parent_name1 = "Bob"
parent_name2 = "Mary"

print("My name is " + my_name + ". My parents' names are " + parent_name1 + " and " + parent_name2 + ".")
print(f"My name is {my_name}. My parents' names are {parent_name1} and {parent_name2}.")



"""
	2.) Create a string variable called petName and give it a string value. 
	Create an integer and call it petAge and assign it a value. Print the
	sentence "X is my pet and they are Y years old". Make sure to cast the
	petAge variable as a string before outputting the sentence.
"""
print("\nQ 2.")
pet_name = "Gizmo"
pet_age = 6

print(pet_name + " is my pet and they are " + str(pet_age) + " years old.")
print(f"{pet_name} is my pet and they are {pet_age} years old.")


"""
	3.) Four strings are provided below representing files. They have file 
	extensions such as .txt, .html and .js at the end. Print out each file name 
	without the file extension. Only remove the file extension from the end
"""
print("\nQ 3.")
s1 = "homework.txt"
s2 = "assignment2.html"
s3 = "main.js"
s4 = "js.mainjs.js"

print(s1[0:8])
print(s1.strip(".txt"))
print(s2.strip(".html"))
print(s3.strip(".js"))
print(s4.rstrip(".js"))



"""
	4.) Four strings are provided below. Update each one of the strings by
	removing all numbers that appear inside them and uppercase the first
	letter. Then in a single sentence print out each new string separated
	by commas e.g. Apple, Orange, Lemon, Tea
"""
print("\nQ 4.")
f1 = "ap12ple"
f2 = "oran454ge"
f3 = "9lem5on5"
f4 = "t12ea"

f1 = f1.replace("12", "").capitalize()
f2 = f2.replace("454", "").capitalize()
f3 = f3.replace("9", "").replace("5", "").capitalize()
f4 = f4.replace("12", "").capitalize()

print(f"{f1}, {f2}, {f3}, {f4}")



"""
	5.) Ask the user to type in their name using input(). Then replace
	all occurences of the letter "a" with "x", and print the following
	"Welcome Nxme! Your name is Y letters long." where Nxme is their 
	inputted converted name and Y is the number of characters in the name. 
	Note that the first letter is capitalized, all subsequent letters are 
	lowercase and all "a"s are replaced with "x".
"""
print("\nQ 5.")
name = input("Type in your name: ").lower().replace("a", "x").capitalize()

print("Welcome " + name + "! Your name is " + str(len(name)) + " letters long.")
print(f"Welcome {name}! Your name is {len(name)} letters long.")



"""
	6.) Create an integer called age and another called year and assign them 
	the values of your age and the current year. Then print a single
	sentence that says "My age is X and I was born in the year YYYY" where
	YYYY is year - age.
"""
print("\nQ 6.")
age = 40
year = 2022

print("My age is " + str(age) + " and I was born in the year " + str(year - age) + ".")
print(f"My age is {age} and I was born in the year {year - age}.")


"""
	7.) Do the exact same as above except this time ask the user to input their
	age and the current year
"""
print("\nQ 7.")


age_user = int(input("Type in your age: "))
year_user = int(input("Type in the year: "))

print("My age is " + str(age_user) + " and I was born in the year " + str(year_user - age_user) + ".")
print(f"My age is{age_user} and I was born in the year {year_user - age_user}.")


"""
	8.) There are two variables below representing a temperature in Celsius
	and one in Fahrenheit. Write code that converts the temperatures to the
	opposite scale and print 2 sentences reading "X degrees Celsius is Y degrees 
	Fahrenheit" and vice versa for the other one.
"""
print("\nQ 8.")
temp_fahrenheit = 32
temp_celsius = 25

converted_fahrenheit = (temp_fahrenheit - 32) * 5/9
converted_celsius = (temp_celsius * 9/5) + 32

print(f"{temp_fahrenheit} degrees F is {converted_fahrenheit} degrees C")
print(f"{temp_celsius} degree C is {converted_celsius} degrees F")



"""
	9.) Calculate the area of a circle that has a radius of 45.5cm. Use
	the correct and accurate value of a pi. Display this result like 
	"6503.882cm^2". Note the area is rounded to three decimal places
"""
print("\nQ 9.")
radius = 45.5
area = round(math.pi * pow(radius, 2), 3)

print(f"{area}cm^2")
