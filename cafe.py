#Define the restaurant menu
menu = {
    'Pizza' : 120,
    'Burger' : 100,
    'Fries' : 80,
    'Chicken Wings' : 90,
    'Chicken Nuggets' : 70,
    'Coffee': 80,
    'Salad' : 120,
}

# print(menu)

#Greeting
print("Welcome to BHARATH RESTO!\n")
print("Please select your meal:\n")
print("Pizza\t\t\t:\t\t\t120\nBurger\t\t\t:\t\t\t100\nFries\t\t\t:\t\t\t80\nChicken Wings\t\t:\t\t\t90\nChicken Nuggets\t\t:\t\t\t70\nCoffee\t\t\t:\t\t\t80\nSalad\t\t\t:\t\t\t120")

order_total = 0
#80+70=150 now the total amount of 150 will be stored in the order total
#give conditions
# create a variable item_1
item_1 = input("Enter the name of the item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Y/N):")
if another_order == 'Y':
    item_2 = input("Enter the name of the item you want to order = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available yet!")
print(f"The total amount of items to pay is {order_total}")