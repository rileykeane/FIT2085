from task1 import HashTable

def test_setitem():
    test_table = HashTable(7)
    assert test_table._array == [None] * 7, 'Failed on test 1'
    test_table['riley'] = 19
    assert test_table._array == [None, None, None, None, ('riley', 19), None, None], 'Failed on test 2'
    test_table['sally'] = 28
    test_table['rileyy'] = 18
    assert test_table._array == [('rileyy', 18), None, ('sally', 28), None, ('riley', 19), None, None], 'Failed on test 3'
    test_table['bill'] = 65
    test_table['daniel'] = 19
    test_table['steve'] = 25
    test_table['alan'] = 55
    test_table['rileyy'] = 35
    test_table['bill'] = 100
    assert test_table._array == [('rileyy', 35), ('steve', 25), ('sally', 28), ('alan', 55), 
        ('riley', 19), ('bill', 100), ('daniel', 19)], 'Failed on test 4' 
    test_table['scott'] = 45
    assert test_table._array ==  [None, None, ('steve', 25), None, ('sally', 28), ('alan', 55), 
        ('bill', 100), ('riley', 19), ('scott', 45), None, None, None, None, None, ('rileyy', 35), None, ('daniel', 19)] 


def test_getitem():
    test_table = HashTable()
    test_table['riley'] = 'Keane'
    test_table['daniel'] = 'Feltham'
    test_table['bill'] = 'Gates'
    test_table['steve'] = 'Jobs'
    test_table['daniel'] = 'Smith'
    assert test_table['riley'] == 'Keane'
    assert test_table['daniel'] == 'Smith'
    assert test_table['steve'] == 'Jobs'
    try:
        test_table['mark']
        print('Should have raised KeyError - __getitem__() Failed')
    except:
        pass


def test_contains():
    test_table = HashTable(7)
    test_table['riley'] = 'Keane'
    assert 'riley' in test_table
    assert not 'alan' in test_table
    test_table['daniel'] = 'Feltham'
    test_table['bill'] = 'Gates'
    test_table['steve'] = 'Jobs'
    test_table['daniel'] = 'Smith'
    test_table['jeff'] = 'Bezos'
    test_table['elon'] = 'Musk'
    assert 'jeff' in test_table
    assert not 'tim' in test_table


def test_rehash():
    test_table = HashTable(7)
    test_table['riley'] = 19
    test_table['sally'] = 28
    test_table['rileyy'] = 18
    test_table['bill'] = 65
    test_table['daniel'] = 19
    test_table['steve'] = 25
    test_table['alan'] = 55
    test_table.rehash()
    assert test_table._count == 7
    assert test_table._table_size == 17
    assert test_table._array == [None, None, ('steve', 25), None, ('sally', 28), ('alan', 55), 
        ('bill', 65), ('riley', 19), None, None, None, None, None, None, ('rileyy', 18), None, ('daniel', 19)]
    test_table = HashTable(4166287)
    try:
        test_table.rehash()
        print('Should have raised ValueError - rehash() Failed')
    except:
        pass


def main():
    print('Testing __setitem__()')
    test_setitem()
    print('Testing __getitem__()')
    test_getitem()
    print('Testing __contains__()')
    test_contains()
    print('Tetsing rehash()')
    test_rehash()
    print('\nAll tests passed\n')


main()