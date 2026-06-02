'''
Grade Calculator - Convert numerical grade (0-100) to letter grade (A-F)
'''

grade = float(input("Enter a numerical grade (0-100): "))

if grade >= 90:
    print("Your letter grade is: A")
elif grade >= 80:
    print("Your letter grade is: B")
elif grade >= 70:   
    print("Your letter grade is: C")
elif grade >= 60:
    print("Your letter grade is: D")
else:
    print("Your letter grade is: F")