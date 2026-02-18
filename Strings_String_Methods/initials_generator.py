'''
Initials Generator - Take first and last name, return initials (e.g., "John Doe" → "J.D.")
'''

name = input("Enter your name: ").capitalize()

surname = input("Enter your surname: ").capitalize()

print(f' {name} {surname} -> {name[0]},{surname[0]} ')