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
    
    def dfs(box_index, visited):
        """
        Using depth-first search (DFS) to traverse the boxes.

        Args:
            box_index (int): Index of the box to explore.
            visited (set): Set containing indices of visited boxes.
        """
        visited.add(box_index)
        for key in boxes[box_index]:
            if key not in visited and key < len(boxes):
                dfs(key, visited)

    visited = set()
    dfs(0, visited)
    return len(visited) == len(boxes)
