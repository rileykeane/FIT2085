from linked_stack import Stack


def test_len():
    x = Stack()
    assert len(x) == 0, 'Expected 0, got ' + str(len(x))
    x.push(20)
    x.push(25)
    x.push(32)
    assert len(x) == 3, 'Expected 3, got ' + str(len(x))
    x.push(11)
    x.push(12)
    assert len(x) == 5, 'Expected 5, got ' + str(len(x))
    for _ in range(5):
        x.pop()
    assert len(x) == 0, 'Expected 0, got ' + str(len(x))

def test_str():
    x = Stack()
    assert str(x) == "", 'Expected "", got ' + str(x)
    x.push(20)
    x.push(25)
    x.push(32)
    assert str(x) == "32 25 20", 'Expected 32 25 20, got ' + str(x)
    x.push(11)
    x.push(12)
    assert str(x) == "12 11 32 25 20", 'Expected 12 11 32 25 20, got ' + str(x)

def test_eq():
    x = Stack()
    y = 'hello'
    assert x != y, 'Expected False but got, ' + str(x != y)
    y = Stack()
    assert x == y, 'Expected True but got, ' + str(x != y)
    x.push(1)
    x.push(2)
    y.push(2)
    y.push(1)
    y.push(0)
    assert x != y, 'Expected False but got, ' + str(x != y)
    x.pop()
    x.pop()
    x.push(2)
    x.push(1)
    x.push(0)
    assert x == y, 'Expected True but got, ' + str(x != y)

def main():
    print('Testing __len__')
    test_len()
    print('Testing __str__')
    test_str()
    print('Testing __eq__')
    test_eq()

if __name__ == "__main__":
    main()