# Matt Carmody
# COSC 6375
# Lab 5 Part 1

def is_palindrome(string):
    """Determine if a string is a palindrome."""
    string = string.lower()
    stack = []

    for letter in string:
        stack.append(letter)

    word = ''.join(stack)
    print(word)

    stack.reverse()
    word_reversed = ''.join(stack)
    print(word_reversed)

    if(word == word_reversed):
        print('true')
        return True
    else:
        print('false')
        return False

is_palindrome('THIS IS A STRING')
is_palindrome('racecar')

"""
INSTRUCTIONS:
Take a string and returns True if it is a palindrome and False otherwise. Use a stack (simulated
with a list as we did in Section 5.11) to help determine whether a string is a palindrome. Your function
should ignore case sensitivity (that is, 'a' and 'A' are the same), spaces and punctuations.
"""