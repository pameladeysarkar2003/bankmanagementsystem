#Define the menu of restaurent
menu={
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
}

#Greet
print("Welcome to python restaurent")
print("Pizaa:Rs4\nPasta:Rs 50\nBurger:Rs 60\nSalad:Rs 70\nCoffee:Rs80")

order_total=0

item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total+=menu(item_1)
    print("Your item(item_1) has been added to your order")

else:
    print(f"Ordered item(item_1) is not available yet!")

    another_order=input("Do you want to add another item?(Yes/No)")
    if another_order=="Yes":
        item_2=input("Enter the name of second item=")
        if item_2 in menu:
            order_total+=menu(item_2)
            print("Item(item_2) has been added to order")

        else:
            print(f"Ordered item (item_2) is not available!")

            print(f"The to ntal amount of items to pay is {order_total}")