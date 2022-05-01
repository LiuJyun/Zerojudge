#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 23:06 2021

@author: AnnieChen
"""

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    c = ((b-a) / a) * 100

    if c > 0:
        c += 0.00001
    elif c < 0:
        c -= 0.00001

    print('{:.2f}% '.format(c), end='')
    s = 'dispose' if c >= 10.00 or c <= -7.00 else 'keep'
    print(s)