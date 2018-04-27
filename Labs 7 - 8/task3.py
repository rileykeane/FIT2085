from task2 import List


def read_text_file(name):
    file = open(name, 'r')
    file_list = List()

    for line in file:
        file_list.append(line.rstrip('\n'))

    file.close()

    return file_list


def test_read_text_file():
    # creating tests
    test1 = read_text_file('small.tex')
    test2 = read_text_file('small.txt')

    # created
    exp_result1 = List()
    exp_result1.unsafe_set_array(['Yossarian decided', 'not to utter', 'another word.'], 3)
    exp_result2 = List()
    exp_result2.unsafe_set_array(['print', 'every', 'line', 'in this', 'file!'], 5)

    assert test1 == exp_result1, 'Failed on test 1, expected {} but got {}.'.format(str(test1), str(exp_result1))
    assert test2 == exp_result2, 'Failed on test 2, expected {} but got {}.'.format(str(test2), str(exp_result2))

    print('read text file passed all tests')

test_read_text_file()