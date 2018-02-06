import json
from difflib import get_close_matches

# def load_dict():
# 	data = json.load(open('data.json'))
# 	print(data)

# load_dict()

data = json.load(open('data.json'))

def translate(word):
    # or word = word.lower()
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		yn = input("Not found - did you mean %s? Y or N: " % get_close_matches(word, data.keys())[0])
        # return "Did you mean " + (get_close_matches(word, data.keys(), cutoff=0.8)[0]) + "?"
		if yn == "Y":
			return data[get_close_matches(word, data.keys())[0]]
		elif yn == "N":
			return "That is not a word, please check your spelling"
		else:
			return "That is not a valid reply."
	else:
		return "Please pick a REAL word."

word = input("Enter a word: ").lower()

# print(translate(word))

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
