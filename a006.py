#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:32 2020

@author: AnnieChen
"""

import math

while True:
    try:
        a, b, c = map(int, input().split())
        D = b ** 2 - 4 * a * c

        if D < 0:
            print("No real root")
        elif D == 0:
            print("Two same roots x=", int((-b - math.sqrt(D)) / (2*a)), sep="")
        else:
            ans = sorted([int((-b + math.sqrt(D)) / (2*a)), int((-b - math.sqrt(D)) // (2*a))], reverse = True)
            print("Two different roots x1=", ans[0], " , x2=", ans[1], sep="")

    except:
        break