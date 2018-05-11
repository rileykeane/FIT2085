from task1 import HashTable 
import timeit


def read_text_file(name):
    """
    Imports a text file into a list

    param       name: the name of the file you want to import
    return      The list containing each line of the file
    pre         name must be a string
    pre         the file you are importing must exist within the directory of the code
    post        the list with have each line as a new item
    complexity  best = worst: O(n) where n is the number of lines in the text file.
    """

    if type(name) is not str:
        raise ValueError('name must be a string')

    file = open(name, 'r')
    file_list = []

    for line in file:
        file_list.append(line.strip('\n'))

    file.close()

    return file_list


b_values = [1, 27183, 250726]
table_sizes = [250727, 402221, 1000081]
dict_files = ['english_small.txt', 'english_large.txt', 'french.txt']

results = open("task2_results.csv", "w")
result_tiles = "File" + "," + "b" + "," + "Table Size" + "," + "Time"
results.write(result_tiles + '\n')

for dictionary in dict_files:
    keys = read_text_file(dictionary)
    results.write(str(dictionary) + '\n')

    for size in table_sizes:
        for b in b_values:
            hash_table = HashTable(size, b)
            start = timeit.default_timer()
            for key in keys:
                hash_table[key] = 1
            time = (timeit.default_timer() - start)
            hash_result = "" + "," + str(b) + "," + str(size) + "," + str(time)
            results.write(hash_result + "\n")

results.close()

