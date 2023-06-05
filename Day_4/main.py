# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
sleep = input("How many hours do you sleep on average? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_left = int(age)
sleep_time = int(sleep)
years_left = 90 -(age_left)
days_left = years_left *365
weeks_left = years_left * 52
months_left = years_left *12
hours_left = years_left *24
sleep_time = hours_left *8
life_time_left = f"You have {years_left} years, {days_left} days, {weeks_left} weeks, and {months_left} months left"
print(life_time_left)