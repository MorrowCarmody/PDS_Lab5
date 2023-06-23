# Matt Carmody
# COSC 6375
# Lab 5 Part 2

def is_ordered(sequence):
    """Determine if the elements of a sequence are in sorted order."""
    length = len(sequence)

    for i in range(1, length):
        # increasing sequence
        if(sequence[i] > sequence[i-1]):
            if(((i+1) < length) and (sequence[i+1] < sequence[i])):
                return False
        # decreasing sequence
        elif(sequence[i] < sequence[i-1]):
            if(((i+1) < length) and (sequence[i+1] > sequence[i])):
                return False
    return True

print(is_ordered([0,1,2,3]))        # sorted list (increasing)      -   True
print(is_ordered([3,2,1,0]))        # sorted list (decreasing)      -   True
print(is_ordered([0,5,10,15,3]))    # unsorted list                 -   False
print(is_ordered((0,1,2,3)))        # sorted tuple (increasing)     -   True
print(is_ordered((3,2,1,0)))        # sorted tuple (decreasing)     -   True
print(is_ordered((0,1,2,4,3)))      # unsorted tuple                -   False
print(is_ordered('abcd'))           # sorted string (increasing)    -   True
print(is_ordered('dcba'))           # sorted string (decreasing)    -   True
print(is_ordered('abdc'))           # unsorted string               -   False
print(is_ordered([0]))              # single item                   -   True by default
print(is_ordered([0, 1]))           # two items                     -   True by default
