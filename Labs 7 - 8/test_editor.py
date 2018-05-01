from Editor import Editor
from task2 import List


def test_read_filename():
    test_file1 = Editor()
    test_file1.read_filename('small.tex')
    result1 = List()
    result1.unsafe_set_array(['Yossarian decided', 'not to utter', 'another word.'], 3)
    assert test_file1._text_lines == result1, 'Test failed on test1'

    test_file2 = Editor()
    test_file2.read_filename('test1.txt')
    result2 = List()
    result2.unsafe_set_array(['print', 'every', 'line', 'in this', 'file!'], 5)
    assert test_file2._text_lines == result2

    try:
        test_file3 = Editor()
        test_file3.read_filename('test2.txt.txt')
        assert True is False, 'Should have raised an exception.'
    except Exception:
        True

    print('read_filename passed all tests\n')


def test_print_num():
    test_file1 = Editor()
    test_file1.read_filename('test1.txt')
    assert test_file1.print_num(1) == 'print'
    assert test_file1.print_num(3) == 'line'
    assert test_file1.print_num(5) == 'file!'
    assert test_file1.print_num() == 'print\nevery\nline\nin this\nfile!\n'

    try:
        test_file1.print_num(0)
        assert 'Should have raised an index error'
    except IndexError:
        True

    try:
        test_file1.print_num(6)
        assert True is False, 'Should have raised an index error'
    except IndexError:
        True

    try:
        test_file1.print_num('three')
        assert True is False, 'Should have raised a value error'
    except ValueError:
        True

    print('print_num passed all tests\n')


def test_delete_num():
    test_file1 = Editor()
    test_file1.read_filename('test1.txt')
    result1 = List()
    test_file1.delete_num(3)
    result1.unsafe_set_array(['print', 'every', 'in this', 'file!'], 4)
    assert test_file1._text_lines == result1, 'Failed on test 1'
    test_file1.delete_num(1)
    result1.unsafe_set_array(['every', 'in this', 'file!'], 3)
    assert test_file1._text_lines == result1, 'Failed on test 2'
    test_file1.delete_num()
    result1.unsafe_set_array([], 0)
    assert test_file1._text_lines == result1, 'Failed on test 3'

    try:
        test_file1.delete_num(0)
        assert 'Should have raised an index error'
    except IndexError:
        True

    try:
        test_file1.delete_num(6)
        assert True is False, 'Should have raised an index error'
    except IndexError:
        True

    try:
        test_file1.delete_num('three')
        assert True is False, 'Should have raised a value error'
    except ValueError:
        True

    print('delete_num passed all tests\n')


def test_inset_num():
    test_file1 = Editor()
    test_file1.read_filename('test1.txt')
    result1 = List()
    test_file1.insert_num('please', 1)
    result1.unsafe_set_array(['please', 'print', 'every', 'line', 'in this', 'file!'], 6)
    assert test_file1._text_lines == result1, 'Failed on test 1'
    test_file1.insert_num('you can', 5)
    result1.unsafe_set_array(['please', 'print', 'every', 'line', 'you can', 'in this', 'file!'], 7)
    assert test_file1._text_lines == result1, 'Failed on test 2'
    test_file1.insert_num('provided', 7)
    result1.unsafe_set_array(['please', 'print', 'every', 'line', 'you can', 'in this', 'provided', 'file!'], 8)
    assert test_file1._text_lines == result1, 'Failed on test 3'
    test_file1.insert_num('Now!', 9)
    result1.unsafe_set_array(['please', 'print', 'every', 'line', 'you can', 'in this', 'provided', 'file!', 'Now!'], 9)

    print('insert_num passed all tests\n')


def test_search_string():
    test_file1 = Editor()
    test_file1.read_filename('test1.txt')
    assert test_file1.search_string('every') == "2\n"
    assert test_file1.search_string('file!') == "5\n"

    test_file2 = Editor()
    test_file2.read_filename('test2.txt')
    assert test_file2.search_string('dog') == "1\n4\n6\n"
    assert test_file2.search_string('cat') == "2\n7\n"
    assert test_file2.search_string('house') == ""

    print('search_string passed all tests')

def main():
    print('Testing read_filename')
    test_read_filename()
    print('Testing print_num')
    test_print_num()
    print('Testing delete_num')
    test_delete_num()
    print('Testing insert_num')
    test_inset_num()
    print('Testing search string')
    test_search_string()


if __name__ == '__main__':
    main()
