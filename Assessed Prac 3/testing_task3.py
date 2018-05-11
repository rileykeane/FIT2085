from task1 import HashTable

def test_counters():
    # testing the counters added to task1 
    test1_table = HashTable(17)
    test1_table['riley'] = 19
    test1_table['sally'] = 28
    test1_table['rileyy'] = 18
    test1_table['bill'] = 65
    test1_table['daniel'] = 19
    test1_table['steve'] = 25
    test1_table['alan'] = 55
    test1_table['scott'] = 33
    assert test1_table.collision_info() == (3, 6, 4, 0), str(test1_table.collision_info())


def main():
    print('Testing collision_info()')
    test_counters()
    print("\nPassed all tests")


if __name__ == "__main__":
    main()