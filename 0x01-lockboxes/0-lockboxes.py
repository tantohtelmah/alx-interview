#!/usr/bin/python3
"""
LockBoxes code
"""


def canUnlockAll(boxes):
    """ Initialize a set to keep track of visited boxes """

    visited = set()
    visited.add(0)  # Mark the first box as visited

    # Initialize a list to store the keys we have
    keys = [0]  # Start with the keys from the first box

    # Explore other boxes
    while keys:
        current_box = keys.pop()  # Get the last key
        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                visited.add(key)
                keys.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)
