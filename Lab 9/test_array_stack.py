from array_stack import *

def test_is_empty():
    x = Stack()
    assert x.is_empty(), "Should be empty stack but it is" + str(x)
    x.push(3)
    assert not x.is_empty(), "Should not be empty stack but it is" + str(x)
    x.unsafe_set_array([3, 4], 2)
    assert not x.is_empty(), "Should not be empty stack but it is" + str(x)

def test_push():
    x = Stack(3)
    x.push(1)
    y = Stack()
    y.unsafe_set_array([1, None, None], 1)
    assert x==y, "Should be True but it is" + "x="+ str(x) + "y=" + str(y)
    x.push(2)
    y.unsafe_set_array([1, 2, None, None], 2)
    assert x == y, "Should be True but it is" + "x="+ str(x) + "y=" + str(y)
    x.push(3)
    y.unsafe_set_array([1, 2, 3, None, None], 3)
    assert (x == y), "Should be True but it is" + "x=" + str(x) + "y=" + str(y)

def test_pop():
    x = Stack()
    x.unsafe_set_array([6, 7, None, None], 2)
    y = Stack()
    y.unsafe_set_array([6, None, None], 1)
    item = x.pop()
    assert (item == 7 and x == y), "Should be True but it is" + "item=" +str(item)+"x=" + str(x) + "y=" + str(y)
    item = x.pop()
    y.unsafe_set_array([None, None], 0)
    assert (item == 6 and x == y), "Should be True but it is" + "item=" + str(item) + "x=" + str(x) + "y=" + str(y)

def test_peek():
    x = Stack()
    x.unsafe_set_array([6, 7, None, None], 2)
    y = Stack()
    y.unsafe_set_array([6, 7, None, None], 2)
    item = x.peek()
    assert (item == 7 and x == y), "Should be True but it is" + "item=" +str(item)+"x=" + str(x) + "y=" + str(y)

def test_len():
    x = Stack()
    assert len(x) == 0, "Length should be 0 but is " + str(len(x))
    x.unsafe_set_array([None,None],0)
    assert len(x) == 0, "Length should be 0 but is " + str(len(x))
    x.push(1)
    assert len(x) == 1, "Length should be 0 but is " + str(len(x))
    x.unsafe_set_array([1,2,3,None,None],3)
    assert len(x) == 3, "Length should be 0 but is " + str(len(x))

def test_str():
    x = Stack()
    assert str(x) == "", "Should be empty string but it is" + str(x)
    x.push(2)
    assert str(x) == "2", "Should be a 2 string but it is" + str(x)
    x.unsafe_set_array([1, 2, 3, None, None], 3)
    assert str(x) == "1 2 3", "Should be a 1 2 3 string but it is" + str(x)

def test_resize():
    x = Stack(100)
    for i in range(100):
        x.push(i)
    assert len(x._array) == 100, "Should be 100 but is " + str(len(x._array))
    x.push(100)
    assert len(x._array) == 170, "Should be 170 but is " + str(len(x._array))
    for i in range(101, 1001):
        x.push(i)
    assert len(x._array) == 1423, "Should be 1423 but is " + str(len(x._array))
    for i in range(645):
        x.pop()
    assert len(x._array) == 1423, "Should be 1423 but is " + str(len(x._array))
    x.pop()
    assert len(x._array) == 712, "Should be 712 but is " + str(len(x._array))
    for i in range(353):
        x.pop()
    assert len(x._array) == 100, "Should be 100 but is " + str(len(x._array))

def main():
    # Run the tests when the module is called from the command line
    print("Testing is_empty")
    test_is_empty()
    print("Testing push")
    test_push()
    print("Testing pop")
    test_pop()
    print("Testing peek")
    test_peek()
    print("Testing __len__")
    test_len()
    print("Testing __str__")
    test_str()
    print("Testing resize")
    test_resize()


if __name__ == "__main__":
    main()
