from Editor import Editor
my_file = Editor()


def read_file_name(command):
    """
    checks input is valid and runs read_filename

    param:      command: an array [read, file name]
    pre         file name must be a string
    post        if an exception is thrown, read_filename is not completed
    post        if no errors read_filename is executed
    complexity  best = worst: O(n) where n is the number of lines in the text file.
    """
    try:
        my_file.read_filename(command[1])
    except FileNotFoundError:
        print('The file {} cannot be found'.format(command[1]))


def print_line(command):
    """
    checks input is valid and runs print_num

    param       command: a list, [print, line number]
    pre         line number must be an integer or blank
    post        if line number is blank, all lines are printed
    post        if input is not valid, print_num is not executed
    post        if a file has not been read print_num is not executed
    complexity  best = worst: O(n)
    """
    try:
        if len(command) > 1:
            my_file.print_num(int(command[1]))
        else:
            my_file.print_num()
    except FileNotFoundError:
        print('No file has been read yet')
    except ValueError:
        print('The line number is not an integer')
    except IndexError:
        print('Line number is out of range')


def delete_line(command):
    """
    checks input is valid and runs delete_num

    param       command: a list, [delete, line number]
    pre         line number must be an integer or left blank
    post        if line number is left blank, all lines are deleted
    post        if input is not valid, delete_num is not executed
    post        if a file has not been read delete_num is not executed
    complexity  worst: O(n) where n is the size file. if deleting index from the start
    """
    try:
        if len(command) > 1:
            my_file.delete_num(int(command[1]))
        else:
            my_file.delete_num()
    except FileNotFoundError:
        print('No file has been read yet')
    except ValueError:
        print('The line number is not an integer')
    except IndexError:
        print('Line number is out of range')


def insert_line(command):
    """
    checks input is valid and runs insert_num, user can keep inserting lines until a full stop is entered

    param       command: a list, [insert, line number]
    pre         line number must be an integer within range
    post        if input is not valid, insert_num is not executed
    post        if a file has not been read delete_num is not executed
    complexity  best case: O(n) where n is the amount of lines being inserted
    complexity  worst case: O(n * m) where n is the number of lines being inserted and m is the length of the file
    """
    try:
        line_no = int(command[1])
        my_file.is_valid_index(line_no)
        print("Enter a line/s to add to the file. Enter a '.' when you are finished")
        line = input()
        while line != '.':
            my_file.insert_num(line, line_no)
            if line_no > 0:
                line_no += 1
            else:
                line_no -= 1
            line = input()
    except FileNotFoundError:
        print('No file has been read yet')
    except ValueError:
        print('The line number is not an integer')
    except IndexError:
        print('Line number is out of range')


def search_string(command):
    """
    checks input is valid and runs search

    param       command: a list, [insert, string]
    post        if a file has not been read delete_num is not executed
    complexity  best = worst: O(n * m) where n is the size of the file and m is size of each line in the file
    """
    try:
        my_file.search_string(command[1])
    except FileNotFoundError:
        print('No file has been read yet')


def undo():
    """
    checks input is valid and runs undo

    post        if an edit must be made delete_num is not executed
    post        if a file has not been read delete_num is not executed
    complexity  complexity  best = worst: O(1)
    """

    try:
        my_file.undo()
    except FileNotFoundError:
        print('No file has been read yet')
    except Exception:
        print('You must make an edit to undo')


def main():
    print('Text Editor\n-------------\nCommands:\n'
          'read [filename] -- reads the specified file\n'
          'print [num] -- prints the line at num, leave num blank to print the entire file\n'
          'delete [num] -- deletes the line at num, leave blank to delete the entire file\n'
          'insert [num] -- insert a string at line num\n'
          'search [string] -- returns the line numbers containing string\n'
          'undo -- undoes the last change you made to the file'
          'quit -- quits the program\n')

    quit_editor = False
    while quit_editor is False:

        command = input('Enter a command: ')
        command = command.strip()
        command = command.split(' ', 1)
        try:
            if command[0] == 'read':
                read_file_name(command)

            elif command[0] == 'print':
                print_line(command)

            elif command[0] == 'delete':
                delete_line(command)

            elif command[0] == 'insert':
                insert_line(command)

            elif command[0] == 'search':
                search_string(command)

            elif command[0] == 'undo':
                undo()

            elif command[0] == 'quit':
                quit_editor = True

            else:
                print('{} is an unknown command'.format(command[0]))

        except Exception:
            print('?')


if __name__ == '__main__':
    main()