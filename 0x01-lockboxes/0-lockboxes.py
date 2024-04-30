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
        return False  # Empty boxes list, cannot unlock anything
    
    # Initialize a set to keep track of visited boxes
    visited = set()
    
    # Initialize a list to keep track of boxes to be explored
    to_explore = [0]  # Start with box 0
    
    while to_explore:
        current_box = to_explore.pop()  # Get the next box to explore
        
        # Mark the current box as visited
        visited.add(current_box)
        
        # Add unvisited boxes to the list of boxes to explore
        for key in boxes[current_box]:
            if key not in visited and key not in to_explore and key < len(boxes):
                to_explore.append(key)
    
    return len(visited) == len(boxes)