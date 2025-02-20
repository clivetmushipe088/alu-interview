#!/usr/bin/python3
def minOperations(n):
    if n < 2:
        return 0  # Impossible case, as we start with one 'H'
    
    operations = 0
    factor = 2  # Start with the smallest prime factor

    while n > 1:
        while n % factor == 0:  # If factor divides n
            operations += factor  # Add the factor to operations
            n //= factor  # Reduce n by the factor
        factor += 1  # Move to the next factor

    return operations