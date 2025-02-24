#!/usr/bin/python3

def rain(walls):
    """
    Calculate the total amount of rainwater retained after it rains.
    
    Args:
        walls (list of int): List of non-negative integers representing wall heights.
    
    Returns:
        int: Total amount of rainwater retained.
    """
    if not walls:
        return 0
    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n
    
    # Compute left_max
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], walls[i])
    
    # Compute right_max
    right_max[-1] = walls[-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i])
    
    # Calculate total water retained
    total_water = 0
    for i in range(n):
        total_water += max(0, min(left_max[i], right_max[i]) - walls[i])
    
    return total_water