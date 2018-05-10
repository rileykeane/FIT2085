from task2 import List


def read_text_file(name):
    """
    Imports a text file into a list

    param       name: the name of the file you want to import
    return      The list containing each line of the file
    pre         name must be a string
    pre         the file you are importing must exist within the directory of the code
    post        the list with have each line as a new item
    complexity  best = worst: O(n) where n is the number of lines in the text file.
    """

    if type(name) is not str:
        raise ValueError('name must be a string')

    file = open(name, 'r')
    file_list = List()

    for line in file:
        file_list.append(line.rstrip('\n'))

    file.close()

    return file_list


def test_read_text_file():
    # creating tests
    test1 = read_text_file('small.tex')
    test2 = read_text_file('test1.txt')

    # created
    exp_result1 = List()
    exp_result1.unsafe_set_array(['Yossarian decided', 'not to utter', 'another word.'], 3)
    exp_result2 = List()
    exp_result2.unsafe_set_array(['print', 'every', 'line', 'in this', 'file!'], 5)

    assert test1 == exp_result1, 'Failed on test 1, expected {} but got {}.'.format(str(test1), str(exp_result1))
    assert test2 == exp_result2, 'Failed on test 2, expected {} but got {}.'.format(str(test2), str(exp_result2))

    print('read text file passed all tests')


test_read_text_file()