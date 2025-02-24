#!/usr/bin/python3
"""
Module for calculating the minimum number of operations to reach n H characters.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations (Copy All and Paste) needed to result in exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed. Returns 0 if n is impossible to achieve (n <= 1).
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations