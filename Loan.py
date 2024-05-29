"""A program to calculate the qualification to receive a loan
#loan if they are 21 years or over
#and have an anual income of atleast 21,000.
#iNPUT THE AGE AND INCOME IN THE USER FRIENDLY PRO,PT"""
age = int(input("Enter your age: "))
income = int(input("Enter your income: "))
if age >= 21 and income >= 21000:
    print("Congratulations you qualify for a loan.")
else:
    print("Unfortunately, we are unable to offer you a loan at this time!.")
