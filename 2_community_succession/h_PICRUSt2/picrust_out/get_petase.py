#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 17:31:04 2019

@author: robynwright
"""

import csv

with open('ko_all_predicted_highest.csv', 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)

for a in range(1, len(rows)):
    for b in range(1, len(rows[a])):
        rows[a][b] = int(rows[a][b])

print(len(rows))

new_list = []
for a in range(1, len(rows)):
    if rows[a][3] > 0:
        new_list.append([rows[a][0], rows[a][3]])

with open('ko_PETases.csv', 'w') as f:
    writer = csv.writer(f)
    for row in new_list:
        writer.writerow(row)