from task2 import *


def test_is_empty():
    # creating test cases
    test1 = List(5)
    test1.unsafe_set_array(5, [1, 2, 3, 4, 5])
    test2 = List()
    test3 = List(10)
    test4 = List(20)
    test4.unsafe_set_array(3, [6, 9, 12])

    test_cases = [
        (1, test1, False),
        (2, test2, True),
        (3, test3, True),
        (4, test4, False)
    ]

    for test_id, test, exp_result in test_cases:
        actual_result = test.is_empty()
        assert actual_result == exp_result, 'Fail on {}, expected {}, got {}'.format(test_id, exp_result, actual_result)

    print('is_empty passed all tests')


def test_is_full():
    test1 = List(5)
    test1.unsafe_set_array([1,2,3,4,5], 5)
    test2 = List()
    test3 = List(10)
    test4 = List(5)
    test4.unsafe_set_array([1,2,3,4], 5)

    test_cases = [
        (1, test1, True),
        (2, test2, False),
        (3, test3, False),
        (4, test4, False)
    ]

    for test_id, test, exp_result in test_cases:
        actual_result = test.is_full()
        assert actual_result == exp_result, 'Fail on {}, expected {}, got {}'.format(test_id, exp_result, actual_result)

    print('is_full passed all tests')


def test_str():
    x = List()
    assert str(x) == "", "Should be empty string but it is" + str(x)
    x.append(2)
    assert str(x) == "2\n", "Should be a 2 string but it is" + str(x)
    x.unsafe_set_array([1, 2, 3, None, None], 3)
    assert str(x) == "1\n2\n3\n", "Should be a 1 2 3 string but it is" + str(x)
    print('str passed all tests')


def test_len():
    test1 = List(5)
    test1.unsafe_set_array([1, 2, 3], 3)
    test2 = List()
    test3 = List(5)
    test3.unsafe_set_array([1, 2, 3, 4, 5], 5)
    test4 = List(10)
    test4.unsafe_set_array([1], 1)

    tests = [
        (1, test1, 3),
        (2, test2, 0),
        (3, test3, 5),
        (4, test4, 1)
    ]

    for test_id, test, exp_result in tests:
        actual_result = len(test)
        assert actual_result == exp_result, 'Fail on {}, expected {}, got {}'.format(test_id, exp_result, actual_result)

    print('len passed all tests')


def test_get_item():
    test_list = List(10)
    test_list.unsafe_set_array([0, 1, 2, 3, 4, 5], 6)

    tests = [
        (0, 0),
        (3, 3),
        (5, 5),
        (2, 2),
        (-1, 5),
        (-6, 0)
    ]

    for test, exp_result in tests:
        actual_result = test_list[test]
        assert exp_result == actual_result, 'Fail on list[{}] - expected {}, got {}'.format(test, exp_result, actual_result)

    try:
        test_list[6]
        assert True is False, ('Should have raised an indexError')
    except IndexError:
        True

    try:
        test_list[-7]
        assert True is False, ('Should have raised an indexError')
    except IndexError:
        True

    print('get_item passed all tests')


def test_set_item():
    test_list = List(10)
    exp_result = List(10)
    test_list.unsafe_set_array([1, 2, 3, 4, 5, 6, 7, None, None, None], 7)
    test_list[3] = 8
    exp_result.unsafe_set_array([1, 2, 3, 8, 5, 6, 7, None, None, None], 7)
    assert test_list == exp_result, "Failed on test 1 - expected " + str(exp_result) + ", got " + str(test_list)
    test_list[0] = 2
    test_list[6] = 14
    exp_result.unsafe_set_array([2, 2, 3, 8, 5, 6, 14, None, None, None], 7)
    assert test_list == exp_result, "Failed on test 1 - expected " + str(exp_result) + ", got " + str(test_list)
    test_list[-1] = 5
    test_list[-7] = 8
    exp_result.unsafe_set_array([8, 2, 3, 8, 5, 6, 5, None, None, None], 7)

    try:
        test_list[7] = 7
        assert True is False, ('Should have raised an indexError')
    except IndexError:
        True

    try:
        test_list[-8] = 7
        assert True is False, ('Should have raised an indexError')
    except IndexError:
        True

    print('set_item passed all tests')


def test_append():
    x = List(3)
    x.append(1)
    y = List()
    y.unsafe_set_array([1, None, None], 1)
    assert (str(x) == str(y)), "Should be True but it is" + "x="+ str(x) + "y=" + str(y)
    x.append(2)
    y.unsafe_set_array([1, 2, None], 2)
    assert (str(x) == str(y)), "Should be True but it is" + "x="+ str(x) + "y=" + str(y)
    x.append(3)
    y.unsafe_set_array([1, 2, 3], 3)
    assert (str(x) == str(y)), "Should be True but it is" + "x=" + str(x) + "y=" + str(y)
    try:
        x.append(4)
        print("Should have raised Exception")
    except Exception:
        True
    print('test_append passed all tests')


def test_eq():
    x = List()
    x.unsafe_set_array([4, 3, 5, None, None], 3)
    y = List()
    y.unsafe_set_array([4, 3, 5, None, None, None], 3)
    z = List()
    z.unsafe_set_array([4, 5, 3, None, None], 3)
    w = List()
    w.unsafe_set_array([4, 5, None, None], 2)
    v = List()
    v.unsafe_set_array([4, 3, 5, 7, None, None], 4)
    assert (x == y), "Should be True but it is" + "x="+ str(x) + "y=" + str(y)
    assert (x != z), "Should be False but it is" + "x="+ str(x) + "z=" + str(z)
    assert (x != w), "Should be False but it is" + "x="+ str(x) + "w=" + str(w)
    assert (x != v), "Should be False but it is" + "x=" + str(x) + "v=" + str(v)
    try:
        x[7] = 0
        print("Should have raised IndexError")
    except IndexError:
        True

    print('eq passed all tests')


def test_insert():
    x = List()
    x.unsafe_set_array([1, 2, 5, 6, 7, None, None], 5)
    y = List()
    y.unsafe_set_array([1, 2, 3, 5, 6, 7, None], 6)
    x.insert(2, 3)
    assert (x == y), "Should be True but it is" + "x=" + str(x) + "y=" + str(y)
    x.insert(0, 0)
    y.unsafe_set_array([0, 1, 2, 3, 5, 6, 7], 7)
    assert (x == y), "Should be True but it is" + "x=" + str(x) + "y=" + str(y)
    x.insert(-1, 4)
    y.unsafe_set_array([0, 1, 2, 3, 5, 6, 4, 7], 8)
    assert (x == y), "Should be True but it is" + "x=" + str(x) + "y=" + str(y)
    x.insert(-8, 5)
    y.unsafe_set_array([5, 0, 1, 2, 3, 5, 6, 4, 7], 9)

    try:
        x.insert(9,2)
        assert True is False, "Should have raised IndexError"
    except IndexError:
        True

    try:
        x.insert(-10, 2)
        assert True is False, "Should have raised IndexError"
    except IndexError:
        True

    print('insert passed all tests')


def test_contains():
    x = List()
    assert (2 in x) is False, "Should be False as x is empty but it is" + str(x)
    x.append(2)
    assert (2 in x), "Should be True as x=[2] but it is" + str(x)
    x.unsafe_set_array([4, 2, 3, None, None], 3)
    assert (3 in x), "Should be True as x=[4,2,3] but it is" + str(x)

    print('contains passed all tests')


def test_remove():
    x = List()
    x.unsafe_set_array([0, 1, 2, 2, 2, 7, 0, None, None], 7)
    x.remove(2)
    y = List()
    y.unsafe_set_array([0, 1, 7, 0, None, None], 4)
    assert (x == y), "Should be True but it is" + "x=" + str(x) + "y=" + str(y)
    x.remove(0)
    y.unsafe_set_array([1, 7, None, None], 2)
    assert (x == y), "Should be True but it is" + "x=" + str(x) + "y=" + str(y)
    try:
        x.remove(12)
        print("Should have raised ValueError")
    except ValueError:
        True

    print('remove passed all tests')


def test_delete():
    x = List()
    x.unsafe_set_array([1, 2, 5, 6, 7, None, None], 5)
    y = List()
    y.unsafe_set_array([1, 2, 6, 7, None, None], 4)
    item = x.delete(2)
    assert (item == 5 and x == y), "Should be True but it is" + "item=" +str(item)+"x=" + str(x) + "y=" + str(y)
    item = x.delete(0)
    y.unsafe_set_array([2, 6, 7, None, None], 3)
    assert (item == 1 and x == y), "Should be True but it is" + "item=" + str(item) + "x=" + str(x) + "y=" + str(y)
    item = x.delete(-1)
    y.unsafe_set_array([2, 6], 2)
    assert (item == 7 and x == y)
    item = x.delete(-2)
    y.unsafe_set_array([6], 1)
    assert (item == 2 and x == y)
    try:
        x.delete(1)
        assert True is False, "Should have raised IndexError"
    except IndexError:
        True

    print('delete passed all tests')


def test_resize():
    test_list = List(100)
    # adding 10 ints to test
    for i in range(10):
        test_list.append(i)
    assert len(test_list._the_array) == 100, 'Fail on test 1'

    for i in range(100):
        test_list.append(i)
    assert len(test_list._the_array) == 170, 'Fail on test 2'

    for i in range(1000):
        test_list.append(i)
    array_len = len(test_list._the_array)
    assert array_len == 1423, 'Fail on test 3, expected 1423, got {}'.format(array_len)

    for i in range(754):
        test_list.delete(1)
    array_len = len(test_list._the_array)
    assert array_len == 1423, 'Fail on test 3, expected 1423, got {}'.format(array_len)

    for i in range(55):
        test_list.delete(1)
    array_len = len(test_list._the_array)
    assert array_len == 712, 'Fail on test 3, expected 712, got {}'.format(array_len)

    for i in range(200):
        test_list.delete(1)
    array_len = len(test_list._the_array)
    assert array_len == 356, 'Fail on test 3, expected 712, got {}'.format(array_len)

    for i in range(100):
        test_list.delete(1)
    array_len = len(test_list._the_array)
    assert array_len == 100, 'Fail on test 3, expected 100, got {}'.format(array_len)

    print("resize passed all tests")

def main():
    test_is_empty()
    test_is_full()
    test_str()
    test_len()
    test_get_item()
    test_set_item()
    test_append()
    test_eq()
    test_insert()
    test_contains()
    test_remove()
    test_delete()
    test_resize()

main()


