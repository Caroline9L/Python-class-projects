# def string_length(str):
# 	str = "blah blah blah"
# 	return len(str)

# print(string_length(str))


# def string_length(str):
# 	return len(str)

# print(string_length("blah blah"))


def string_length(string):
    if type(string) == int:
		print("Numbers won't work")
	elif type(string) == float:
        print("Numbers won't work")
	else:
        return len(string)

