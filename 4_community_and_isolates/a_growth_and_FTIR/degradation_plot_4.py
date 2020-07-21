#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:39:35 2020

@author: robynwright
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from matplotlib.patches import Patch
import pandas as pd
from scipy.integrate import simps
from numpy import trapz


plt.figure(figsize=(10,10))
ax1, ax2, ax3 = plt.subplot(311), plt.subplot(312), plt.subplot(313)

FTIR_ax = [ax1, ax2, ax3]
FTIR_file = ['corrected_spectra_LC.csv', 'corrected_spectra_WPET.csv', 'corrected_spectra_PET.csv']
FTIR_all = ['corrected_spectra_LC_all.csv', 'corrected_spectra_WPET_all.csv', 'corrected_spectra_PET_all.csv']
#ref_area, areas = [1410], [[1341], [], [], []]
ref_area, areas = [1390, 1425], [[1325, 1355], [1185, 1355]]
ref_peak_crys, peaks_crys = 1100, [1120]
ref_peak, peaks = 1410, [1711, 1240, 725, 1090, 1017]

colors = ['gray', '#028DE9', '#B03A2E', '#F1C40F']

for a in range(len(FTIR_ax)):
    this_file = pd.read_csv(FTIR_file[a], index_col=0, header=0)
    treats = ['Control', 'Thioclava', 'Bacillus', 'Community']
    for b in range(len(treats)):
        FTIR_ax[a].plot(list(this_file.index.values), this_file.loc[:, treats[b]].values, color=colors[b])
    FTIR_ax[a].set_xlim([2000, 650])
    if a < 2:
        plt.sca(FTIR_ax[a])
        plt.xticks([])

for a in [ref_area]+areas:
    if a != []:
        for b in a:
            for c in FTIR_ax:
                c.plot([b, b], [0, 6], 'gray', linestyle='-.', alpha=0.3)

for a in [ref_peak]+peaks:
    for c in FTIR_ax:
        c.plot([a, a], [0, 6], 'k', linestyle='-.')
        
for a in [ref_peak_crys]+peaks_crys:
    for c in FTIR_ax:
        c.plot([a, a], [0, 6], 'k', linestyle='-.')
        
plt.savefig('Testing', dpi=600)
plt.close()

plt.figure(figsize=(10,10))
ax1 = plt.subplot(311)
ax2, ax3 = plt.subplot(312, sharex=ax1, sharey=ax1), plt.subplot(313, sharex=ax1, sharey=ax1)
FTIR_ax = [ax1, ax2, ax3]

#areas:    A1341/1410 = degree of crystallinity

#peaks:    I1120/1100 = degree of crystallinity
groups = ['Control', 'Thioclava', 'Bacillus', 'Community']
for a in range(len(FTIR_all)):
    x = [1, 2, 3, 4]
    #if a > 0: continue
    area_ratios, peak_ratios = [], []
    for b in range(len(areas)):
        area_ratios.append([[], [], [], []])
    for c in range(len(peaks)):
        peak_ratios.append([[], [], [], []])
    data = pd.read_csv(FTIR_all[a], header=0, index_col=0)
    for sample in data.columns:
        ref_values = data.loc[1390:1425, sample].values
        ref_area = trapz(ref_values, dx=1)
        for b in range(len(areas)):
            if areas[b] == []: continue
            value = data.loc[areas[b][0]:areas[b][1], sample].values
            area = trapz(value, dx=1)
            for c in range(len(groups)):
                if groups[c] in sample:
                    area_ratios[b][c].append(area/ref_area)
    for b in range(len(area_ratios)):
        this_mean, this_std = [], []
        for c in range(len(area_ratios[b])):
            this_mean.append(np.mean(area_ratios[b][c]))
            this_std.append(np.std(area_ratios[b][c]))
        FTIR_ax[a].bar(x, this_mean, yerr=this_std, color=colors, edgecolor='k')
        x = [d+5 for d in x]

plt.savefig('Testing ratios', dpi=600)