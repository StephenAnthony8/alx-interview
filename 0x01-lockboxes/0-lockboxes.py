#!/usr/bin/python3
"""
lockboxes algorithm
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    """
    if not (boxes) or not isinstance(boxes, list):
        return False

    status = [0]
    for i in status:
        for item in boxes[i]:
            if item not in status and item < len(boxes):
                status.append(item)
    if len(status) == len(boxes):
        return True
    return False
