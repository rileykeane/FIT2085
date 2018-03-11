"""
@author Riley Keane
@since 8/3/18
@modified 11/3/18
"""

user_year = int(input("Enter a year: "))

# Checking if the year is divisible by 4
if user_year % 4 == 0:
    # checking if year is divisible by 100
    if user_year % 100 == 0:
        # if the year is divisible by 400, its a leap year
        if user_year % 400 == 0:
            print('Is a leap year')
        else:
            print('Is not a leap year')
    # if its not divisible by 100, its a leap year
    else:
        print('Is a leap year')
# if its not divisible by 4, its not a leap year
else:
    print('Is not a leap year')




