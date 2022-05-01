#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:39 2020

@author: AnnieChen
"""

while True:
    try:
        s = input()
        for i in s:
            print(chr(ord(i) - 7), end="")
        print()

    except:
        break