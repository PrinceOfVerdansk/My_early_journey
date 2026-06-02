'''
 Shopping List - Create a program that lets users add items to a shopping list
'''

shopping_list = []
while True:
    item = input("Enter an item to add to your shopping list (or type 'done' to finish): ")
    if item.lower() == 'done':
        break
    shopping_list.append(item)  
print("Your shopping list:")
for item in shopping_list:
    print("- " + item)
    