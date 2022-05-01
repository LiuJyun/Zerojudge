#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 10:10 2022

@author: AnnieChen
"""

a, b = map(int, input().split())
if b + 30 >= 60:
    a += 3
    b = b + 30 - 60
else:
    a += 2
    b += 30

if a >= 24:
    a -= 24

print('{:02d}:{:02d}'.format(a, b))