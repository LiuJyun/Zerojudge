#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:26 2020

@author: AnnieChen
"""

while True:
    try:
        d = {}
        n = int(input())
        for i in range(2, n + 1):
            while n % i == 0:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1

                n /= i

        for k, v in d.items():
            if v != 1:
                print(k, "^", v, sep="", end="")
            else:
                print(k, sep="", end="")

            if k != list(d.keys())[-1]:
                print(" * ", end="")
        print()
    except:
        break