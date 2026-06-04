'''
Palindrome Checker - Check if a word is the same forwards and backwards 
'''
def is_palindrome(word):
   
    cleaned_word = word.replace(" ", "").lower()

    return cleaned_word == cleaned_word[::-1]   



word = input("Enter a word to check if it's a palindrome: ")
if is_palindrome(word):
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")   
