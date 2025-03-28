import time
from palindrome.data_generator import get_random_strings
from palindrome.algorithms import (
    is_palindrome_reverse,
    palindrome_two_pointers,
    is_palindrome_iterators,
    is_palindrome_recursive,
)
from palindrome.constants import TIME_MULTIPLIER


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print(f"Computing execution time for size {size}")
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)

    return return_table


"""
    It will return 5 values, one per algorithm: The execution time
"""


def take_times(size, samples_by_size):
    samples = [get_random_strings(size, samples_by_size, ensure_palindrome=True)]

    return [
        take_time_for_algorithm(samples, "two_pointers"),
        take_time_for_algorithm(samples, "reverse"),
        take_time_for_algorithm(samples, "iterators"),
        take_time_for_algorithm(samples, "recursive"),
    ]


"""
    Returns the median of the execution time
"""


def take_time_for_algorithm(samples, algorithm):
    times = []

    if algorithm == "two_pointers":
        for sample in samples:
            start = time.time()
            palindrome_two_pointers(sample)
            end = time.time()
            times.append(TIME_MULTIPLIER * (end - start))

    elif algorithm == "reverse":
        for sample in samples:
            start = time.time()
            is_palindrome_reverse(sample)
            end = time.time()
            times.append(TIME_MULTIPLIER * (end - start))
    elif algorithm == "iterators":
        for sample in samples:
            start = time.time()
            is_palindrome_iterators(sample)
            end = time.time()
            times.append(TIME_MULTIPLIER * (end - start))
    elif algorithm == "recursive":
        for sample in samples:
            start = time.time()
            is_palindrome_recursive(sample)
            end = time.time()
            times.append(TIME_MULTIPLIER * (end - start))

    times.sort()
    return times[len(times) // 2]
