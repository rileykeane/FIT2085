from Editor import Editor
my_file = Editor()


def read_file_name(command):
    try:
        my_file.read_filename(command[1])
    except FileNotFoundError:
        print('The file {} cannot be found'.format(command[1]))


def print_line(command):
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
    try:
        line_no = int(command[1])
        print("Enter a line/s to add to the file. Enter a '.' when you are finished")
        line = input()
        while line != '.':
            my_file.insert_num(line, line_no)
            line_no += 1
            line = input()
    except FileNotFoundError:
        print('No file has been read yet')
    except ValueError:
        print('The line number is not an integer')
    except IndexError:
        print('Line number is out of range')


def search_string(command):
    try:
        my_file.search_string(command[1])
    except FileNotFoundError:
        print('No file has been read yet')


def undo():
    my_file.undo()


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


main()