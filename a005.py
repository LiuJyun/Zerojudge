#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:17 2020

@author: AnnieChen
"""

while True:
    try:
        n = int(input())

        for i in range(n):
            a, b, c, d = map(int, input().split())
            if b - a == c - b:
                print(a, b, c, d, d + b - a)
            elif b // a == c // b:
                print(a, b, c, d, d * b // a)

    except:
        break