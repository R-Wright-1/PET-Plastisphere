#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 21:03:01 2020

@author: robynwright
"""

import csv
import numpy
import matplotlib.pyplot as plt
import scipy.stats as stats
from matplotlib.patches import Patch
import pandas as pd

plt.figure(figsize=(20,20))

ax1 = plt.subplot2grid((8,7), (2,0), rowspan=2, colspan=2)
ax2 = plt.subplot2grid((8,7), (4,0), rowspan=2, sharey=ax1, colspan=2)
ax3 = plt.subplot2grid((8,7), (6,0), rowspan=2, sharey=ax1, colspan=2)

ax4 = plt.subplot2grid((8,7), (2,5), rowspan=2, colspan=2)
ax5 = plt.subplot2grid((8,7), (4,5), rowspan=2, colspan=2)
ax6 = plt.subplot2grid((8,7), (6,5), rowspan=2, colspan=2)

ax7 = plt.subplot2grid((8,7), (2,2), rowspan=2, colspan=3)
ax8 = plt.subplot2grid((8,7), (4,2), rowspan=2, colspan=3)
ax9 = plt.subplot2grid((8,7), (6,2), rowspan=2, colspan=3)

ax_empty = plt.subplot2grid((48,7), (0,0), colspan=6, frameon=False, rowspan=11)
ax_leg = plt.subplot2grid((48,7), (0,6), frameon=False, rowspan=11)

ax_em1 = plt.subplot2grid((48,7), (11,0), colspan=2, frameon=False)
ax_em2 = plt.subplot2grid((48,7), (11,2), colspan=5, frameon=False)

ax_em1.set_title('Three months incubation', fontsize=16, fontweight='bold')
ax_em2.set_title('Five months incubation', fontsize=16, fontweight='bold')

remove = [ax_empty, ax_em1, ax_em2, ax_leg]

for rem in remove:
    plt.sca(rem)
    plt.xticks([]), plt.yticks([])

colors = ['gray', '#028DE9', '#B03A2E', '#F1C40F']
bac_labels = ['No inoculum', r'$Thioclava$'+'\nsp. BHET1', r'$Bacillus$'+'\nsp. BHET2', 'Community']

ax1.set_ylabel(r'Protein $\mu$g mL$^{-1}$', fontsize=12)
ax2.set_ylabel(r'Protein $\mu$g mL$^{-1}$', fontsize=12)
ax3.set_ylabel(r'Protein $\mu$g mL$^{-1}$', fontsize=12)
ax4.set_ylabel('Ratio', fontsize=12)
ax5.set_ylabel('Ratio', fontsize=12)
ax6.set_ylabel('Ratio', fontsize=12)
ax7.set_ylabel('Normalised absorbance', fontsize=12)
ax8.set_ylabel('Normalised absorbance', fontsize=12)
ax9.set_ylabel('Normalised absorbance', fontsize=12)

files_protein = ['3 month plate 1 protein 1 in 10.csv', '3 month plate 2 protein 1 in 10.csv']

def get_file(f):
    #f = '/Users/robynwright/Documents/OneDrive/PhD_Plastic_Oceans/Experiments/PET/Degradation_test/Growth_measurements/'+f
    with open(f, 'rU') as f:
        rows = []
        for row in csv.reader(f):
            rows.append(row)
    return rows

def get_prot_plate(f):
    rows = get_file(f)
    rows = rows[23:]
    for a in range(len(rows)):
        rows[a] = rows[a][2:-1]
        for b in range(len(rows[a])):
            rows[a][b] = float(rows[a][b])
    samples, scs = [], []
    for c in range(len(rows)):
        samples.append(rows[c][:9])
        scs.append(rows[c][-2:])
    sc = []
    for d in range(6):
        sc.append(numpy.mean(scs[d]))
    return samples, sc
    gradient, intercept, r_value, p_value, std_err = stats.linregress(concs, sc)
    for a in range(len(samples)):
        for b in range(len(samples[a])):
            num = samples[a][b]
            new_num = (num-intercept)/gradient
            samples[a][b] = new_num
    return samples, sc

def get_prot(f1, f2):
    s1, sc1 = get_prot_plate(f1)
    s2, sc2 = get_prot_plate(f2)
    sc = []
    for a in range(len(sc1)):
        sc.append(numpy.mean([sc1[a], sc2[a]]))
    concs = [0, 0.5, 5, 10, 20, 30]
    gradient, intercept, r_value, p_value, std_err = stats.linregress(concs, sc)
    for a in range(len(s1)):
        for b in range(len(s1[a])):
            num = s1[a][b]*10
            new_num = (num-intercept)/gradient
            s1[a][b] = new_num
    for a in range(len(s2)):
        for b in range(len(s2[a])):
            num = s2[a][b]*10
            new_num = (num-intercept)/gradient
            s2[a][b] = new_num
    return s1, s2

td = r'$Thioclava$'+'\nsp. BHET1'
ba = r'$Bacillus$'+'\nsp. BHET2'

def get_files_protein(files):
    p1, p2 = get_prot(files[0], files[1])
    noC = [p1[0], p1[1], p1[2], p1[3]]
    #print('noC =', noC)
    carbon = [[p1[4], p2[0], p2[4]], [p1[5], p2[1], p2[5]], [p1[6], p2[2], p2[6]], [p1[7], p1[3], p2[7]]]
    #print('carbon =', carbon)
    for a in range(len(carbon)):
        for b in range(len(carbon[a])):
            for c in range(len(carbon[a][b])):
                carbon[a][b][c] = carbon[a][b][c]-noC[b][c]
    axes = [ax1, ax2, ax3]
    xplc1 = [1, 2, 3, 4]
    labels = ['No carbon', td, ba, 'Community']
    these_means = [[], [], []]
    these_all_means = [[], [], []]
    for a in range(len(carbon)):
        for b in range(len(carbon[a])):
            means, stds = [], []
            all_means = carbon[a][b][:3]+carbon[a][b][3:6]+carbon[a][b][6:]
            means.append(numpy.mean(carbon[a][b][:3]))
            means.append(numpy.mean(carbon[a][b][3:6]))
            means.append(numpy.mean(carbon[a][b][6:]))
            stds.append(numpy.std(carbon[a][b][:3]))
            stds.append(numpy.std(carbon[a][b][3:6]))
            stds.append(numpy.std(carbon[a][b][6:]))
            these_means[b].append(means)
            these_all_means[b].append(all_means)
            axes[b].bar(xplc1[a], numpy.mean(means), color=colors[a], edgecolor='k', yerr=numpy.std(means), error_kw=dict(ecolor='k', lw=2, capsize=2, capthick=2), label=labels[a])
            if a > 0:
                ttest = stats.ttest_ind(these_all_means[b][0], all_means)
                if ttest[1] <= 0.05:
                    axes[b].text(xplc1[a], numpy.mean(means)+numpy.std(means)+0.1, '*', ha='center', va='bottom', fontsize=12, fontweight='bold')
    plt.sca(ax1)
    #plt.xticks(ticks=[1, 2, 3, 4], labels=['No inoculum', td, ba, 'Community'])
    plt.xticks([1,2,3,4], ['','','',''])
    ax1.set_ylim(bottom=0, top=50)
    plt.sca(ax2)
    #plt.xticks(ticks=[1, 2, 3, 4], labels=['No inoculum', td, ba, 'Community'])
    plt.xticks([1,2,3,4], ['','','',''])
    ax2.set_ylim(bottom=0, top=50)
    plt.sca(ax3)
    plt.xticks(ticks=[1, 2, 3, 4], labels=['No inoculum', td, ba, 'Community'], fontsize=10)
    ax3.set_ylim(bottom=0, top=50)
    return

handles = [Patch(facecolor=colors[a], edgecolor='k', label=bac_labels[a]) for a in range(len(colors))]
get_files_protein(files_protein)

LC = [[[2.880836090008632, 2.8759996538141106, 3.608023091170047, 2.8725618658153937], [3.1073551669771122, 3.3725272841211305, 4.424672648172658, 3.237487234480522], [3.346628580639322, 4.042532589383279, 4.891648753943692, 3.779796238352676], [3.03499928308463, 3.380769742153617, 4.252187135373816, 3.2414788125860086]], [[0.1756243604420209, 0.13342851604426903, 0.3135618477830579, 0.1700844196763988], [0.26505061509568273, 0.2343180088526368, 0.19060774208309508, 0.2325885491481703], [0.45317229796707426, 0.5183163590758544, 0.4461728250664926, 0.49094613761422573], [0.29078079587500005, 0.2778806373934385, 0.22185590808476927, 0.273573825937945]], [['', '', '*', ''], ['', '*', '*', ''], ['', '*', '*', ''], ['', '*', '*', '']]]
PET2 = [[[2.8193923968768693, 2.8188141837319445, 2.7464525662959636, 2.8876878563509942], [2.841995301435963, 2.87848455643512, 2.718848789677376, 2.8738434685279177], [2.782569378785949, 2.8712851253522786, 2.604481230853662, 2.777638023929795], [2.7197000713090835, 2.7626460701460456, 2.5978801208359865, 2.7411501817674644]], [[0.049278586515484515, 0.12099836152462225, 0.18309595480959678, 0.0801346121888017], [0.06723145643760439, 0.07970122030824578, 0.15003967041918212, 0.0725721546178073], [0.13679518256650414, 0.12567648570790452, 0.14785499429838356, 0.0745796441610995], [0.0759765038569029, 0.07314957380545388, 0.13190928042129482, 0.06999403129078144]], [['', '', '', ''], ['', '', '', ''], ['', '', '*', ''], ['', '', '*', '']]]
PET1 = [[[2.871602548585664, 2.8737613392507724, 2.9240172277369556, 2.9563000573608935], [2.846036499922754, 2.857730178835185, 2.931081400097111, 2.9324364644782803], [2.773159808295686, 2.7406960132364224, 2.8454358940974096, 2.836196436521112], [2.714186141198097, 2.721485437615078, 2.7901773870651985, 2.7910509953391607]], [[0.07346874613416102, 0.08915890180221644, 0.14232361843319352, 0.08379414919384695], [0.05113947020539914, 0.060274589396412975, 0.1152581396364915, 0.09007323204503911], [0.1421112053069309, 0.10121037334787775, 0.13504370218929473, 0.14821174450577274], [0.06529630679998796, 0.05820677064271456, 0.11909938551236261, 0.09268629301319398]], [['', '', '', '*'], ['', '', '', '*'], ['', '', '', ''], ['', '', '', '']]]

x = [1, 2, 3, 4]
xplc = 2.5
xlabs = []       
          
for a in range(len(LC[0])):
    if a == 0:
        for b in range(len(LC[0][a])):
            ax4.bar(x[b], LC[0][a][b], yerr=LC[1][a][b], error_kw=dict(ecolor='k', lw=2, capsize=2, capthick=2), color=colors[b], width=0.8, edgecolor='k')
            ax5.bar(x[b], PET1[0][a][b], yerr=PET1[1][a][b], error_kw=dict(ecolor='k', lw=2, capsize=2, capthick=2), color=colors[b], width=0.8, edgecolor='k')
            ax6.bar(x[b], PET2[0][a][b], yerr=PET2[1][a][b], error_kw=dict(ecolor='k', lw=2, capsize=2, capthick=2), color=colors[b], width=0.8, edgecolor='k')
    else:
        ax4.bar(x, LC[0][a], yerr=LC[1][a], error_kw=dict(ecolor='k', lw=2, capsize=2, capthick=2), color=colors, width=0.8, edgecolor='k')
        ax5.bar(x, PET1[0][a], yerr=PET1[1][a], error_kw=dict(ecolor='k', lw=2, capsize=2, capthick=2), color=colors, width=0.8, edgecolor='k')
        ax6.bar(x, PET2[0][a], yerr=PET2[1][a], error_kw=dict(ecolor='k', lw=2, capsize=2, capthick=2), color=colors, width=0.8, edgecolor='k')
    ttxt_LC, ttxt_PET1, ttxt_PET2 = [], [], []
    for b in range(len(LC[0][a])):
        ttxt_LC.append(LC[0][a][b]+LC[1][a][b]+0.05)
        ttxt_PET1.append(PET1[0][a][b]+PET1[1][a][b]+0.05)
        ttxt_PET2.append(PET2[0][a][b]+PET2[1][a][b]+0.05)
    for b in range(len(LC[2][a])):
        ax4.text(x[b], ttxt_LC[b], LC[2][a][b], ha='center', va='bottom', fontsize=12, fontweight='bold')
        ax5.text(x[b], ttxt_PET1[b], PET1[2][a][b], ha='center', va='bottom', fontsize=12, fontweight='bold')
        ax6.text(x[b], ttxt_PET2[b], PET2[2][a][b], ha='center', va='bottom', fontsize=12, fontweight='bold')
    for b in range(len(x)):
        x[b] += 4.5
    xlabs.append(xplc)
    xplc += 4.5
    
#bonds = ['C=O\n1710', 'O-H\n2920', 'C-O\n1235', 'O-H\n3300', 'C-O\n1090']

wl = [1711, 1240, 725, 1090]
bonds = ['C=O\nCA\n'+str(wl[0]), 'C-O\nCA\n'+str(wl[1]), 'C-H\nar\n'+str(wl[2]), 'C-O\nest\n'+str(wl[3])]
plt.sca(ax4)
plt.xticks(xlabs, ['', '', '', ''], fontsize=10)
#plt.ylim([0, 6])

plt.sca(ax5)
plt.xticks(xlabs, ['', '', '', ''], fontsize=10)
#plt.ylim([0, 6])

plt.sca(ax6)
plt.xticks(xlabs, bonds, fontsize=10)
#plt.ylim([0, 6])


img = plt.imread("Degradation_mechanism.png")
ax_empty.imshow(img)

FTIR_ax = [ax7, ax8, ax9]
FTIR_file = ['corrected_spectra_LC.csv', 'corrected_spectra_WPET.csv', 'corrected_spectra_PET.csv']

for a in range(len(FTIR_ax)):
    this_file = pd.read_csv(FTIR_file[a], index_col=0, header=0)
    treats = ['Control', 'Thioclava', 'Bacillus', 'Community']
    for b in range(len(treats)):
        FTIR_ax[a].plot(list(this_file.index.values), this_file.loc[:, treats[b]].values, color=colors[b])
    FTIR_ax[a].set_xlim([2000, 650])
    if a < 2:
        plt.sca(FTIR_ax[a])
        plt.xticks([])

y = [8, 4.5, 4.75]
wl.append(1410)
ytck = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5]]
for a in range(len(FTIR_ax)):
    xlim, ylim = FTIR_ax[a].get_xlim(), FTIR_ax[a].get_ylim()
    for c in wl:
        FTIR_ax[a].plot([wl, wl], ylim, 'gray', linestyle='-.', alpha=0.3)
        FTIR_ax[a].text(c+20, y[a], str(c), rotation=90, ha='right', va='center')
    FTIR_ax[a].set_xlim(xlim)
    FTIR_ax[a].set_ylim(ylim)
    plt.sca(FTIR_ax[a])
    plt.yticks(ytck[a], ytck[a])
        
ax_leg.legend(handles=handles, loc='center right', bbox_to_anchor=(1.02,0.5), fontsize=12)
ax1.text(-0.2, 0.5, 'Amorphous PET', ha='right', va='center', transform = ax1.transAxes, rotation=90, fontsize=16, fontweight='bold')
ax2.text(-0.2, 0.5, 'Weathered PET powder', ha='right', va='center', transform = ax2.transAxes, rotation=90, fontsize=16, fontweight='bold')
ax3.text(-0.2, 0.5, 'PET powder', ha='right', va='center', transform = ax3.transAxes, rotation=90, fontsize=16, fontweight='bold')

ax_empty.set_ylabel('PET degradation\nmechanism\n\n', fontsize=16, fontweight='bold')
ax_empty.set_title('A', loc='left', fontsize=16, fontweight='bold')

axis = [ax1, ax7, ax4, ax2, ax8, ax5, ax3, ax9, ax6]
labels = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

for a in range(len(axis)):
    axis[a].text(0.05, 0.9, labels[a], transform=axis[a].transAxes, fontsize=16, fontweight='bold')

ax1.set_title('Protein content', fontsize=16, fontweight='bold')
ax7.set_title('FTIR spectra', fontsize=16, fontweight='bold')
ax4.set_title(r'Ratio with reference 1410 cm$^{-1}$', fontsize=16, fontweight='bold')

ax9.set_xlabel(r'Wavelength (cm$^{-1}$)')

plt.subplots_adjust(wspace=0.5)
#plt.tight_layout()
plt.savefig('PET degradation 2.png', dpi=600)
