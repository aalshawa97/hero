# Hero's inventory

def display_inventory(inventory):
    print("Your items:")
    for item in inventory:
        print(item)
    print("You have", len(inventory), "items in your inventory")

def print_hi(name):
    print(f'Hi, {name} welcome to Hero!')
    print('Items you need: Sword, Armor, Shield, Medicine')

    inventory = ["sword", "armor", "shield", "medicine"]
    display_inventory(inventory)

    print('You have found a gold treasure chest, adding the items to your inventory')

    inventory.append("axe")
    inventory.append("arrow")
    inventory.append("bow")
    display_inventory(inventory)

    while True:
        user_input = input("Enter an index number (0-6) for an item in the inventory (or press Enter to exit): ")
        if user_input == "":
            break
        try:
            index = int(user_input)
            item = inventory[index]
            print("Item at index", index, "is:", item)
        except (ValueError, IndexError):
            print("Invalid input or index out of range. Please try again.")

    input("\nPress the enter key to continue.")

if __name__ == '__main__':
    print_hi('PyCharm')
