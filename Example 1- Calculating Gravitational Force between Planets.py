#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 18:33:00 2024

@author: brettnakao
"""

import numpy as np

# Constant
G = 6.674e-11 # Gravitational constant (N m^2/kg^2)

# Arrays for masses (kg) and distances (m)
masses = np.array([1.0241e26, 8.6810e25, 5.6834e26, 1.8982e27, 6.4171e23, 5.972e24, 4.8675e24, 3.3011e3])
distance = np.array([4.5e12, 2.9e12, 1.4e12, 7.78e11, 2.28e11, 1.496e11, 1.08e11, 5.79e10])

# Calculate gravitational forces
for i in range(len(masses)):
    m1 = masses[i]
    d1 = distance[i]
    
    for j in range(i + 1, len(masses)):
        m2 = masses[j]
        d2 = distance[j]
        d = (d1-d2)
        F = G*(m1*m2)/d**2
        print(f"For planets with mass {m1} kg & {m2} kg and {d} m apart, the gravitational force is {F} N")