import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#print(names) output will be a list of Names.

number_of_names = (len(names))
print(names)
random_number = random.randint(0, number_of_names-1)

who_will_pay = names[random_number]
print(who_will_pay + " is going to buy the meal today!")