#!/usr/bin/python3

"""
This file implements the unsorted list ADT using Python lists as fake objects and arrays.

@author         Javier Candeira, from lecture code by Maria Garcia de la Banda
@since          11 Aug 2013
@input          none
@output         none
@errorHandling  none
@knownBugs      none

Invariants:
- length is never greater than len(the_array)
- length points to the first empty position (if any)
- all slots in positions 0 to length-1 of the_array contain items.
"""


def List(size):
    """
    Creates an empty object of the class, i.e., an empty array list.

    @param          size number of items in containing array, or maxitems of list
    @return         a list data structure
    @post           an empty list object is created
    @complexity     best and worst case: the complexity of [None]*size, which it is 
                    probably O(size)
    """
    length = 0
    the_array = [None] * size
    return [length, the_array]

def length(the_list):
    """
    Returns the length of the list.

    @param          the_list data structure
    @return         the length of the list
    @complexity     best and worst case: O(1)
    """
    length = the_list[0]
    return length

def is_empty(the_list):
    """
    Determines if the list has any elements.

    @param          the_list data structure
    @return         false if list has elements, true if empty
    @complexity     best and worst case: O(1)
    """
    length = the_list[0]
    return length == 0

def is_full(the_list):
    """
    Determines whether the list is full.
    Since it is implemented with arrays, it can get full.

    @param      the_list data structure
    @return     true is the list is full, false otherwise
    @complexity best and worst case: O(1)
    """
    [length,the_array] = the_list
    return length >= len(the_array)

def reset(the_list):
    """
    Resets the list to an empty state.

    @param          the_list data structure
    @post           the list is empty
    @complexity     best and worst case: O(1)
    """
    the_list[0] = 0

def get_item(the_list, index):
    """
    Returns an item at a given position in the list.

    @param          the_list data structure
    @param          index of element to return
    @pre            index is integer between zero and len(list)-1
    @post           list isn't changed
    @complexity     best and worst case: O(1)
    """
    [length,the_array] = the_list
    try:
        assert int(index) == index
        assert 0 <= index <= length-1
    except (AssertionError, ValueError):
        raise IndexError('index not an integer within range')
    return the_array[index]

def add_last(the_list, new_item):
    """
    Adds the input item at the end of the unsorted list.

    @param          the_list data structure
    @param          new_item to add to this list
    @post           returns True if list has space, False it is has not
    @post           if True, the list has one more element after the method is called and
                    list[last] equals new_item after the method is called
    @post           If False, list is untouched
    @complexity     best and worst case: O(1)
    """
    has_space_left = not is_full(the_list)
    if has_space_left:
        [length,the_array] = the_list
        the_array[length] = new_item
        the_list[0] = length + 1
    return has_space_left


def index(the_list, item):
    """
    Position of the first item equaling input item in this unsorted list
    Since this is an unsorted list, this is a linear search.

    @param      the_list data structure
    @param      item to find
    @return     the item's index if the item appears in the list,
                None otherwise.
    @complexity best case: O(M) (first item), worst case: O(length*M) (not there), where 
                M is the size of the elements
    """
    [length,the_array] = the_list
    for i in range(length):
        if the_array[i] == item:      #found
            return i
    return None

def delete_item(the_list, delitem):
    """
    Deletes the first appearance (if any) of the input item.

    @param      the_list data structure
    @param      delitem, first instance of which to be deleted
    @return     True if item was in list and has been deleted
    @post       if item was in list, list has one fewer elements
    @post       if item was in list one or more times, only first one
                will have been removed
    @post       if item wasn't in list, list is unchanged
    @complexity best and worst case: O(length*M) 
    """
    pos = index(the_list, delitem)
    found = (pos != None)
    if found:   
        [length,the_array] = the_list
        for i in range(pos, length - 1):
            the_array[i] = the_array[i+1]
        the_list[0] = length - 1
    return found  


def set_item(the_list, index, item):
    """
    sets the element in the given index to the given item

    @param          the_list data structure
    @param          index of element to set
    @:param         item to be set
    @pre            index is integer between zero and len(list)-1 and must exist in the list
    @post           index will be set to item
    @complexity     best and worst case: O(1)
    """
    [length, the_array] = the_list
    try:
        assert int(index) == index
        assert 0 <= index <= length - 1
    except (AssertionError, ValueError):
        raise IndexError('index not an integer within range')
    the_array[index] = item


def test_is_empty():
    li = List(3)
    assert is_empty(li)
    add_last(li, 5)
    assert li==[1,[5,None,None]]
    assert not is_empty(li)

def test_is_full():
    li = List(3)
    assert not is_full(li)
    add_last(li, 5)
    add_last(li, 5)
    add_last(li, 5)
    assert li==[3,[5,5,5]]
    assert is_full(li)

def test_add_last():
    li = List(5)
    assert add_last(li, 5)
    assert li==[1,[5,None,None,None,None]]
    assert add_last(li, 3)
    assert li==[2,[5,3,None,None,None]]
    assert add_last(li, 10)
    assert li==[3,[5,3,10,None,None]]
    assert add_last(li, 0)
    assert li==[4,[5,3,10,0,None]]
    assert add_last(li, 9)
    assert li==[5,[5,3,10,0,9]]
    assert not add_last(li, 10)

def test_length():
    li = List(0)
    assert length(li)==0
    li = List(10)
    assert length(li)==0
    add_last(li, 5)
    assert length(li)==1    

def test_get_item():
    li=[5,[5,3,10,0,9,None,None,None,None,None]]
    assert get_item(li, 0) == 5
    assert get_item(li, 1) == 3
    assert get_item(li, 2) == 10
    assert get_item(li, 3) == 0
    assert get_item(li, 4) == 9

def test_index():
    li=[5,[5,3,10,0,9,None,None,None,None,None]]
    assert get_item(li, 0) == 5
    assert get_item(li, 1) == 3
    assert get_item(li, 2) == 10
    assert get_item(li, 3) == 0
    assert get_item(li, 4) == 9

def test_delete_item():
    li=[10,[5,3,10,0,9,1,4,6,7,8]]
    assert delete_item(li, 0)
    assert delete_item(li, 10)
    assert delete_item(li, 9)
    assert delete_item(li, 4)
    assert delete_item(li, 7)
    assert li==[5,[5,3,1,6,8,8,8,8,8,8]]

if __name__ == '__main__':
    """minimal sanity tests"""
    li = List(10)
    test_is_empty()
    test_is_full()
    test_add_last()
    test_length()
    test_get_item()
    test_index()
    test_delete_item()
    reset(li)
    assert length(li) == 0
    assert is_empty(li)

    print("All tests passed")
