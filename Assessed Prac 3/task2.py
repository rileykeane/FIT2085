from task1 import HashTable 
import timeit


def import_keys(keys_file, b, size):
    """
    Imports a file of keys into a hash table

    :param      keys_file: a file containing all the keys you want in the table
    :param      b: the b value used in the hash function 
    :param      size: the size you want the hash table to be
    :return     The hash table with all the keys
    :pre        the keys in the file must all be strings 
    :pre        keys_file must be a string and a file within the project file
    :pre        b and size must be integers 
    :post       all keys will be put in the table with the data as integer 1
    :complexity best= worst = O(n) where n is the size of keys_file
    """
    if type(keys_file) is not str:
        raise ValueError('keys_file must be a string')

    # importing keys from text
    file = open(keys_file, 'r')
    hash_table = HashTable(size, b)
    for key in file:
        key = key.strip('\n')
        hash_table[key] = 1
    file.close()

    return hash_table

def main():
    b_values = [1, 27183, 250725]
    table_sizes = [250727, 402221, 1000081]
    dict_files = ['english_small.txt', 'english_large.txt', 'french.txt']

    # created a csv file to import results into
    results = open("results/task2_results.csv", "w")
    result_tiles = "File" + "," + "b" + "," + "Table Size" + "," + "Time"
    results.write(result_tiles + '\n')

    # testing times for each file and each combination of size and b
    for dictionary in dict_files:
        results.write(dictionary + '\n')
        for size in table_sizes:
            for b in b_values:
                start = timeit.default_timer()
                import_keys("text_files/" + dictionary, b, size)
                time = (timeit.default_timer() - start)
                hash_result = "" + "," + str(b) + "," + str(size) + "," + str(time)
                results.write(hash_result + "\n")
        print(dictionary + ' completed')

    results.close()


if __name__ == "__main__":
    main()
