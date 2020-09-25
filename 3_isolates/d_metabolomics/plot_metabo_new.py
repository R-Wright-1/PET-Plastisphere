#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:36:44 2020

@author: robynwright
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rcParams

plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

cmap_up = 'winter'
norm_up = mpl.colors.Normalize(vmin=-18, vmax=10)
colormap_up = mpl.cm.get_cmap(cmap_up, 256)
m_up = mpl.cm.ScalarMappable(norm=norm_up, cmap=colormap_up)

cmap_down = 'winter'
norm_down = mpl.colors.Normalize(vmin=-10, vmax=18)
colormap_down = mpl.cm.get_cmap(cmap_down, 256)
m_down = mpl.cm.ScalarMappable(norm=norm_down, cmap=colormap_down)

bhet = [['-1.36', '1.13', r'$\bf{-2.29}$', 'ND'],
        [r'$\bf{21.95}$', r'$\bf{1.6}$', '1.88', 'ND']]
bhet_num = [[-1.36, 1.13, -2.29, 1],
            [21.95, 1.6, 1.88, 1]]

plt.figure(figsize=(3,1.5))
plt.subplot2grid((3,1), (0,0), rowspan=2)

bottom = [0,0,0,0]
x = [1,2,3,4]
for a in range(2):
    colors = []
    for b in range(len(bhet_num[a])):
        if bhet_num[a][b] < 0:
            colors.append(m_down.to_rgba(bhet_num[a][b]))
        else:
            colors.append(m_up.to_rgba(bhet_num[a][b]))
        fc = 'k'
        if bhet_num[a][b] < 1: fc = 'w'
        plt.text(x[b], bottom[0]+0.5, bhet[a][b], color=fc, ha='center', va='center')
    plt.bar(x, [1,1,1,1], bottom=bottom, width=1, color=colors, edgecolor='k')
    bottom = [a+1 for a in bottom]

plt.yticks([0.5, 1.5], ['BHET', 'PET']), plt.xticks([1, 2, 3, 4], ['Thio', 'Baci', 'Ideo', 'Comm'])
plt.xlim([0.5,4.5]), plt.ylim([0,2])
plt.savefig('BHET.png', dpi=600)
plt.close()

bhet = [['ND', 'ND', 'ND', 'ND'],
        ['-1.36', '1.13', r'$\bf{-2.29}$', 'ND'],
        [r'$\bf{21.95}$', r'$\bf{1.6}$', '1.88', 'ND']]
bhet_num = [[1,1,1,1],
            [-1.36, 1.13, -2.29, 1],
            [21.95, 1.6, 1.88, 1]]

plt.figure(figsize=(3,1.5))
plt.subplot2grid((3,1), (0,0), rowspan=2)

bottom = [0,0,0,0]
x = [1,2,3,4]
sub = ['TPA', 'BHET', 'PET']
for a in range(3):
    colors = []
    for b in range(len(bhet_num[a])):
        if bhet_num[a][b] < 0:
            colors.append(m_down.to_rgba(bhet_num[a][b]))
        elif bhet_num[a][b] == 1:
            colors.append('w')
        else:
            colors.append(m_up.to_rgba(bhet_num[a][b]))
        fc = 'k'
        if bhet_num[a][b] < 1: fc = 'w'
        plt.text(x[b], bottom[0]+0.5, bhet[a][b], color=fc, ha='center', va='center')
    plt.bar(x, [1,1,1,1], bottom=bottom, width=1, color=colors, edgecolor='k')
    bottom = [a+1 for a in bottom]
    plt.text(0.4, bottom[0]-0.5, sub[a], ha='right', va='center', fontsize=14)
    
bac = ['Thio', 'Baci', 'Ideo', 'Comm']
for b in range(len(x)):
    plt.text(x[b], 3.1, bac[b], ha='center', fontsize=14)
plt.yticks([]), plt.xticks([])
plt.xlim([0.5,4.5]), plt.ylim([0,3])
plt.savefig('BHET.png', dpi=600, bbox_inches='tight')
plt.close()

mhet = [['ND', 'ND', 'ND', 'ND'],
        [r'$\bf{1.98}$', r'$\bf{1.17}$', r'$\bf{7.26}$', r'$\bf{48.16}$'],
        ['ND', 'ND', 'ND', 'ND']]
mhet_num = [[1,1,1,1],
            [1.98, 1.17, 7.26, 48.16],
            [1,1,1,1]]

plt.figure(figsize=(3,1.5))
plt.subplot2grid((3,1), (0,0), rowspan=2)

bottom = [0,0,0,0]
for a in range(3):
    colors = []
    for b in range(len(mhet_num[a])):
        if mhet_num[a][b] < 0:
            colors.append(m_down.to_rgba(mhet_num[a][b]))
        elif mhet_num[a][b] == 1:
            colors.append('w')
        else:
            colors.append(m_up.to_rgba(mhet_num[a][b]))
        fc = 'k'
        if mhet_num[a][b] < 1: fc = 'w'
        plt.text(x[b], bottom[0]+0.5, mhet[a][b], color=fc, ha='center', va='center')
    plt.bar(x, [1,1,1,1], bottom=bottom, width=1, color=colors, edgecolor='k')
    bottom = [a+1 for a in bottom]
    plt.text(0.4, bottom[0]-0.5, sub[a], ha='right', va='center', fontsize=14)
    
for b in range(len(x)):
    plt.text(x[b], 3.1, bac[b], ha='center', fontsize=14)
plt.yticks([]), plt.xticks([])
plt.xlim([0.5,4.5]), plt.ylim([0,3])
plt.savefig('MHET.png', dpi=600, bbox_inches='tight')
plt.close()

c2_O7 = [['ND', 'ND', 'ND', 'ND'],
        [r'$\bf{31.38}$', '1.21', r'$\bf{14.32}$', 'ND'],
        ['ND', 'ND', 'ND', 'ND']]
c2_O7_num = [[1,1,1,1],
            [31.38, 1.21, 14.32, 1],
            [1,1,1,1]]

plt.figure(figsize=(3,1.5))
plt.subplot2grid((3,1), (0,0), rowspan=2)

bottom = [0,0,0,0]
for a in range(3):
    colors = []
    for b in range(len(c2_O7_num[a])):
        if c2_O7_num[a][b] < 0:
            colors.append(m_down.to_rgba(c2_O7_num[a][b]))
        elif c2_O7_num[a][b] == 1:
            colors.append('w')
        else:
            colors.append(m_up.to_rgba(c2_O7_num[a][b]))
        fc = 'k'
        if c2_O7_num[a][b] < 1: fc = 'w'
        plt.text(x[b], bottom[0]+0.5, c2_O7[a][b], color=fc, ha='center', va='center')
    plt.bar(x, [1,1,1,1], bottom=bottom, width=1, color=colors, edgecolor='k')
    bottom = [a+1 for a in bottom]
    plt.text(0.4, bottom[0]-0.5, sub[a], ha='right', va='center', fontsize=14)
    
for b in range(len(x)):
    plt.text(x[b], 3.1, bac[b], ha='center', fontsize=14)
plt.yticks([]), plt.xticks([])
plt.xlim([0.5,4.5]), plt.ylim([0,3])
plt.savefig('c2_O7.png', dpi=600, bbox_inches='tight')
plt.close()

c3_O6 = [['ND', 'ND', 'ND', 'ND'],
        [r'$\bf{8.44}$', '-1.19', r'$\bf{11.73}$', r'$\bf{135.3}$'],
        ['ND', 'ND', 'ND', 'ND']]
c3_O6_num = [[1,1,1,1],
            [8.44, -1.19, 11.73, 135.3],
            [1,1,1,1]]

plt.figure(figsize=(3,1.5))
plt.subplot2grid((3,1), (0,0), rowspan=2)

bottom = [0,0,0,0]
for a in range(3):
    colors = []
    for b in range(len(c3_O6_num[a])):
        if c3_O6_num[a][b] < 0:
            colors.append(m_down.to_rgba(c3_O6_num[a][b]))
        elif c3_O6_num[a][b] == 1:
            colors.append('w')
        else:
            colors.append(m_up.to_rgba(c3_O6_num[a][b]))
        fc = 'k'
        if c3_O6_num[a][b] < 1: fc = 'w'
        plt.text(x[b], bottom[0]+0.5, c3_O6[a][b], color=fc, ha='center', va='center')
    plt.bar(x, [1,1,1,1], bottom=bottom, width=1, color=colors, edgecolor='k')
    bottom = [a+1 for a in bottom]
    plt.text(0.4, bottom[0]-0.5, sub[a], ha='right', va='center', fontsize=14)
    
for b in range(len(x)):
    plt.text(x[b], 3.1, bac[b], ha='center', fontsize=14)
plt.yticks([]), plt.xticks([])
plt.xlim([0.5,4.5]), plt.ylim([0,3])
plt.savefig('c3_O6.png', dpi=600, bbox_inches='tight')
plt.close()

tpa = [[r'$\bf{1.28}$','1.03','-1.15','ND'],
            ['-1.1', r'$\bf{26.53}$', r'$\bf{576.4}$', 'ND'],
            ['-1.04', '1.03', '-1.06', 'ND']]
tpa_num = [[1.28,1.03,-1.15,1],
            [-1.1, 26.53, 576.4, 1],
            [-1.04, 1.03, -1.06, 1]]

plt.figure(figsize=(3,1.5))
plt.subplot2grid((3,1), (0,0), rowspan=2)

bottom = [0,0,0,0]
for a in range(3):
    colors = []
    for b in range(len(tpa_num[a])):
        if tpa_num[a][b] < 0:
            colors.append(m_down.to_rgba(tpa_num[a][b]))
        elif tpa_num[a][b] == 1:
            colors.append('w')
        else:
            colors.append(m_up.to_rgba(tpa_num[a][b]))
        fc = 'k'
        if tpa_num[a][b] < 1: fc = 'w'
        plt.text(x[b], bottom[0]+0.5, tpa[a][b], color=fc, ha='center', va='center')
    plt.bar(x, [1,1,1,1], bottom=bottom, width=1, color=colors, edgecolor='k')
    bottom = [a+1 for a in bottom]
    plt.text(0.4, bottom[0]-0.5, sub[a], ha='right', va='center', fontsize=14)
    
for b in range(len(x)):
    plt.text(x[b], 3.1, bac[b], ha='center', fontsize=14)
plt.yticks([]), plt.xticks([])
plt.xlim([0.5,4.5]), plt.ylim([0,3])
plt.savefig('TPA.png', dpi=600, bbox_inches='tight')
#plt.close()

