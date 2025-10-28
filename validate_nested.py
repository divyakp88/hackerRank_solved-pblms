#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'areBracketsProperlyMatched' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code_snippet as parameter.
#

def areBracketsProperlyMatched(code_snippet):
    stack=[]
    bracket={'{':'}','[':']','(':')'}
    for ch in code_snippet:
        if ch in bracket.keys():
            stack.append(ch)
        elif ch in bracket.values():
            if not stack or bracket[stack[-1]]!=ch:
                return False
            stack.pop()
    if not stack:
        return True
    else:
        return False

if __name__ == '__main__':
    code_snippet = input()

    result = areBracketsProperlyMatched(code_snippet)

    print(int(result))
