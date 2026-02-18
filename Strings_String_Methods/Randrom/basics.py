'''

1. Age calculator: Ask the user for their age and print out the age in 5 years.
    - Use input() to get the age and convert it to an integer.
2. Temperature converter: Ask the user foru a temperature in Celsius and convert it to Fahrenheit.
    - Use input() to get the temperature and convert it to a float.
3. Greeting: Ask the user for their name and print out a personalized greeting.
    - Use input() to get the name and concatenate it with a string.
4. Number doubler: Ask the user for a number and print out the number doubled.
    - Use input() to get the number and convert it to an integer or float.
5. String repeater: Ask the user for a string and a number, then repeat the string that many times.
    - Use input() to get the string and number, and convert the number to an integer.

''' 



age = int(input("Enter your age: "))

f_age = age + 5 

c = int(input("Enter temperture in Celsius: "))

fahrenheit = (c * 9/5) + 32 

name = input("Enter your name: ").capitalize()

number = int(input("Enter a number and watch it double!: "))

double = number * 2 

string = input("Enter a word: ")

num = int(input("ENter a number"))

repeat = string * num 

print(f' You will be a {age} years old in 5 years and youll feel like its {fahrenheit} in your head, oh yes! You {name}!. It takes you {double} seconds to blink because you keep saying {repeat} over and over again!')

