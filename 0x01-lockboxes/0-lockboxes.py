#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def canUnlockAll(boxes):
    """
    function to unlock all boxes

    Args:
        boxes (list): list that contains all boxes with keys
    """
    
    
    def dfs(box_index, visited):
        """
    using a depth-first search (DFS) to traverse the boxes

    Args:
        box_index (dict): opened bok with key
    """
        visited.add(box_index)
        for key in boxes[box_index]:
            if key not in visited and key < len(boxes):
                dfs(key, visited)

    visited = set()
    dfs(0, visited)
    return len(visited) == len(boxes)