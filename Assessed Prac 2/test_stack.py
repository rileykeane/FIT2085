from stack import Stack


def test_push():
    test1 = Stack()
    test1.push(1)
    test1.push(4)
    test1.push(5)
    result1 = Stack()
    result1.unsafe_set_stack([1,4,5], 3)
    assert result1 == test1

    print('push passed all tests\n')


def test_pop():
    test1 = Stack()
    test1.unsafe_set_stack([1,2,3,4,5,6], 6)
    assert test1.pop() == 6
    assert test1.pop() == 5
    assert test1.pop() == 4
    result1 = Stack()
    result1.unsafe_set_stack([1,2,3], 3)
    assert test1 == result1

    print('pop passed all tests\n')


def test_resize():
    test1 = Stack()
    assert len(test1._array) == 40

    # testing array will resize by 1.7 when full
    for i in range(40):
        test1.push(i)
    assert len(test1._array) == 40
    test1.push(41)
    assert len(test1._array) == 68
    for i in range(42, 1000):
        test1.push(i)
    assert len(test1._array) == 1658

    # checking array will shrink by half when less 1/4 full
    for i in range(584):
        test1.pop()
    assert len(test1._array) == 1658
    test1.pop()
    assert len(test1._array) == 829

    print('resize passed all tests')


def main():
    print('Testing push')
    test_push()
    print('Testing pop')
    test_pop()
    print('Testing resize')
    test_resize()


if __name__ == '__main__':
    main()
