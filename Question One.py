# Write a program that prints the numbers from 1 to 100. For multiples of 3, it prints"fizz"; for multiples of 5 it prints"Buzz" ; and for numbers that are both multiples of 3 and 5 it prints " FizzBuzz".

# I used a for loop to iterate over the numbers from 1 to 100 (inclusive).
# For each number, it checks if it's divisible by 3, 5, or both, and prints the appropriate message.
# If the number is not divisible by either 3 or 5, the program simply prints the number.
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)