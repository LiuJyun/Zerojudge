#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 14:26 2020

@author: AnnieChen
"""

while True:
    try:
        dic = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
        m, n = input().split()

        if m == "#":
            break

        a = b = 0
        for i in m:
            a += dic[i]

        for i in n:
            b += dic[i]

        #sum = 1997 MCMXCVII // MMCCXVII
        sum = abs(a - b)
        if sum == 0:
            print("ZERO")
        else:
            str = ""
            while sum != 0:
                for k, v in dic.items():
                    while sum >= v:
                        str += k
                        sum -= v
            print(str)

    except:
        break