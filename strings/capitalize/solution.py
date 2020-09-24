#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# solution.py

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    print(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
