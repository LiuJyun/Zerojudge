#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:06 2020

@author: AnnieChen
"""

while True:
    try:
        M, D = map(int, input().split())
        S = (M * 2 + D) % 3

        if S == 0:
            print("普通")
        elif S == 1:
            print("吉")
        else:
            print("大吉")

    except:
        break