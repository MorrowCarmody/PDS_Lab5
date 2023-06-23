# Matt Carmody
# COSC 6375
# Lab 5 Part 1

import string

def is_palindrome(input):
    """Determine if a input is a palindrome."""
    # convert input to lowercase and remove spaces
    input = input.lower().replace(' ','')
    # remove punctuation from input
    input = input.translate(str.maketrans('', '', string.punctuation))
    stack = []
    reversed_input = ''

    for letter in input:
        stack.append(letter)

    while(len(stack) > 0):
        reversed_input += stack.pop()

    if(input == reversed_input):
        return True
    else:
        return False

print(is_palindrome('Don\'t nod!')) # True
print(is_palindrome('Racecar.'))    # True
print(is_palindrome('Applejuice'))  # False
