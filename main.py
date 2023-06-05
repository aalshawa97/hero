# Hero's inventory

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#Create an empty tuple
inventory = ()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} welcome to Hero!')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f'Items you need: Sword, Armor, Shield, Medicine')
    if not inventory:
        print("You are empty-handed.")
    input("\nPress the enter key to continue.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
