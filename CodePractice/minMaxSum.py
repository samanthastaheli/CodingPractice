#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# def miniMaxSum(arr):
#     # Write your code here
#     min_num = 100
#     max_num = 0
#     total = 0
#     for x in range(len(arr)):
#         # total = 0
#         x_num = arr[x]
#         # total += arr[x]
#         if x + 4 > len(arr):
#             pass
#         else:
#             for y in range(x, x+4):
#                 y_num = arr[y]
#                 total += arr[y]
#         if total > max_num:
#             max_num = total
#         if total < min_num:
#             min_num = total
    
#     print(min_num, '  ', max_num)

# if __name__ == '__main__':

#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)

def miniMaxSum(arr):
    totals = []
    for x in range(len(arr)):
        total = 0
        x_num = arr[x]
        # total += arr[x]
        if x + 4 > len(arr):
            pass
        else:
            for y in range(x, x+4):
                y_num = arr[y]
                total += arr[y]
        if total != 0:
            totals.append(total)

    min_num = min(totals)
    max_num = max(totals)
    
    print(min_num, max_num)

arr = [1, 3, 5, 7, 9]
arr2 = [7, 69, 2, 221, 8974]
miniMaxSum(arr)
miniMaxSum(arr2)