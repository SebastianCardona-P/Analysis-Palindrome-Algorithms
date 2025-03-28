from palindrome import execution_time_gathering
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    minimum_size = 10000
    maximum_size = 100000
    step = 10000
    samples_by_size = 7

    sizes = []
    two_pointers_times = []
    reverse_times = []
    iterators_times = []
    recursive_times = []

    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)
    print("Size | Two Pointers | Reverse | Iterators | Recursive")
    for row in table:
        print(row)
        sizes.append(row[0])
        two_pointers_times.append(row[1])
        reverse_times.append(row[2])
        iterators_times.append(row[3])
        recursive_times.append(row[4])

    plt.figure(figsize=(10, 6))

    plt.plot(sizes, two_pointers_times, marker='o', linestyle='-', label='Two Pointers', color='blue')
    plt.plot(sizes, reverse_times, marker='^', linestyle='-.', label='Reverse', color='green')
    plt.plot(sizes, iterators_times, marker='x', linestyle=':', label='Iterators', color='purple')
    plt.plot(sizes, recursive_times, marker='d', linestyle='-.', label='Recursive', color='orange')

    plt.xlabel('String Size')
    plt.ylabel('Execution time (ns)')
    plt.title('Time comparison between palindrome algorithms')
    plt.legend()
    plt.grid()

    plt.show()

    x = np.arange(len(sizes))
    width = 0.2  # bar width

    plt.subplot(1, 2, 2)  # second
    plt.bar(x - width, two_pointers_times, width=width, label='Two Pointers', color='blue')
    plt.bar(x + width, reverse_times, width=width, label='Reverse', color='green')
    plt.bar(x + width, iterators_times, width=width, label='Iterators', color='purple')
    plt.bar(x + width, recursive_times, width=width, label='Recursive', color='orange')
    plt.xlabel('String Size')
    plt.ylabel('Execution time (ns)')
    plt.xticks(ticks=x, labels=sizes)
    plt.title('Execution Time Comparison (Bar Chart)')
    plt.legend()
    plt.grid(axis='y')

    plt.tight_layout()
    plt.show()


