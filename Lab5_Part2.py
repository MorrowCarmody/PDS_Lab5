# Matt Carmody
# COSC 6375
# Lab 5 Part 2

def is_ordered(sequence):
    """Determine if the elements of a sequence are in sorted order."""
    for i in range(len(sequence)):
        print(sequence[i])
    return

"""
INSTRUCTIONS:
Receive a sequence and returns True if the elements are in sorted order. Test your function with
sorted and un-sorted lists, tuples and strings.
"""

is_ordered([0,1,2,3])       # sorted list       -   True
is_ordered([0,5,10,15,3])   # unsorted list     -   False
is_ordered((0,1,2,3))       # sorted tuple      -   True
is_ordered((0,1,2,4,3))     # unsorted tuple    -   False
is_ordered('abcd')          # sorted string     -   True
is_ordered('abdc')          # unsorted string   -   False
