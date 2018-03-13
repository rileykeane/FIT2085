"""
@author Riley Keane
@since 8/3/18
@modified 8/3/18
"""


def is_a_leap_year(year):
    """
    This function takes a year as an integer eg. 2008 and returns True for a leap year or False if its not a leap year
    :param year: A year as an integer false
    :return: A Boolean, True for leap year, False for non leap years
    """
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def main():
    """
    This function is the main function of the program, it prompts the user for a year and then checks it using the
    is_a_leap_year function. It will print the result to the user
    :return: NA
    """
    # While the user does not want to exit, keep asking for a year
    user_year = int(input('Enter a year: '))

    # Using the is_a_leap year function to check if its a leap year and printing the corresponding response
    if is_a_leap_year(user_year):
        print('Is a leap year')
    else:
        print('Is not a leap year')


# Calling the main function to run the program
main()
