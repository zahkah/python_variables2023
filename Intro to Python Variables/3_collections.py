# Python Collections

"""
	1.) Below, commented out, are 4 collections. A list, tuple, set and 
	dictionary. They are created with errors. Uncomment the code, fix the 
	errors and print each one along with its type e.g. type(myList).
"""
print("\nQ 1.")

my_list = ["list", "tuple", "set", "dictionary"]
my_tuple = ("cannot", "change", "a", "tuple")
my_set = {"no", "duplicates", "allowed", "here"}
my_dict = {"string": "word", "number": 1, "boolean": True}

print(my_list, type(my_list))
print(my_tuple, type(my_tuple))
print(my_set, type(my_set))
print(my_dict, type(my_dict))



"""
	2.) Below is a list called colours. Add 2 new colours to the list and
	remove the first colour from it. Then print the entire list and after
	print the the following "There are X colours in my list" where X is
	the number of elements in your list.
"""
print("\nQ 2.")

colours = ["red", "green", "brown", "white"]
colours.pop(0)
colours.extend(["purple", "black"])

print(colours)
print(f"There are {len(colours)} colours in my list")



"""
	3.) Create a tuple called carBrands with 5 strings in it representing
	different car companies. In separate print(), print out:
	- the first element in your tuple
	- the third and fourth element in your tuple
	- the last element in your tuple
	- the first, third and fifth element in your tuple
"""
print("\nQ 3.")

car_brands = ("VW", "Toyota", "Honda", "Ferrari", "Ford")

print(car_brands[0])
print(" ".join(car_brands[2:4]))
print(car_brands[-1])
print(" ".join(car_brands[::2]))



"""
	4.) Create a list and store 3 country names inside it as strings.
	Ask the user using an input to add a new country into the list. If
	the country name doesn't appear in the list, add it in. If it already
	is in the list then insert it in in capital letters. Print out your 
	list at the end to see the effect,
"""
print("\nQ 4.")

countries = ["America", "Canada", "Mexico"]
user_country = input("Add a new country: ")

if user_country in countries:
	countries.append(user_country.upper())
else:
	countries.append(user_country)

print(countries)



"""
	5.) Below you will find a large list containing numerous numbers. 
	Write code to check and see if the number 13 is present in 
	it. If it is, remove it from the list. Print how many items
	are in this list. Then cast the list to a set to remove any duplicate
	items that may be present. Then print the new number of items in
	the list now that all duplicates have been removed.
"""
print("\nQ 5.")

huge_list = [54, 22, 111, 5, 
			22, 22, 67, 6, 99, 99, 
			20, 67, 90, 123, 110, 
			4, 18, 19, 111, 77, 6, 
			54, 81, 80, 13, 38]

if 13 in huge_list:
	huge_list.remove(13)

print(len(huge_list))

huge_list_no_duplicates = set(huge_list)

print( len(huge_list_no_duplicates) )



"""
	6.) Remove all duplicates from the names list below and then
	print each name in alphabetical order separated by the following
	characters " -- "
"""
print("\nQ 6.")

names = ["james", "mark", "mary", "paul", "mark", "aaron", "mary", "mark"]
names = set(names)
names = list(names)
names.sort()
print(" -- ".join(names))



"""
	7.) Create a colletion variable that holds the names of 4 of your
	friends paired with their phone number. Decide between a list,
	tuple, set or dictionary to create this. Then, using one of your 
	friend's names, print their name along side their number
"""
print("\nQ 7.")

phone_book = {"james": 1234567, "mark": 7654321, "mary": 1726354, "paul": 1123456}
print("mark => " + str(phone_book["mark"]))


"""
	8.) Below is a dictionary containing some of the richest people in 
	the world along side their net worth. They are randomly ordered. 
	Write code to print out the following: "X is the richest person with
	$YYY. Z is the poorest person with $WWW" where YYY and WWW is the
	number of dollars they have.
"""
print("\nQ 8.")

worlds_richest = {
	"Bernard Arnault": 196000000000, 
	"Bill Gates": 137900000000, 
	"Elon Musk": 278700000000, 
	"Jeff Bezos": 200500000000,
	"Larry Ellison": 127100000000, 
	"Larry Page": 124700000000
}
# Get list of money and people only
wealth = list(worlds_richest.values())
people = list(worlds_richest.keys())

# Sort money from lowest to highest
wealth_ordered = sorted(wealth)

# Extract highest and lowest values
wealthiest_value = wealth_ordered[-1]
poorest_value = wealth_ordered[0]

# Get the position of richest and poorest 
# and use that to get the person
wealthiest_pos = wealth.index(wealthiest_value)
wealthiest_person = people[wealthiest_pos]

poorest_pos = wealth.index(poorest_value)
poorest_person = people[poorest_pos]

# Output the result
msg = f"{wealthiest_person} is the richest person with ${worlds_richest[wealthiest_person]}\n"
msg += f"{poorest_person} is the poorest person with ${worlds_richest[poorest_person]}"

print(msg)