#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findFirstOccurrence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def findFirstOccurrence(nums, target):
    l = 0
    h = len(nums) - 1

    while l <= h:
        mid = (l + h) // 2
        if nums[mid] == target:
            flag = mid
            return mid
        elif nums[mid] > target:
            h = mid - 1
        else:
            l = mid + 1
    return -1


if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = findFirstOccurrence(nums, target)

    print(result)
