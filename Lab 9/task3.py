def describe(sub_strings):
    operators = ['+', '-', '*', '/']
    sub_string_types = []

    for string in sub_strings:
        try:
            float(string)
            string_type = (float(string), 'Float')
        except Exception:
            string_type = None

        if string_type is not None:
            if int(string_type[0]) == string_type[0]:
                string_type = (int(string_type[0]), 'Int')
        else:
            for op in operators:
                if string == op:
                    string_type = (string, 'Operator')

        if string_type is None:
            string_type = (string, 'Invalid String')

        sub_string_types.append(string_type)

    return sub_string_types


"""
user_input = input('Enter a string: ')
user_input = user_input.strip()
user_input = user_input.split(' ')
types = describe(user_input)

for item in types:
    print(str(item[0]) + "  " + str(item[1]) + '\n')
"""