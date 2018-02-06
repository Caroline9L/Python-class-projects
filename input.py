# planet = input("What planet are you from? ")
# print(planet)

def currency_conv(rate, euros):
    dollars = euros * rate
    return dollars
r = input("Enter rate: ")
e = input("Enter Euros: ")

print(currency_conv(float(r), float(e)))

#or
# r = float(input("Enter rate: "))
# e = float(input("Enter Euros: "))

# print(currency_conv(r, e))