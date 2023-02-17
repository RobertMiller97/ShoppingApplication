# Shopping Application

print("Welcome to Food Mart ")

item = input("What item would you like to buy: ")
price = float(input("What is the price of the item: "))
quantity = int(input("How many would you like: "))
pay = float(input("How much are you paying: "))


total = price * quantity
changeleft = pay - total


print(f"You have purchase {quantity}x {item}'s")
print(f"Your total is: ${total}")
print("")

print(f"Your Change is ${changeleft} ")



