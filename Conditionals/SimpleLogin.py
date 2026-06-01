'''
    Simple Login - Check if username and password match predefined values 
'''

# Predefined username and password
Saved_username = "admin"
Saved_password = "password123"

# Get user input
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if credentials match
if username == Saved_username and password == Saved_password:
    print("Login successful!")
else:
    print("Invalid username or password.")