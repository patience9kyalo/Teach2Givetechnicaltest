# Write a program that accepts a string as input , capitalizes the first letter of each word in the string, and the returns the result string

# The function capitalize_first_letters(input_string) takes a string input_string as input and returns a new string with the first letter of each word capitalized.
# The function first splits the input string into a list of words using the split() method.
# It then loops through each word and checks if the first character is a letter using the isalpha() method.
# If it is, the function capitalizes it using the upper() method and concatenates it with the rest of the word (excluding the first letter) using slicing.
# If the first character is not a letter, the function simply appends the word as is.
# Finally, the function joins all the capitalized words in the list using the join() method with a space character as the separator and returns the resulting string.
def capitalize_first_letters(input_string):
    words = input_string.split()
    capitalized_words = []
    for word in words:
        first_letter = word[0]
        if first_letter.isalpha():
            capitalized_words.append(first_letter.upper() + word[1:])
        else:
            capitalized_words.append(word)
    result_string = ' '.join(capitalized_words)
    return result_string


input_string = "patience is key"
capitalized_string = capitalize_first_letters(input_string)
print(capitalized_string)