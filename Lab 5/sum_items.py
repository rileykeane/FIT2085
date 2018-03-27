"""
@author Riley Keane
@since 23/3/18
@modified 23/3/18
"""


def sum_items(a_list):
    list_len = len(a_list)

    if list_len <= 0:
        return 0

    list_sum = 0
    for num in a_list:
        list_sum = list_sum + num

    return list_sum


def test_sum_items():
    tests = [
        ([1, 2, 3, 4, 5], 15),
        ([7, 4, 12, 9, 13], 45),
        ([10], 10),
        ([], 0)
    ]

    for test, exp_result in tests:
        func_result = sum_items(test)
        assert func_result == exp_result, 'Failed on {} - got {}, expected {}'.format(test, func_result, exp_result)

    print('All tests passed')


test_sum_items()

