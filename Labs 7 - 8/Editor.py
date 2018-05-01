from task2 import List
from stack import Stack


class Editor:
    def __init__(self):
        self._text_lines = List()
        self._file_read = False
        self._undo_stack = Stack()
        self._performing_undo = False

    def read_filename(self, file_name):
        try:
            file = open(file_name, 'r')
        except Exception:
            raise FileNotFoundError('File not found')

        for line in file:
            self._text_lines.append(line.rstrip('\n'))

        self._file_read = True

        file.close()

    def print_num(self, line_num=None):
        # checking a file has been read
        if self._file_read is False:
            raise FileNotFoundError('No file has been read yet')

        # if no line_num is given print evey line
        if line_num is None:
            print(self._text_lines)
            return str(self._text_lines)

        # checking line_num is an integer
        try:
            int(line_num)
        except ValueError:
            raise ValueError('line_num must be an integer')

        # checking line_num is within range
        if line_num < 1 or line_num > len(self._text_lines):
            raise IndexError('line_num is not within range')

        # printing line at line_num
        line = self._text_lines[line_num - 1]
        print(line)
        return line

    def delete_num(self, line_num=None):
        # checking a file has been read
        if self._file_read is False:
            raise FileNotFoundError('No file has been read yet')

        if line_num is None:
            self._text_lines = List()
            return

        # checking line_num is an integer
        try:
            line_num = int(line_num)
        except ValueError:
            raise ValueError('line_num must be an integer')

        # checking line_num is within range
        if line_num < 1 or line_num > len(self._text_lines):
            raise IndexError('line_num is not within range')

        # saving to the stack before deleting
        if self._performing_undo is False:
            self._undo_stack.push(('delete', line_num, self._text_lines[line_num - 1]))

        # deleting the line at num
        self._text_lines.delete(line_num - 1)

    def insert_num(self, item, line_num=None):
        # checking a file has been read
        if self._file_read is False:
            raise FileNotFoundError('No file has been read yet')

        # checking the user entered a line num
        if line_num is None:
            raise Exception('a line_num must be provided')

        # checking line_num is an integer
        try:
            line_num = int(line_num)
        except ValueError:
            raise ValueError('line_num must be an integer')

        # checking line_num is within range
        if line_num < 1 or line_num > len(self._text_lines) + 1:
            raise IndexError('line_num is not within range')

        if item == '.':
            return
        elif line_num <= len(self._text_lines):
            self._text_lines.insert(line_num - 1, item)
        else:
            self._text_lines.append(item)

        if self._performing_undo is False:
            self._undo_stack.push(('insert', line_num))

    def search_string(self, string):
        # checking a file has been read
        if self._file_read is False:
            raise FileNotFoundError('No file has been read yet')

        string_lines = List()
        for i in range(len(self._text_lines)):
            if string in self._text_lines[i]:
                string_lines.append(i + 1)
        print('{} occurs on lines:'.format(string))
        print(string_lines)
        return str(string_lines)

    def undo(self):
        self._performing_undo = True
        last_line = self._undo_stack.pop()
        if last_line[0] == 'insert':
            self.delete_num(last_line[1])
        elif last_line[0] == 'delete':
            self.insert_num(last_line[2], last_line[1])
        self._performing_undo = False









