#Simple Inventory System 

# INVENTORY SYSTEM REQUIREMENTS
# 1. Start with an empty inventory
# 2. Show a menu:
#    - Add item
#    - Remove item
#    - View inventory
#    - Quit
# 3. Allow adding an item with a quantity
# 4. Prevent quantities from going below 0
# 5. Prevent removing items that do not exist
# 6. Use functions for actions (add, remove, view)
# 7. Keep the program running until the user chooses to quit

inventory = { }
running = True
print("📮Main Menu\n1. Add item\n2. Remove item\n3. View inventory\n4. Quit")

def main_menu(running):
    choice = input("\nWhat would you like to do?\n>> ")
    if choice == "1":
        print("\n📥 Add an Item")
        add_item()
        view_inventory()
    elif choice == "2":
        print("\n📤 Remove an Item")
        remove_item()
        view_inventory()     
    elif choice == "3":
        print("\n💼 View Inventory")
        view_inventory()
    elif choice == "4":
        print("\n📨 Have a nice dayy")
        running = False
    else:
        print("\n😑 Only enter numbers 1-4")
        main_menu(running)
        
    return running 
    
def add_item():
    item = input("Item: ")
    quantity = int(input("Quantity: "))
    
    if item in inventory:
        inventory[item] = (inventory.get(item) + quantity)
        #add quantity 
        
    else:
        inventory.update({item: quantity})       
        #add item
        
    return inventory
   
    
def remove_item():
    item = input("Item: ")
    quantity = int(input("Quantity: "))
    
    if item in inventory:
        inventory[item] = (inventory.get(item) - quantity)
        #reduce  quantity 
        if inventory.get(item) <= 0:
            inventory.pop(item)            
            #removes item <= 0
        
    else:
        print(f"{item} does not exist")
        remove_item()      
        #prevents removing of item that does           not exist 
        
    return inventory 
    

def view_inventory():
    print("\n📬 Inventory")
    
    for items in inventory:
        print(f"{items}: {inventory[items]}")
        #items =  index/keys
       #inventory[items] gets the                               corresponding value for the items
    
while running:
    running = main_menu(running)

    