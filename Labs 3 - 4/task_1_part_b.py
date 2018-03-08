"""
@author Riley Keane
@since 8/3/18
@modified 8/3/18
"""

user_year = int(input("Enter a year: "))

# Checking if the year is divisible by for and not by 100
if user_year % 4 == 0:
    if user_year % 100 != 0:
        print('Is a leap year')
# Checking if the year is divisible by 400
elif user_year % 400 == 0:
        print('Is a leap year')
# if all tests fail, its not a leap year
else:
    print('Is not a leap year')

