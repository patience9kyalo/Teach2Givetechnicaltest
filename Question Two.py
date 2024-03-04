# Write a program to generate the Fibonacci sequence up to 100.

# This program generates the Fibonacci sequence up to a given limit of 100.
# It starts with the initial sequence [0, 1] and iteratively generates the next Fibonacci number by summing up the last two numbers in the sequence.
# The process continues until the last number in the sequence exceeds the specified limit.
# The function returns the Fibonacci sequence up to, but not including, the number that exceeds the limit.
def generate_fibonacci(limit):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < limit:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence[:-1]

fib_sequence = generate_fibonacci(100)
for num in fib_sequence:
    print(num)
