#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 18:02:34 2024

@author: brettnakao
"""

import numpy as np

print("initial velocity:")
vo=float(input())

print("launch angle in degrees:")
theta=float(input())*np.pi/180

g = 9.81

time_intervals = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for i in range(len(time_intervals)):
    print(i)
    x = vo*float(np.cos(theta))*i
    y = vo*float(np.sin(theta))*i - .5*g*i**2
    print(f"At time {i} s, the horizontal position is {x} m and vertical position is {y} m")
    