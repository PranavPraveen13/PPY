"""8.
Extend the previous Python program to write the output to a file and perform operations on that file.

  a. ...

  b. ...

  c. ...

  d. ...

  e. ...

  f. ...

  g. ...

  h. Write Output to File: Write all the results (original inputs, modified data structures, type conversion results) to a file.

  i. Perform Operations on File: Open the file, read its content, and perform some operations like counting the number of lines, finding specific data, etc.

  j. Modify File Content: Modify the content of the file by, for example, changing specific lines or adding new lines.
"""

# Input
input_numbers = input("Enter a series of space-separated integers: ")

# Convert Input
numbers_list = list(map(int, input_numbers.split()))
numbers_tuple = tuple(numbers_list)

# Manipulate List
numbers_list.append(10)
numbers_list.insert(2, 20)
numbers_list.remove(8)

# Attempt to Modify Tuple (this will raise an error)
try:
    numbers_tuple.append(10)  # Attempting to modify tuple
except (TypeError, AttributeError):
    print("Tuples are immutable and cannot be modified.")

# Set Operations
numbers_set = set(numbers_list)
set_union = numbers_set.union({11, 12})
set_intersection = numbers_set.intersection({0, 9})
set_difference = numbers_set.difference({2, 8})

# Dictionary Operations
numbers_dict = {x: x ** 2 for x in numbers_list}
print("Original Dictionary:", numbers_dict)
numbers_dict[11] = 121
del numbers_dict[5]

# Type Conversion
list_to_tuple = tuple(numbers_list)
list_to_set = set(numbers_list)
list_to_dict = dict(zip(numbers_list, [x ** 2 for x in numbers_list]))

tuple_to_list = list(numbers_tuple)
tuple_to_set = set(numbers_tuple)
tuple_to_dict = dict(zip(numbers_tuple, [x ** 2 for x in numbers_tuple]))

set_to_list = list(numbers_set)
set_to_tuple = tuple(numbers_set)
set_to_dict = dict(zip(numbers_set, [x ** 2 for x in numbers_set]))

dict_to_list = list(numbers_dict.keys())
dict_to_tuple = tuple(numbers_dict.keys())
dict_to_set = set(numbers_dict.keys())

student_number = input("Enter your student number: ")
# Write Output to File like this:
file_name = "output.txt"
with open(file_name, "w") as f:
    f.write("Student Number: " + student_number + "\n\n")
    f.write("Original List: " + str(numbers_list) + "\n")
    f.write("Original Tuple: " + str(numbers_tuple) + "\n")
    f.write("Original Set: " + str(numbers_set) + "\n")
    f.write("Original Dictionary: " + str(numbers_dict) + "\n\n")

    f.write("Manipulated List: " + str(numbers_list) + "\n")
    f.write("Manipulated Tuple: " + str(numbers_tuple) + "\n")
    f.write("Union of Set: " + str(set_union) + "\n")
    f.write("Intersection of Set: " + str(set_intersection) + "\n")
    f.write("Difference of Set: " + str(set_difference) + "\n")
    f.write("Updated Dictionary: " + str(numbers_dict) + "\n\n")

    f.write("List to Tuple: " + str(list_to_tuple) + "\n")
    f.write("List to Set: " + str(list_to_set) + "\n")
    f.write("List to Dictionary: " + str(list_to_dict) + "\n")
    f.write("Tuple to List: " + str(tuple_to_list) + "\n")
    f.write("Tuple to Set: " + str(tuple_to_set) + "\n")
    f.write("Tuple to Dictionary: " + str(tuple_to_dict) + "\n")
    f.write("Set to List: " + str(set_to_list) + "\n")
    f.write("Set to Tuple: " + str(set_to_tuple) + "\n")
    f.write("Set to Dictionary: " + str(set_to_dict) + "\n")
    f.write("Dictionary to List: " + str(dict_to_list) + "\n")
    f.write("Dictionary to Tuple: " + str(dict_to_tuple) + "\n")
    f.write("Dictionary to Set: " + str(dict_to_set) + "\n")

# print "Content of the file:"
with open(file_name, "r") as f:
    content = f.read()
print("Content of the file:")
print(content)
# Perform Operations on File:

#   Count the number of lines in the file
num_lines = content.count('\n') + 1
print("Number of lines in the file:", num_lines)

#   Count the number of integers in the file
import re

num_integers = len(re.findall(r'\b\d+\b', content))
print("Number of integers in the file:", num_integers)

# Add all integers in the file (sum)
all_integers = [int(x) for x in re.findall(r'\b\d+\b', content)]
total_sum = sum(all_integers)
print("Sum of all integers in the file:", total_sum)

#   Modify the content of the file
new_content = content + "\nThis is a new line appended to the file.\n"
with open(file_name, "w") as f:
    f.write(new_content)

print("Content of the file after modification:")
print(new_content)

"""--------------------------------------------------------------------------------
**Control Statements:**
Control statements are used in programming to alter the flow of execution based on certain conditions or criteria. In Python, commonly used control statements include:

`if, elif, else:` These statements are used for conditional execution. They allow the program to execute different blocks of code based on specified conditions.

`for loop:` Used for iterating over a sequence (such as lists, tuples, strings, etc.) or any iterable object. It allows you to execute a block of code repeatedly for each item in the sequence.

`while loop:` Used for executing a block of code repeatedly as long as a specified condition is true. It keeps iterating until the condition becomes false.


**Loops:**
Loops are used for executing a block of code repeatedly. In Python, there are two main types of loops:

`for loop: `As mentioned earlier, the for loop iterates over a sequence or any iterable object.

`while loop:` This loop executes a block of code as long as a specified condition is true. It continues iterating until the condition becomes false.

**Other Statements:**
This category typically includes other types of statements that don't fall directly under control statements or loops. It can include various types of statements used for different purposes in Python programming, such as:

`Assignment statements:` Assigning values to variables.

`Function calls:` Invoking functions to perform specific tasks.

`Import statements:` Importing modules or packages to use their functionality in the current script or program.

`Exception handling statements: `Statements used for handling exceptions (errors) that may occur during the execution of a program, such as try, except, finally, etc.

`With statements: `Used for resource management, especially for working with files, to ensure that certain resources are properly closed or released after use.

These are fundamental constructs in Python programming that enable you to control the flow of your program, repeat tasks efficiently, and execute various types of statements to achieve desired functionality.

-------------------------------------------------------------------------------

9.  Utilizing the Largest Integer from output.txt

  Task Description:

  Transform the previous task to utilize the largest integer from the output file 'output.txt' instead of asking the user for it.

  1. Read the largest integer from the 'output.txt' file.
  2. Generate a list of all prime numbers up to the largest integer.
  3. Print the list of prime numbers.
  4. Calculate the sum of all prime numbers in the list.
  5. Determine the largest and smallest prime numbers in the list.
  6. Check if the largest integer itself is prime and print the result.
  7. Write the list of prime numbers along with the sum, largest, and smallest prime numbers to a file 'prime_numbers.txt'.
  8. Handle the scenario where the largest integer cannot be found in the file.

  Example:

  If the 'output.txt' file contains:
  Largest prime number: 20

  The program will generate the list of prime numbers up to 20, perform calculations, and write the results to 'prime_numbers.txt'.
"""
import re
import math


def find_largest_integer(filename):
    largest_integer = None
    with open(filename, 'r') as file:
        content = file.read()
        integers = [int(x) for x in re.findall(r'\b\d+\b', content)]
        if integers:
            largest_integer = max(integers)
    return largest_integer


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def write_prime_numbers(filename, primes, prime_sum, largest_prime, smallest_prime, largest_integer_prime):
    with open(filename, 'w') as file:
        file.write("List of Prime Numbers: ")
        file.write(", ".join(map(str, primes)) + "\n")
        file.write("Sum of Prime Numbers: " + str(prime_sum) + "\n")
        file.write("Largest Prime Number: " + str(largest_prime) + "\n")
        file.write("Smallest Prime Number: " + str(smallest_prime) + "\n")
        file.write("Is Largest Integer Itself Prime?: " + str(largest_integer_prime) + "\n")


# Read the largest integer from the output.txt file
largest_integer = find_largest_integer('output.txt')

if largest_integer:
    # Generate a list of all prime numbers up to the largest integer
    primes = generate_primes(largest_integer)

    if primes:
        # Print the list of prime numbers
        print("List of Prime Numbers:", primes)

        # Calculate the sum of all prime numbers in the list
        prime_sum = sum(primes)
        print("Sum of Prime Numbers:", prime_sum)

        # Determine the largest and smallest prime numbers in the list
        largest_prime = max(primes)
        smallest_prime = min(primes)
        print("Largest Prime Number:", largest_prime)
        print("Smallest Prime Number:", smallest_prime)

        # Check if the largest integer itself is prime
        largest_integer_prime = is_prime(largest_integer)
        print("Is Largest Integer Itself Prime?:", largest_integer_prime)

        # Write the list of prime numbers along with the sum, largest, and smallest prime numbers to a file 'prime_numbers.txt'
        write_prime_numbers('prime_numbers.txt', primes, prime_sum, largest_prime, smallest_prime,
                            largest_integer_prime)

    else:
        print("No prime numbers found up to the largest integer.")
else:
    print("Error: Largest integer not found in 'output.txt'.")

"""10.
In the final main.py file, leave the results from task 8 and 9, commit and push
"""
