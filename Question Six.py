#Write a program that counts the number of vowels in a sentence.

#This code defines a function count_vowels that takes a sentence as input and returns the count of vowels present in it.
# It initializes a string variable vowels containing all the lowercase vowels. Then, it converts the input sentence to lowercase to ensure case insensitivity.
# It iterates through each character in the sentence using a for loop, checking if each character is a vowel by comparing it to the characters in the vowels string.
# If a character is found to be a vowel, the counter count is incremented.
# Finally, it returns the total count of vowels in the sentence.
def count_vowels(sentence):
    vowels = 'aeiou'
    sentence = sentence.lower()
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

# Example usage:
sentence = "This is way too big for me"
num_vowels = count_vowels(sentence)
print(num_vowels)