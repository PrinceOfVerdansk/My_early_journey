'''
Number Stats - Find the largest and smallest number in a list
'''
numbers = [3, 7, 1, 9, 4]

for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
        
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)  
