#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 22:57:48 2019

@author: debashis
"""

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum2 = 15
flag = 0
for i in range(len(arr)):
    if flag == 1:
        break
    desired_sum = 0
    desired_sum += arr[i]
    for j in range(i, len(arr)):
        if desired_sum < sum2:
            desired_sum += arr[j]
            
        if desired_sum == sum2:
            print('Index of Desired Sum: ', i, j)
            flag = 1
            break
