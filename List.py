#Fatima Rehan
#November 15th, 2022
#ICS3U-3 
#This program will create a shopping list

shoppinglist = []
needitems = True
remover = "n"
 
while needitems == True:
    addition = input("Enter item ")                             #add item in list 
    shoppinglist.append(addition)
    print("the items in your shopping list are")                #display items in list
    for item in shoppinglist:
        print("- " + item)                                      #print item in list with dash
        
    remover = input("Do you want to remove an item? y/n ")
    if remover.upper() == "Y":                                  #allow item to be removed from list, if not needed
        item_r = input("Which item do you want to remove? ")
        shoppinglist.remove(item_r)

    answer = input("Do you want to add another item? y/n ")     #allow more items to be added to list
    if answer.upper() == "N":
        needitems = False                                       #if, "n", the list is complete
        
print("Your completed shopping list is:")                       #display completed shopping list after every item 
for item in shoppinglist:
    print("- " +item)