#define the menu of resturant
menu={
    "Pizza":40,
    "Pasta":60,
    "coffie":70,
}

 
print("Welcome  to our resturant:")
print("Pizza: price 40\nPasta:price 60\ncoffie:price 70")

total_order=0

item_1=input("Enter the name of item you want to order=")

if item_1 in menu:
    total_order+=menu(item_1)
    print(f"Your item{item_1} has been added to  your order")



else:
    print(f"Ordered item{item_1} is not available yet")

anothe_order=input ("Do you want  to add another item? (yes/No)" )
if anothe_order== "yes":
    item_2=("Enter the name of second item=" )
    if item_2 in menu:
        total_order+=menu(item_2)
        print(f"Item {item_2} has been added to order")

    else:
        print(f"Ordered item{item_2} is not avialable!")


print(f"The total amount of items to pay is {total_order}")