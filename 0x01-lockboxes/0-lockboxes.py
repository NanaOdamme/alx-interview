#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def canUnlockAll(boxes):
    """
    Function to determine if all boxes can be opened.

    Args:
        boxes (list): List that contains all boxes with keys.
        
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False
    visited = set()
    to_explore = [0]
    
    while to_explore:
        current_box = to_explore.pop()
        visited.add(current_box)

        for key in boxes[current_box]:
            if key not in visited and key not in to_explore and key < len(boxes):
                to_explore.append(key)
    
    return len(visited) == len(boxes)