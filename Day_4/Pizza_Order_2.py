# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == "S":
    price = 15
    if add_pepperoni == "Y":
        price += 2
        print(f"Your final bill is ${price}")
    else:
        print(f"Your final bill is ${price}")
    if extra_cheese == "Y":
            price += 3
            print(f"Your final bill is ${price}")
    else:
        print(f"Your final bill is ${price}")

elif size == "M":
    price  = 20
    if add_pepperoni == "Y":
        price += 3
        print(f"Your final bill is ${price}")
    else:
        print(f"Your final bill is ${price}")
    if extra_cheese == "Y":
        price += 4
        print(f"Your final bill is ${price}")
    else:
        print(f"Your final bill is ${price}")

elif size == "L":
    price = 25
    if add_pepperoni == "Y":
        price += 3
        print(f"Your final bill is ${price}")
    else:
        print(f"Your final bill is ${price}")
    if extra_cheese == "Y":
        price += 4
        print(f"Your final bill is ${price}")
    else:
        print(f"Your final bill is ${price}")

else:
    print("Something Wrong, try again")

