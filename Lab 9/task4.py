from task3 import describe
from linked_stack import Stack


user_input = input('Enter a string: ')
user_input = user_input.strip()
user_input = user_input.split(' ')
types = describe(user_input)


the_stack = Stack()
for item in types:

    if item[1] == 'Int' or item[1] == 'Float':
        the_stack.push(item[0])

    if item[1] == 'Operator':
        num2 = the_stack.pop()
        num1 = the_stack.pop()
        result = None
        if item[0] == '+':
            result = num1 + num2
        elif item[0] == '-':
            result = num1 - num2
        elif item[0] == '*':
            result = num1 * num2
        elif item[0] == '/':
            result = num1 / num2
        the_stack.push(result)

print(the_stack.pop())
