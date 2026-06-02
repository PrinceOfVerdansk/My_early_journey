'''
Password Checker - Create a function that checks if password meets requirements (length, has numbers, etc.) 
'''

def password_checker(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one number."
    if not any(char.isalpha() for char in password):
        return "Password must contain at least one letter."
    return "Password is valid." 

user_password = input("Enter a password to check: ")
result = password_checker(user_password)
print(result)   
