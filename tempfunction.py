# def converter(celsius):
# 	fahrenheit = float(celsius) * (9/5) + 32
# 	return fahrenheit

# celsius = input("Please enter temp in celsius: ")
# print(converter(celsius))

# # if/else:
# def converter(celsius):
#     fahrenheit = float(celsius) * (9 / 5) + 32
#     return fahrenheit

# celsius = input("Please enter temp in celsius: ")

# if float(celsius) < -273.15:
#     print("Nice try, but nothing can be colder than absolute zero!")
# else:
#     print(converter(celsius))

# while loop:
# temperatures = [10, -20, -289, 100]

# for temp in temperatures:
#     if float(temp) < -273.15:
#         print("Nice try, but nothing can be colder than absolute zero!")
#     else:
#         fahrenheit = float(temp) * (9 / 5) + 32
#         print(fahrenheit)

# class solution:
temperatures = [10, -20, -289, 100]
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c * 9 / 5 + 32
        return f
for t in temperatures:
    print(c_to_f(t))