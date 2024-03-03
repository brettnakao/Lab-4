#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 18:25:24 2024

@author: brettnakao
"""

import numpy as np

resistor_series = np.array([3, 4, 6])
resistors_parallel = np.array([9, 5, 3])

for i in range(len(resistor_series)):
    resistance_values = resistor_series[i]
    print(resistance_values)

for i in range(len(resistors_parallel)):
        resistance_values = resistors_parallel[i]
        inverse_series = np.array(1/(resistance_values))
        print(resistance_values)

print(f"total resistance series: {resistor_series.sum()} ohms")
print(f"total resistance parallel: {np.sum(1/resistors_parallel)} ohms")