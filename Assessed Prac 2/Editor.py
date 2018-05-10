from task2 import List
from stack import Stack
import copy


class Editor:
    def __init__(self):
        """
        Created an instance of Editor

        post        an Editor is idealised
        post        the _text_lines list is empty at first
        post        the _undo_stack is empty at first
        complexity  best = worst: O(1)
        """
        self._text_lines = List()
        self._file_read = False
        self._undo_stack = Stack()
        self._performing_undo = False

    def read_filename(self, file_name):
        """
        imports the file into a list

        param       file_name: the name of the file you want to import
        pre         file name must be a string
        post        each line in the file will be added as a new item in the list
        complexity  complexity  best = worst: O(n) where n is the number of lines in the text file.
        """
        try:
            file = open(file_name, 'r')
        except Exception:
            raise FileNotFoundError('File not found')

        for line in file:
            self._text_lines.append(line.rstrip('\n'))

        self._file_read = True

        file.close()

    def print_num(self, line_num=None):
        """
        prints the line at the specified number or all lines if no number is given

        param       line_num: the line number of the line you want to print
        return      the line to be printed
        pre         line number must be an integer
        pre         the line number must be within range
        pre         a file must be read
        post        each line will be printed as a new line
        complexity  best = worst: O(n)
        """
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

        if line_num < 0:
            line_num = line_num + len(self._text_lines) + 1

        # checking line_num is within range
        if line_num < 1 or line_num > len(self._text_lines):
            raise IndexError('line_num is not within range')

        # printing line at line_num
        line = self._text_lines[line_num - 1]
        print(line)
        return line

    def delete_num(self, line_num=None):
        """
        Deletes the line at line_num and deletes all lines if no line_num is given

        param       line_num: the line number of the item you want to delete
        return      NA
        pre         line num must be an integer within range
        pre         file must be already read
        post        all items to the right of line_num will be shifted
        post        the length will become length - 1
        complexity  best: O(1) if deleting line at the end
        complexity  worst: O(n) where n is the size file. if deleting index from the start
        """
        # checking a file has been read
        if self._file_read is False:
            raise FileNotFoundError('No file has been read yet')

        if line_num is None:
            # for item in self._text_lines:
            list_copy = copy.deepcopy(self._text_lines)
            self._undo_stack.push(('delete_all', list_copy))
            self._text_lines = List()
            return

        # checking line_num is an integer
        try:
            line_num = int(line_num)
        except ValueError:
            raise ValueError('line_num must be an integer')

        if line_num < 0:
            line_num = line_num + len(self._text_lines) + 1

        # checking line_num is within range
        if line_num < 1 or line_num > len(self._text_lines):
            raise IndexError('line_num is not within range')

        # saving to the stack before deleting
        if self._performing_undo is False:
            self._undo_stack.push(('delete', line_num, self._text_lines[line_num - 1]))

        # deleting the line at num
        self._text_lines.delete(line_num - 1)

    def insert_num(self, item, line_num=None):
        """
        inserts and item at line_num

        param       item: the item you want to add into the given line_num
        param       line_num: the line number you want to add item in
        pre         a file must be read first
        pre         line_num must be an index within range
        post        all the items to the right of line_num will shift to the right
        complexity  best: O(1) if inserting at the end
        complexity  worst: O(n) where n is the length of file. If inserting at the start
        """
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

        if line_num < 0:
            line_num = line_num + len(self._text_lines) + 1

        # checking line_num is within range
        if line_num < 1 or line_num > len(self._text_lines) + 1:
            raise IndexError('line_num is not within range')

        # inserting items at line num
        if item == '.':
            return

        if line_num > len(self._text_lines):
            self._text_lines.append(item)
        else:
            self._text_lines.insert(line_num - 1, item)

        # Adds inserted item to the stack
        if self._performing_undo is False:
            self._undo_stack.push(('insert', line_num))

    def search_string(self, string):
        """
        searches for an string in each line of the file

        param       string: the string you want to search for
        return      each line the string appears in
        pre         a file must be read
        post        if string is not found, an empty string is returned
        complexity  best = worst: O(n * m) where n is the size of the file and m is size of each line in the file
        """
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
        """
        Undoes the last change made to the file

        pre         a file must be read
        pre         at least one change to the file must have been made
        post        the last change to the file is undone
        complexity  best = worst: O(1)
        """
        # checking a file has been read
        if self._file_read is False:
            raise FileNotFoundError('No file has been read yet')

        # checking there is something to undo
        if self._undo_stack.is_empty():
            raise Exception('The stack is empty')

        self._performing_undo = True
        last_line = self._undo_stack.pop()
        if last_line[0] == 'insert':
            self.delete_num(last_line[1])
        elif last_line[0] == 'delete':
            self.insert_num(last_line[2], last_line[1])
        elif last_line[0] == 'delete_all':
            self._text_lines = last_line[1]
        self._performing_undo = False

    def is_valid_index(self, line_num):
        """
        checks that a index is within range of the file

        param       line_num: the line number to be checked
        pre         line_num must be an integer
        pre         a file must be read
        post        if the integer is not in range, an exception is raised
        complexity  best = worst: O(1)
        """
        if line_num < 0:
            line_num = line_num + len(self._text_lines) + 1

        # checking line_num is within range
        if line_num < 1 or line_num > len(self._text_lines) + 1:
            raise IndexError('line_num is not within range')

