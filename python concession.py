#----------------PYTHON CONCESSION STAND PROGRAM---------------------

menu = {"pizza" : 3.000,
        "nachos" : 4.50,
        "popcorn" : 6.000,
        "fries" : 2.50,
        "chips" : 3.50,
        "pretze" : 3.50,
        "soda" : 3.00,
        "lemonade" : 4.25}

cart = []
total = 0
print("---------MENU-----------")
for key, value in menu.items():
    print(f"{key:10} :${value:.2f}")
print("---------------------------------")
while True:
    food = input("select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("--------YOUR order---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"the total is: ${total:.2f}")
