# Palindrome Analysis

## Escuela Colombiana de Ingeniería Julio Garavito  
**Author:** Sebastian Cardona Parra  
**Professor:** Rafael Alberto Niquefa Velasquez  
**2025-1**  

## Introduction
The task of detecting whether a given string is a palindrome is fundamental in various fields such as text analysis, bioinformatics, and software optimization. This report analyzes five different palindrome detection algorithms: Two-pointers, Reverse, Iterators, and Recursion, comparing their efficiency in terms of execution time and computational complexity.

## Algorithms

### Two-pointers Algorithm
The two-pointers algorithm uses two pointers, one starting from the beginning of the string and the other from the end, comparing characters one by one.
- **Worst case:** O(n)
- **Best case:** O(1) when the string is empty or consists of a single character.
- **Average case:** O(n)
- **Characteristics:** Simple and efficient for most cases.

### Reverse Algorithm
The reverse algorithm compares the original string with its reversed version to check if they are identical.
- **Worst case:** O(n)
- **Best case:** O(1) when the string is empty or consists of a single character.
- **Average case:** O(n)
- **Characteristics:** Simple to implement, but requires additional space for storing the reversed string.

### Iterators Algorithm
This algorithm uses iterators to traverse the string from both ends, comparing characters as it iterates.
- **Worst case:** O(n)
- **Best case:** O(1) when the string is empty or consists of a single character.
- **Average case:** O(n)
- **Characteristics:** Efficient and avoids the need for extra space, although slightly less intuitive than two-pointers.

### Recursive Algorithm
The recursion algorithm checks if the first and last characters of the string match, and recursively checks the substring between them.
- **Worst case:** O(n)
- **Best case:** O(1) when the string is empty or consists of a single character.
- **Average case:** O(n)
- **Characteristics:** Elegant and simple, but may not be optimal for very large strings due to recursion depth limitations.

## Performance Analysis
The algorithms were implemented in Python, and execution times were measured for different string sizes. The results are presented in both line charts and bar charts for better visualization.


### Key Observations
- **Two-pointers is the most efficient** algorithm in terms of time complexity, operating in O(n) without requiring extra memory.
- **Reverse is simple** but not space-efficient, as it requires additional space for the reversed string.
- **Iterators offer a space-efficient approach,** but can be slightly less intuitive than two-pointers.
- **Recursion offers a clean solution,** but may be less efficient due to recursion depth limitations and the overhead of function calls.


## Conclusions
1. Two-pointers is the best choice for general-purpose palindrome detection due to its time and space efficiency.
2. Stack-based approach should be avoided for larger strings due to its extra space requirement.
3. Reverse is simple, but its space requirement makes it less optimal for large strings.
4. Iterators offer a good trade-off between time and space efficiency.
5. Recursion is elegant, but may not scale well with large strings due to recursion depth and function call overhead.


## Coverage

The coverage of the tests is 89% as shown below:

to see the coverage of the tests, run the following command:
1. coverage run -m unittest discover
2. coverage report

```
Name                           Stmts   Miss  Cover
--------------------------------------------------
palindrome\__init__.py             0      0   100%
palindrome\algorithms.py          25      8    68%
palindrome\data_generator.py       9      0   100%
test\__init__.py                   0      0   100%
test\test_algorithm.py            28      1    96%
test\test_data_generator.py       28      1    96%
--------------------------------------------------
TOTAL                             90     10    89%
```

## Graphics

The following graphics show the performance of the algorithms for different string sizes:

* Parameters:
- minimum_size = 10000
- maximum_size = 100000
- step = 5000
- samples_by_size = 7
- is palindrome = True

![image](https://github.com/user-attachments/assets/a1bc8694-70ba-4833-864b-9329895adf97)

![image](https://github.com/user-attachments/assets/83766235-10c3-4585-9d67-d88abbc1d669)


* Parameters:
- minimum_size = 10000
- maximum_size = 100000
- step = 5000
- samples_by_size = 7
- is palindrome = False

![image](https://github.com/user-attachments/assets/f1317fc5-f1c3-472f-9c3a-0a28007886fc)

![image](https://github.com/user-attachments/assets/c011d853-13fe-4123-9c6f-c2667f66d6f0)


In all cases, the times are competitive

## Repository
This repository contains:
- **Python implementations** of the palindrome detection algorithms (Two-pointers, Reverse, Iterators, Recursion).
- **Performance analysis scripts** to measure execution times.
- **Graphical comparisons** illustrating algorithm performance across different string sizes.
