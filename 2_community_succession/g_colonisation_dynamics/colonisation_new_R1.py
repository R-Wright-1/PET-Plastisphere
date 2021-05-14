#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:22:36 2021

@author: robynwright
"""

import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib
from colorsys import hls_to_rgb
import random
import pandas as pd

def get_distinct_colors(n):
    colors = []
    for i in np.arange(0., 360., 360. / n):
        h = i / 360.
        l = (50 + np.random.rand() * 10) / 100.
        s = (90 + np.random.rand() * 10) / 100.
        colors.append(hls_to_rgb(h, l, s))
    random.shuffle(colors)
    return colors

PRC_ASV_LCPB = ['ASV31', 'ASV11', 'ASV81', 'ASV3', 'ASV6', 'ASV19', 'ASV12']
PRC_ASV_BHET = ['ASV48', 'ASV97', 'ASV49', 'ASV22', 'ASV88', 'ASV92', 'ASV7', 'ASV100', 'ASV14', 'ASV86']
PETase = ['ASV43', 'ASV98', 'ASV20']

plt.figure(figsize=(20,20))
ax1, ax2, ax3, ax4, ax5, ax6 = plt.subplot2grid((1,49), (0,0), colspan=7), plt.subplot2grid((1,49), (0,7), colspan=7), plt.subplot2grid((1,49), (0,14), colspan=7), plt.subplot2grid((1,49), (0,21), colspan=7), plt.subplot2grid((1,49), (0,28), colspan=7), plt.subplot2grid((1,49), (0,35), colspan=7)
ax_ord = plt.subplot2grid((1,49), (0,42))
axes = [ax1, ax2, ax3, ax4, ax5, ax6]

abundance = pd.read_csv('over_time_all.csv', header=0, index_col=0).drop('Day00Inoc', axis=1)
taxonomy = pd.read_csv('Taxonomy.csv', header=0, index_col=0)

treats = ['BHET', 'LowCrys', 'LowCrysWater', 'PET', 'WeatherPET', 'NoC']
abundance = abundance[abundance.max(axis=1) > 0.5]
samples = list(abundance.columns)
days = ['01', '03', '07', '14', '21', '30', '42']
x = [0.5, 2.5, 5.5, 11, 18, 26, 36.5]
xwidth = [2, 2, 4, 7, 7, 9, 12]
xlab = [1, 3, 7, 14, 21, 30, 42]
asv_max = []

treat_abundance = []

for treat in treats:
    treat_samples = []
    for sample in samples:
        if treat in sample:
            treat_samples.append(sample)
    treat_samples = sorted(treat_samples)
    this_treat = pd.DataFrame(abundance.loc[:, treat_samples])
    this_treat[this_treat < 0.5] = 0
    treat_abundance.append(this_treat)

abundance = pd.concat(treat_abundance).fillna(0)
abundance = abundance.groupby(by=abundance.index, axis=0).sum()

for asv in abundance.index.values:
    this_asv = []
    for treat in treat_abundance:
        asv_treat = pd.DataFrame(treat.loc[asv, :]).transpose()
        if max(list(asv_treat.values)[0]) == 0: 
            continue
        day_max = list(asv_treat.idxmax(axis=1))[0]
        day_max = int(day_max[3:5])
        this_asv.append(day_max)
    asv_max.append(np.mean(this_asv))

abundance['Maximum day'] = asv_max
abundance = abundance.sort_values('Maximum day', ascending=False)

taxonomy = taxonomy.loc[abundance.index.values, 'Order']
(all_unique_tax) = sorted(['Caulobacterales', 'Rhodobacterales', 'Xanthomonadales', 'Vibrionales', 'Bacteroidales', 'Alteromonadales', 'Rhodovibrionales', 'Oceanospirillales', 'Cytophagales', 'Rhodospirillales', 'Nitrosococcales', 'Bacillales', 'Rhizobiales', 'Parvibaculales', 'Betaproteobacteriales', 'Chitinophagales', 'Micrococcales', 'Sphingomonadales', 'Pseudomonadales', 'Nitrospirales'])
tax_colors = get_distinct_colors(len(all_unique_tax))
all_unique_tax.append('Other')
tax_colors.append('k')
order_dict = {}
for a in range(len(all_unique_tax)):
    order_dict[all_unique_tax[a]] = tax_colors[a]

rename_asv = {}
asv_color = {}
for asv in abundance.index.values:
    new_asv = 'ASV'+str(int(asv[3:]))
    rename_asv[asv] = new_asv
    asv_ord = taxonomy.loc[asv]
    if asv_ord in order_dict:
        asv_color[new_asv] = [order_dict[asv_ord], asv_ord[0]]
    else:
        asv_color[new_asv] = [order_dict['Other'], 'O']

abundance = abundance.rename(index=rename_asv).drop('Maximum day', axis=1)
abundance_norm = abundance.div(abundance.max(axis=1), axis=0)

norm = mpl.colors.Normalize(vmin=0, vmax=1)
colormap = mpl.cm.get_cmap('plasma', 256)
m = mpl.cm.ScalarMappable(norm=norm, cmap=colormap)

c = 0
ylabs, ylocs = [], []

for asv in abundance.index.values:
    for t in range(len(treats)):
        treat = treats[t]
        keeping = []
        for sample in abundance_norm.columns:
            if sample[5:] == treat:
                keeping.append(sample)
        keeping = sorted(keeping)
        values = list(abundance_norm.loc[asv, keeping].values)
        values = [m.to_rgba(value) for value in values]
        axes[t].bar(x, [1,1,1,1,1,1,1], bottom=[c,c,c,c,c,c,c], width=xwidth, color=values, edgecolor='k')
    ax_ord.bar(0.5, 1, bottom=c, width=1, color=asv_color[asv][0], alpha=0.7, edgecolor='k')
    ax_ord.text(0.5, c+0.5, asv_color[asv][1], ha='center', va='center')
    text = asv
    if asv in PETase:
        ax_ord.text(1.5, c+0.5, text, ha='left', va='center', color='w', bbox=dict(facecolor='k', boxstyle='round'))
    elif asv in PRC_ASV_LCPB:
        ax_ord.text(1.5, c+0.5, text, ha='left', va='center', bbox=dict(facecolor='none', edgecolor='m', boxstyle='round', lw=2))
    elif asv in PRC_ASV_BHET:
        ax_ord.text(1.5, c+0.5, text, ha='left', va='center', bbox=dict(facecolor='none', edgecolor='orange', boxstyle='round', lw=2))
    else:
        ax_ord.text(1.5, c+0.5, text, ha='left', va='center')
    c += 1

titles = ['BHET', 'Amorphous\nPET biofilm', 'Amorphous\nPET planktonic', 'PET powder', 'Weathered\nPET powder', 'No carbon']
colors = ['orange', 'm', 'r', 'b', 'g', 'y']
title1 = ['A', 'B', 'C', 'D', 'E', 'F']
for a in range(len(axes)):
    plt.sca(axes[a])
    plt.xticks([x-0.5 for x in xlab], xlab)
    plt.xlim([-0.5, 42])
    plt.ylim([0, c])
    plt.yticks([])
    plt.title(titles[a], color=colors[a], fontweight='bold')
    plt.title(title1[a], fontweight='bold', loc='left')
    if a == 2:
        plt.text(45, -2, 'Days', ha='center')

plt.sca(ax_ord)
plt.xticks([])
plt.xlim([0,1])
plt.ylim([0,c])
plt.yticks(ylocs, ['' for y in ylocs])
ax_ord.yaxis.tick_right()

ax_leg = plt.subplot2grid((74,49), (4,45), rowspan=21)
d = 20
ylocs = []
for order in order_dict:
    ax_leg.bar(0.5, 1, bottom=d, color=order_dict[order], edgecolor='k', alpha=0.7, width=1)
    ax_leg.text(0.5, d+0.5, order[0], ha='center', va='center')
    ax_leg.text(1.5, d+0.5, order, ha='left', va='center')
    ylocs.append(d)
    d -= 1

plt.sca(ax_leg)
plt.xticks([])
plt.xlim([0,1])
plt.ylim([0,21])
plt.yticks([y+0.5 for y in ylocs], ['' for y in ylocs])
ax_leg.yaxis.tick_right()

axcolbar = plt.subplot2grid((120,49), (0,45), colspan=4, rowspan=2)
plt.sca(axcolbar)
orm = mpl.colors.Normalize(vmin=0, vmax=1)
colormap = mpl.cm.get_cmap('plasma', 256)
matplotlib.colorbar.ColorbarBase(axcolbar, cmap=colormap, norm=norm, orientation='horizontal')
plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)
plt.tick_params(axis='x', which='both', top=False, bottom=False, labelbottom=False)
axcolbar.text(0.1, 0.5, '0', ha='center', va='center', color='w')
axcolbar.text(0.9, 0.5, '1', ha='center', va='center', color='k')
plt.xlabel('Normalised\nrelative\nabundance')

plt.subplots_adjust(wspace=0.8)
plt.savefig('New figure.tiff', bbox_inches='tight', dpi=600)

    