from task2 import import_keys

def test_import_keys():
    test1 = import_keys('text_files/test_keys1.txt', 1, 7)
    test2 = import_keys('text_files/test_keys2.txt', 27183, 11)
    assert test1._array == [None, ('dog', 1), None, ('cat', 1), ('fish', 1), None, None]
    assert test2._array == [('b', 1), ('abc', 1), None, None, ('aaa', 1), ('bb', 1), None, None, None, None, ('aa', 1)]


def main():
    print('Testing test_import_keys()')
    test_import_keys()
    print('\nPassed all tests')


main()
