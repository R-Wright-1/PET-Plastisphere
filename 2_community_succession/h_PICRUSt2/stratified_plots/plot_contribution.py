#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:26:39 2020

@author: robynwright
"""
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from matplotlib.patches import Patch
import math
import numpy as np

taxonomy = pd.read_csv('/Users/robynwright/Documents/OneDrive/Github/PET-Plastisphere/2_community_succession/e_nmds_PRC_heatmap/Taxonomy.csv', header=0, index_col=0)
asvs = list(taxonomy.index.values)
labels = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']
tax_dict = {}

for asv in asvs:
  this_asv = taxonomy.loc[asv, :].values
  new = ''
  for b in range(len(this_asv)):
    if not isinstance(this_asv[b], str):
      new = this_asv[b-1]
    elif b == 6 and isinstance(this_asv[b], str):
      new = this_asv[b-1]+' '+this_asv[b]
    if new != '':
      this_asv[b] = new
  tax_dict[asv] = this_asv
  
def get_cols(num):
    colormap_20, colormap_40b, colormap_40c = mpl.cm.get_cmap('tab20', 256), mpl.cm.get_cmap('tab20b', 256), mpl.cm.get_cmap('tab20c', 256)
    norm, norm2 = mpl.colors.Normalize(vmin=0, vmax=19), mpl.colors.Normalize(vmin=20, vmax=39)
    m1, m2, m3 = mpl.cm.ScalarMappable(norm=norm, cmap=colormap_20), mpl.cm.ScalarMappable(norm=norm, cmap=colormap_40b), mpl.cm.ScalarMappable(norm=norm2, cmap=colormap_40c)
    colors_20 = [m1.to_rgba(a) for a in range(20)]
    colors_40 = [m2.to_rgba(a) for a in range(20)]+[m3.to_rgba(a) for a in range(20,40)]
    if num < 21: return colors_20
    elif num < 41: return colors_40
    else: return colors_40+colors_40+colors_40

taxa = []
#key_functions = ['PETase', 'tphA2', 'tphA3', 'tphB', 'K18074', 'K18075', 'K18076', 'K00448', 'K00449']
key_functions = ['PETase', 'K18074', 'K18075', 'K18076', 'K00448', 'K00449', 'monooxygenases', 'dioxygenases']
key_functions = ['monooxygenases', 'dioxygenases']
sample_order = ['Day00Inoc', 'Day01NoC', 'Day03NoC', 'Day07NoC', 'Day14NoC', 'Day21NoC', 'Day30NoC', 'Day42NoC', 'Day01LowCrysWater', 'Day03LowCrysWater', 'Day07LowCrysWater', 'Day14LowCrysWater', 'Day21LowCrysWater', 'Day30LowCrysWater', 'Day42LowCrysWater', 'Day01LowCrys', 'Day03LowCrys', 'Day07LowCrys', 'Day14LowCrys', 'Day21LowCrys', 'Day30LowCrys', 'Day42LowCrys', 'Day01PET', 'Day03PET', 'Day07PET', 'Day14PET', 'Day21PET', 'Day30PET', 'Day42PET', 'Day01WeatherPET', 'Day03WeatherPET', 'Day07WeatherPET', 'Day14WeatherPET', 'Day21WeatherPET', 'Day30WeatherPET', 'Day42WeatherPET', 'Day01BHET', 'Day03BHET', 'Day07BHET', 'Day14BHET', 'Day21BHET', 'Day30BHET', 'Day42BHET']
x = [0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48]
all_functions = []
count = 0

for func in key_functions:
    #if func != 'PETase' and func != 'tphA2':
    #    continue
    if func == 'monooxygenases' or func == 'dioxygenases':
        this_func = pd.read_csv('/Users/robynwright/Documents/OneDrive/Github/PET-Plastisphere/2_community_succession/h_PICRUSt2/picrust_out/ko_all_metagenome_out/'+func+'.csv', header=0, index_col=0)
    else:
        this_func = pd.read_csv('/Users/robynwright/Documents/OneDrive/Github/PET-Plastisphere/2_community_succession/h_PICRUSt2/picrust_out/ko_all_metagenome_out/'+func+'.csv', header=0, index_col=1)
        this_func.drop(['Unnamed: 0', 'function', 'taxon_abun', 'taxon_rel_abun', 'genome_function_count', 'taxon_rel_function_abun'], axis=1, inplace=True)
    rename = {}
    for sample in sample_order:
        for sam in list(this_func.index.values):
            if sample == sam[:-1]:
                rename[sam] = sample
    rename['Inoc1']  = 'Day00Inoc'
    rename['Inoc2']  = 'Day00Inoc'
    rename['Inoc3']  = 'Day00Inoc'
    rename['Inoc4']  = 'Day00Inoc'
    this_func.rename(index=rename, inplace=True)
    taxa = list(set(this_func.loc[:, 'taxon']))
    taxa_all = []
    for tax in taxa:
        this_tax = []
        for sample in sample_order:
            this_sample = []
            try:
                this_day = this_func.loc[sample, :]
                this_day = this_day.loc[this_day['taxon'] == tax].values
                for a in range(len(this_day)):
                    this_sample.append(this_day[a][1])
            except:
                do_nothing = True
            if len(this_sample) > 0:
                this_tax.append(np.mean(this_sample))
            else:
                this_tax.append(0)
        taxa_all.append(this_tax)
    this_function = pd.DataFrame(taxa_all, index=taxa, columns=sample_order)
    this_function = this_function.groupby(by=this_function.index, axis=0).sum()
    max_tax = list(this_function.max(axis=1))
    all_functions.append(this_function)
    if count == 0:
        max_taxa = pd.DataFrame([max_tax], columns=list(this_function.index.values))
        max_taxa = max_taxa.transpose()
        max_taxa.rename(columns={0:func}, inplace=True)
        count += 1
    else:
        this_func_new = pd.DataFrame([max_tax], columns=list(this_function.index.values))
        this_func_new = this_func_new.transpose()
        this_func_new.rename(columns={0:func}, inplace=True)
        max_taxa = pd.concat([max_taxa, this_func_new])
max_taxa = max_taxa.fillna(value=0)
max_taxa = max_taxa.groupby(by=max_taxa.index, axis=0).sum()
min_taxa = max_taxa[max_taxa.max(axis=1) < 1]
other = min_taxa.sum(axis=0)
max_taxa = max_taxa[max_taxa.max(axis=1) > 1]
colors = get_cols(max_taxa.shape[0])

color_dict = {}
rename = {}
count = 0
for asv in list(max_taxa.index.values):
    rename[asv] = asv+': '+tax_dict[asv][-1]
    color_dict[asv] = colors[count]
    count += 1
color_dict['Other'] = colors[count]

"""
plt.figure(figsize=(8,14))
ax1 = plt.subplot(611)
ax2 = plt.subplot(612)
ax3 = plt.subplot(613)
ax4 = plt.subplot(614)
ax5 = plt.subplot(615)
ax6 = plt.subplot(616)
axes = [ax1, ax2, ax3, ax4, ax5, ax6]
x = [0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48]

for a in range(6):
    function = all_functions[a]
    ax = axes[a]
    keeping, other = [], []
    for b in list(function.index.values):
        if b in list(max_taxa.index.values):
            keeping.append(True)
            other.append(False)
        else:
            keeping.append(False)
            other.append(True)
    other = pd.DataFrame(function.loc[other, :])
    function = pd.DataFrame(function.loc[keeping, :])
    other = other.sum(axis=0)
    bottom = [0 for a in list(function.columns)]
    for b in list(function.index.values):
        ax.bar(x, function.loc[b, :].values, bottom=bottom, color=color_dict[b], edgecolor='k')
        bottom = [bottom[c]+function.loc[b, :].values[c] for c in range(len(bottom))]
    ax.bar(x, other.values, bottom=bottom, color=color_dict['Other'], edgecolor='k')
    ax.set_ylabel(key_functions[a]+'\n\nRelative\nabundance (%)', fontsize=8)
    plt.sca(ax)
    blank = ['' for y in x]
    if ax != ax6:
        plt.xticks(x, blank)
    plt.xlim([-1, 49])
handles = []
for asv in rename:
    handles.append(Patch(facecolor=color_dict[asv], edgecolor='k', label=rename[asv]))
handles.append(Patch(facecolor=color_dict['Other'], edgecolor='k', label='Other'))

labels = [1, 3, 7, 14, 21, 30, 42, 1, 3, 7, 14, 21, 30, 42, 1, 3, 7, 14, 21, 30, 42, 1, 3, 7, 14, 21, 30, 42, 1, 3, 7, 14, 21, 30, 42, 1, 3, 7, 14, 21, 30, 42]
labels = [str(a) for a in labels]
trt_labels, x_trt = ['No carbon', '\nplanktonic', '\nbiofilm', 'PET powder', 'Weathered\nPET powder', 'BHET', 'Amorphous PET'], [5, 13, 21, 29, 37, 45, 17]
ymax = ax6.get_ylim()[1]/5
for a in range(len(trt_labels)):
  ax6.text(x_trt[a], -ymax, trt_labels[a], ha='center', va='top', fontsize=8)
plt.sca(ax6)
plt.xticks(x[1:], labels, fontsize=6)
ax6.text(0, -0.5, 'Inoculum', ha='center', va='top', rotation=90, fontsize=8)

ax6.legend(handles=handles, loc='upper left', bbox_to_anchor=(0, -0.4), fontsize=8, ncol=2)

plt.savefig('Stratified PICRUSt2 output.png', dpi=600, bbox_inches='tight')
plt.close()
"""

#key_functions = ['PETase', 'K18074', 'K18075', 'K18076', 'K00448', 'K00449', 'monooxygenases', 'dioxygenases']

plt.figure(figsize=(8,6))
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
axes = [ax1, ax2]

for a in range(2):
    function = all_functions[a]
    ax = axes[a]
    keeping, other = [], []
    for b in list(function.index.values):
        if b in list(max_taxa.index.values):
            keeping.append(True)
            other.append(False)
        else:
            keeping.append(False)
            other.append(True)
    other = pd.DataFrame(function.loc[other, :])
    function = pd.DataFrame(function.loc[keeping, :])
    other = other.sum(axis=0)
    bottom = [0 for a in list(function.columns)]
    for b in list(function.index.values):
        ax.bar(x, function.loc[b, :].values, bottom=bottom, color=color_dict[b], edgecolor='k')
        bottom = [bottom[c]+function.loc[b, :].values[c] for c in range(len(bottom))]
    ax.bar(x, other.values, bottom=bottom, color=color_dict['Other'], edgecolor='k')
    ax.set_ylabel(key_functions[a].capitalize()+'\n\nRelative\nabundance (%)', fontsize=8)
    plt.sca(ax)
    blank = ['' for y in x]
    if ax != ax2:
        plt.xticks(x, blank)
    plt.xlim([-1, 49])
handles = []
for asv in rename:
    handles.append(Patch(facecolor=color_dict[asv], edgecolor='k', label=rename[asv]))
handles.append(Patch(facecolor=color_dict['Other'], edgecolor='k', label='Other'))

labels = [1, 3, 7, 14, 21, 30, 42, 1, 3, 7, 14, 21, 30, 42, 1, 3, 7, 14, 21, 30, 42, 1, 3, 7, 14, 21, 30, 42, 1, 3, 7, 14, 21, 30, 42, 1, 3, 7, 14, 21, 30, 42]
labels = [str(a) for a in labels]
trt_labels, x_trt = ['No carbon', '\nplanktonic', '\nbiofilm', 'PET powder', 'Weathered\nPET powder', 'BHET', 'Amorphous PET'], [5, 13, 21, 29, 37, 45, 17]
ymax = ax2.get_ylim()[1]/5
for a in range(len(trt_labels)):
  ax2.text(x_trt[a], -ymax, trt_labels[a], ha='center', va='top', fontsize=8)
plt.sca(ax2)
plt.xticks(x[1:], labels, fontsize=6)
ax2.text(0, -0.5, 'Inoculum', ha='center', va='top', rotation=90, fontsize=8)

ax2.legend(handles=handles, loc='upper left', bbox_to_anchor=(0, -0.4), fontsize=8, ncol=2)

plt.savefig('Stratified PICRUSt2 output oxygenases.png', dpi=600, bbox_inches='tight')

    
    

  
