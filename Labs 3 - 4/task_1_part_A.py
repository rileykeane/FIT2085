"""
@author Riley Keane
@since 8/3/18
@modified 8/3/18
"""


def is_a_leap_year(year):
    if (year % 4 == 0) and (year % 4 != 0) or (year % 400 == 0):
        return True
    else:
        return False


user_year = int(input('Enter a year: '))

if is_a_leap_year(user_year):
    print('Is a leap year')
else:
    print('Is not a leap year')

'''
testing 1234


'''