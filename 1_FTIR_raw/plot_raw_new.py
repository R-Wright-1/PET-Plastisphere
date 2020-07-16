#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:43:00 2020

@author: robynwright
"""

import matplotlib.pyplot as plt
import numpy
import pandas as pd

raw_data = pd.read_csv('Raw_plastics.csv', index_col=0, header=0)

plt.figure(figsize=(12,12))
ax1 = plt.subplot2grid((4,20), (0,0), rowspan=2, colspan=12)
ax2, ax3, ax4, ax5 = plt.subplot(425), plt.subplot(426), plt.subplot(427), plt.subplot(428)
axis = [ax1, ax2, ax3, ax4, ax5]

ax6 = plt.subplot2grid((4,20), (0,14), rowspan=2, colspan=8)

rename_col, rename_ind = {}, {}
for col in raw_data.columns:
    rename_col[col] = col.split('.')[0]

for ind in raw_data.index.values:
    rename_ind[ind] = int(ind)
raw_data.rename(index=rename_ind, inplace=True)

#normalise all to 2501
diff = list(raw_data.loc[2501, :])
diff = [a*(-1) for a in diff]
raw_data = (raw_data+diff)*(-1)

raw_data.rename(columns=rename_col, inplace=True)
raw_data_mean = raw_data.groupby(by=raw_data.columns, axis=1).mean()

colors = ['m', 'b', 'g']
labels = ['Amorphous PET', 'PET powder', 'Weathered PET powder']
for ax in axis:
    #ax.plot(list(raw_data_mean.index.values), raw_data_mean.loc[:, 'LC'], color=colors[0], label=labels[0])
    ax.plot(list(raw_data_mean.index.values), raw_data_mean.loc[:, 'PET'], color=colors[1], label=labels[1])
    ax.plot(list(raw_data_mean.index.values), raw_data_mean.loc[:, 'WPET'], color=colors[2], label=labels[2])
    plt.sca(ax)
    plt.ylabel('Absorbance (%)')
    plt.xlabel('Wavenumber (cm$^{-1}$)')

ax6.set_ylabel(r'Ratio between reference 1410 cm$^{-1}$'+'/nand wavelength')

wl = [1710, 2920, 1235, 3300, 1090]
wl_name = ['C=O\n1710', 'O-H\n2920', 'C-O\n1235', 'O-H\n3300', 'C-O\n1090']

x = [1, 2]
xplt = []

for a in range(len(wl)):
    xplt.append(x[0]+0.5)
    a = wl[a]
    ref = line = pd.DataFrame(raw_data.loc[1410, :]).transpose()
    line = pd.DataFrame(raw_data.loc[a, :]).transpose()
    line = line.divide(ref.values[0])
    m1, m2, m3 = numpy.mean(line.loc[:, 'LC'].values[0]), numpy.mean(line.loc[:, 'PET'].values[0]), numpy.mean(line.loc[:, 'WPET'].values[0])
    s1, s2, s3 = numpy.std(line.loc[:, 'LC'].values[0]), numpy.std(line.loc[:, 'PET'].values[0]), numpy.std(line.loc[:, 'WPET'].values[0])
    ax6.bar(x, [m2, m3], yerr=[s2, s3], color=colors[1:], edgecolor='k', width=0.8, error_kw=dict(ecolor='k', lw=1, capsize=2, capthick=1))
    x = [b+3 for b in x]
plt.sca(ax6)
plt.xticks(xplt+[4.51, 12], wl_name+['\n\ncarboxylic acid', '\n\nalcohol'])   

ax1.set_title('A', loc='left', fontweight='bold')
ax2.set_title('C', loc='left', fontweight='bold')
ax3.set_title('D', loc='left', fontweight='bold')
ax4.set_title('E', loc='left', fontweight='bold')
ax5.set_title('F', loc='left', fontweight='bold')
ax6.set_title('B', loc='left', fontweight='bold')

plt.sca(ax1)
plt.xlim(4000,500)
plt.xticks([500, 1000, 1500, 2000, 2500, 3000, 3500, 4000])

plt.sca(ax2)
plt.xlim(1000,650)
plt.xticks([700, 800, 900, 1000])

plt.sca(ax3)
plt.xlim([1200,1000])
plt.xticks([1000, 1040, 1080, 1120, 1160, 1200])

plt.sca(ax4)
plt.xlim([1600, 1200])
plt.xticks([1200, 1300, 1400, 1500, 1600])

plt.sca(ax5)
plt.xlim([1800, 1600])
plt.xticks([1600, 1640, 1680, 1720, 1760, 1800])

ax1.legend()
plt.subplots_adjust(hspace=0.5)
plt.savefig('Raw plastics 2.png', dpi=600)