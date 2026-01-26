#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice = bob = 0
    
    for x, y in zip(a, b):
        if x>y:
            alice += 1
        elif x<y:
            bob += 1
    return [alice, bob]

# Below code is HackerRank boilerplate code. 
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     a = list(map(int, input().rstrip().split()))

#     b = list(map(int, input().rstrip().split()))

#     result = compareTriplets(a, b)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()

# Modified to allow direct execution and testing locally
if __name__ == "__main__":
    a = list(map(int, input("a = ").split()))
    b = list(map(int, input("b = ").split()))

    result = compareTriplets(a, b)

    if 'OUTPUT_PATH' in os.environ:
        with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
            fptr.write(' '.join(map(str, result)) + '\n')
            fptr.close()
    else:
        print(*result)
