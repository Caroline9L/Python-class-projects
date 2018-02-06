# def minutes_to_hours(minutes):
# 	hours = minutes / 60
# 	return hours

# def seconds_to_hours(seconds):
# 	hours = seconds / 3600
# 	return hours

# print(minutes_to_hours(90) + 10)
# print(seconds_to_hours(70))

def minutes_to_hours(minutes, seconds):
	hours = minutes / 60 + seconds / 3600
	print(hours) #this won't produce a number, so the result can't be fiddled with as on 9
# 	return hours #this will return a value that can be worked with but needs to be printed in call

# print(minutes_to_hours(90, 120))
minutes_to_hours(90, 120)