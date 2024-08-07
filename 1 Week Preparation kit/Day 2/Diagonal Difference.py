#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)  # n is the number of rows (and columns) in the square matrix
    primary_sum = 0
    secondary_sum = 0
    
    # Calculate sums of primary and secondary diagonals
    for i in range(n):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][n-i-1]
    
    # Calculate absolute difference
    difference = abs(primary_sum - secondary_sum)
    
    return difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
