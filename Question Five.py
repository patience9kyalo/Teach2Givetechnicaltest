# Write a program that takes an integer as input and returns an integer with reversed digit ordering.

# This code defines a function called reverse_digits that takes an integer n as input and returns an integer with its digits reversed.
# If the input number is negative, it converts it to positive, reverses its digits, and adds back the negative sign to the result.
# Within the function, it iterates through the digits of the number using a while loop, extracting them one by one and storing them in a list.
# After extracting all the digits, it joins them back together in reverse order to form the reversed number.
# Finally, it returns the reversed number as an integer.

def reverse_digits(n):
    if n == 0:
        return 0
    elif n < 0:
        return -reverse_digits(-n)
    else:
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10
        return int(''.join(str(d) for d in digits))

n = 875646
reversed_n = reverse_digits(n)
print(reversed_n)