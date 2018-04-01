#You are creating a fantasy video game. The data structure to model the player’s inventory
#will be a dictionary where the keys are string values describing the item in the inventory
#and the value is an integer value detailing how many of that item the player has. 

#Write a function named displayInventory() that would take any possible “inventory”
#and display it like the following:





stuff = {'rope': 1,
              'torch': 6,
              'gold coin': 42,
              'dagger': 1,
              'arrow': 12}

def displayInventory(inventory):
     print('inventory:')
     total_items = 0
     for k,v in inventory.items():
             total_items = total_items + v
             print(str(stuff.get(k,0)) + ' ' + k)
             print('total number of items :  ' + str(total_items))

displayInventory(stuff)
