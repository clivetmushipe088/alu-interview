#!/usr/bin/python3
def minOperations(n):

    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1
    
    return operations

# Example usage:
n = 9
print(minOperations(n))  # Output: 6