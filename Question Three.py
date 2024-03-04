# Write a program that takes an integer as input and returns true if the input is a power of two.

# The expression (n > 0) returns False if n is less than or equal to 0, and (n & (n - 1)) == 0 returns False if n is not a power of two.
# The and operator combines these two conditions, so that the function returns False if either condition is not met.
def is_power_of_two(n):
    if n <= 0:
        return False
    else:
        return (n & (n - 1)) == 0

n = 9
print(is_power_of_two(n))