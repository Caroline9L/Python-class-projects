# password = ''
# while password != 'python123':
# 	password = input("Enter password: ")
# 	if password == 'python123':
# 		print("You are logged in")
# 	else: 
# 		print("Sorry, try again")

names = ['John', 'Jack', 'Bill']
email_domains = ['gmail.com', 'hotmail.com', 'yahoo.com']

for i, j in zip(names, email_domains):
	print(i, j)