#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 12:06:38 2021

@author: robynwright
"""

import pandas as pd

distances = pd.read_csv("ASV_distance.csv", header=0, sep=' ')
#with open("ASV_distance.csv") as f:
#    first_line = f.readline()
#print(first_line)

print(distances.columns)