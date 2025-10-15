#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#
import math


def countResponseTimeRegressions(responseTimes):
    # Write your code here
    elements = []

    count = 0
    for i, item in enumerate(responseTimes):
        if len(elements) > 0:
            sum1 = sum(elements)
            aver = sum1 / len(elements)
            if item > aver:
                count = count + 1
        elements.append(item)
    return count


if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
