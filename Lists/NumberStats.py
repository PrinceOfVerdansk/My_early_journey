'''
Number Stats - Find the largest and smallest number in a list
'''
numbers = [3, 7, 1, 9, 4]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print(f'The largest number is: {largest}')
print(f'The smallest number is: {smallest}')
