# Hero's inventory

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#Create an empty tuple
inventory = ()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} welcome to Hero!')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f'Items you need: Sword, Armor, Shield, Medicine')
    #Populate tuple
    inventory = ("sword", "armor", "shield", "medicine")
    print("Your items:\t")
    for item in inventory:
        print(item)
    input("Press Enter key to continue")
    #Get the length of items in the inventory
    print("You have", len(inventory), "in your inventory")
    if "medicine" in inventory:
        print("\nYou have medicine!")
    if "shield" in inventory:
        print("\nYou have a shield!")
    if "armor" in inventory:
        print("\nYou have armor!")
    if "sword" in inventory:
        print("\nYou have a sword!")
    if not inventory:
        print("You are empty-handed.")
    #Display item
    #try:
    #    index = int(input("\nEnter an index number for an item in the inventory:\t"))
    #except ValueError:
    #    print("In index, ", index, "is:\t", inventory[index - 1])

    input("\nPress the enter key to continue.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
