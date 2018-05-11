from task1 import HashTable
from task2 import import_keys
import timeit

def main():
    b_values = [1, 27183, 250725]
    table_sizes = [250727, 402221, 1000081]
    dict_files = ['english_small.txt', 'english_large.txt', 'french.txt']

    # created a csv file to import results into
    results = open("results/task3_results.csv", "w")
    result_tiles = "File" + "," + "b" + "," + "Table Size" + "," + "Time" + "," + "Collisions" + "," + "Total probes"\
        + "," + "Logest Probe" + "," +"Rehashes"
    results.write(result_tiles + '\n')

    # testing times for each file and each combination of size and b
    for dictionary in dict_files:
        results.write(dictionary + '\n')
        for size in table_sizes:
            for b in b_values:
                start = timeit.default_timer()
                hash_table = import_keys("text_files/" + dictionary, b, size)
                collision_data = hash_table.collision_info()
                time = (timeit.default_timer() - start)
                hash_result = "" + "," + str(b) + "," + str(size) + "," + str(time) + "," + str(collision_data[0])\
                    + "," + str(collision_data[1]) + "," + str(collision_data[2]) + "," + str(collision_data[3]) 
                results.write(hash_result + "\n")
        print(dictionary + ' completed')

    results.close()


if __name__ == "__main__":
    main()
