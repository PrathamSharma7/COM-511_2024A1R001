'''
Write a menu driven python program where a user can add items, remove items,
view cart and exit
'''

items = []
while True:
    print("\nMenu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter the item to add: ")
        items.append(item)
        print(f"{item} added to cart.")
    
    elif choice == '2':
        item = input("Enter the item to remove: ")
        if item in items:
            items.remove(item)
            print(f"{item} removed from cart.")
        else:
            print(f"{item} not found in cart.")
        
    elif choice == '3':
        if items:
            print("Items in cart:")
            for i in range(len(items)):
                print(f"{i + 1}. {items[i]}")
        else:
            print("Cart is empty.")
    elif choice == '4':
        print("Exiting")
        break
    else:
        print("Invalid!!!")