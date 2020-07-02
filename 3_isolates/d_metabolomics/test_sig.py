#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 09:01:17 2020

@author: robynwright
"""

import math
import numpy as np
from scipy import stats

#PET
#norm_area_bhet = [[1488759.467, 839261.037, 141343.0197], [59275.59505, 70938.10471, 69989.05551], [27280.17244, 35339.24841, 115917.3008], [29094.98099, 22460.78702]]
#norm_area_tpa = [[1077228.134, 813530.2657, 1350083.758], [1011212.544, 972312.4497, 1490661.537], [1042485.544, 968379.2374, 1121805.788], [1065390.885, 1139700.97]]

#TPA
#norm_area_bhet = []
#norm_area_tpa = [[8366315.043, 7870858.994, 7364000.28], [6026262.355, 6208245.348, 6631961.456], [4933738.754, 5426020.314, 5621770.779],[ 6263237.016, 5970676.107]]

#BHET
norm_area_bhet = [[593992257.1, 568832584.9, 222090236.8], [686941127.9, 573680494.1, 703526078.2], [228154123.4, 270079419.7, 256379255.7], [654350065.6, 482151372, 603968893.2]]
norm_area_tpa = [[461587.5747, 445030.8918, 556981.3207], [13585934.2, 14937137.06, 14203941.89], [328881211.5, 298729647.9, 300758515.1], [448577.4626, 657695.6725, 523012.6161]]
norm_area_mhet = [[394428642, 379131762.5, 404917566.1], [218492519.8, 240447053.5, 238703023.5], [1516207205, 1404362533, 1402281499], [192598113.2, 196255264.8, 206295352.2]]
norm_area_c3 = [[673315.1929, 742966.9095, 753956.4968], [62735.5973, 78307.33013, 76686.34321], [1014510.647, 1008141.091, 990836.2746], [133066.8635, 68479.39393, 68875.70453]]
norm_area_c2 = [[344253.4732, 467307.7215, 469953.8998], [17901.00491, 16232.92947, 14786.01152], [191952.7407, 197020.7992, 190097.1256], [14355.76325, 10129.22035, 16819.73336]]

for a in range(len(norm_area_bhet)):
    for b in range(len(norm_area_bhet[a])):
        norm_area_bhet[a][b] = math.log2(norm_area_bhet[a][b])
        norm_area_tpa[a][b] = math.log2(norm_area_tpa[a][b])
        norm_area_mhet[a][b] = math.log2(norm_area_mhet[a][b])
        norm_area_c3[a][b] = math.log2(norm_area_c3[a][b])
        norm_area_c2[a][b] = math.log2(norm_area_c2[a][b])

for a in range(3):
    """
    ttest, p = stats.ttest_ind(norm_area_bhet[a], norm_area_bhet[-1])
    print('BHET')
    print(ttest, p)
    print(np.mean(norm_area_bhet[a])-np.mean(norm_area_bhet[-1]))
    ttest, p = stats.ttest_ind(norm_area_tpa[a], norm_area_tpa[-1])
    print('TPA')
    print(ttest, p)
    print(np.mean(norm_area_tpa[a])-np.mean(norm_area_tpa[-1]))
    """
    ttest, p = stats.ttest_ind(norm_area_mhet[a], norm_area_mhet[-1])
    print('MHET')
    print(ttest, p)
    print(np.mean(norm_area_mhet[a])-np.mean(norm_area_mhet[-1]))
    ttest, p = stats.ttest_ind(norm_area_c3[a], norm_area_c3[-1])
    print('c3')
    print(ttest, p)
    print(np.mean(norm_area_c3[a])-np.mean(norm_area_c3[-1]))
    ttest, p = stats.ttest_ind(norm_area_c2[a], norm_area_c2[-1])
    print('c2')
    print(ttest, p)
    print(np.mean(norm_area_c2[a])-np.mean(norm_area_c2[-1]))
    