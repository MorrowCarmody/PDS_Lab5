# Matt Carmody
# COSC 6375
# Lab 5 Part 1

import string

def is_palindrome(text):
    """Determine if a input is a palindrome."""
    # convert input to lowercase and remove spaces
    text = text.lower().replace(' ','')
    # remove punctuation from input
    text = text.translate(str.maketrans('', '', string.punctuation))
    stack = []
    reversed_text = ''

    for letter in text:
        stack.append(letter)

    while(len(stack) > 0):
        reversed_text += stack.pop()

    if(text == reversed_text):
        return True
    else:
        return False

print(is_palindrome('Don\'t nod!')) # True
print(is_palindrome('Racecar.'))    # True
print(is_palindrome('Applejuice'))  # False
