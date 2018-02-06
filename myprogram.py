"""
Some documentation that goes between 3 " marks 
"""
# _greeting = "Hello"
# age = input("Enter your age:")
# new_age = int(age) + 50
# print(new_age)


# as function: 

# def new_age(age):
# 	my_age = float(age) + 50
# 	return my_age

# age = input("Please enter your age: ")
# print(new_age(age))


#with conditionals:

# def new_age(age):
# 	my_age = float(age) + 50
# 	return my_age

# age = input("Please enter your age: ")

# if float(age) < 150:
# 	print(new_age(age))
# else: 
# 	print("How is that possible?")

#or:

def new_age(age):
	my_age = age + 50
	return my_age

age = float(input("Please enter your age: "))


if age < 150:
	print(new_age(age))
else: 
	print("How is that possible?")