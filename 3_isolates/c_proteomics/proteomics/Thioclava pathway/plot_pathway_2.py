import numpy
import matplotlib.pyplot as plt
import csv
import matplotlib as mpl
from matplotlib import rcParams
import math
rcParams['axes.titlepad'] = 15
title1 = ''

#with open('Hcamp_confirmed_transporters.csv', 'rU') as f:
with open('Thioclava_confirmed.csv', 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)
abun, P, PhAc, labels = [], [], [], []
max_P, min_P, max_PhAc, min_PhAc, max_abun, min_abun = 0, 0, 0, 0, 0, 0
for a in range(len(rows)):
    if a > 0:
        for b in range(len(rows[a])):
            if b > 0:
                rows[a][b] = float(rows[a][b])
                if b > 5:
                    rows[a][b] = math.pow(2, rows[a][b])
                    if rows[a][b] < 1:
                        rows[a][b] = -(1/rows[a][b])
        labels.append(rows[a][0])
        abun.append(rows[a][1:6])
        if max(rows[a][1:6]) > max_abun: max_abun = max(rows[a][1:6])
        if min(rows[a][1:6]) < min_abun: min_abun = min(rows[a][1:6])
        P.append(rows[a][6:10])
        if max(rows[a][6:10]) > max_P: max_P = max(rows[a][6:10])
        if min(rows[a][6:10]) < min_P: min_P = min(rows[a][6:10])
        PhAc.append(rows[a][10:])
        if max(rows[a][10:]) > max_PhAc: max_PhAc = max(rows[a][10:])
        if min(rows[a][10:]) < min_PhAc: min_PhAc = min(rows[a][10:])

cmap_up = 'seismic'
norm_up = mpl.colors.Normalize(vmin=-8, vmax=10)
colormap_up = mpl.cm.get_cmap(cmap_up, 256)
m_up = mpl.cm.ScalarMappable(norm=norm_up, cmap=colormap_up)

cmap_down = 'seismic'
norm_down = mpl.colors.Normalize(vmin=-10, vmax=8)
colormap_down = mpl.cm.get_cmap(cmap_down, 256)
m_down = mpl.cm.ScalarMappable(norm=norm_down, cmap=colormap_down)

cmap_abun = 'Greens'
norm_abun = mpl.colors.Normalize(vmin=0, vmax=max_abun)
colormap_abun = mpl.cm.get_cmap(cmap_abun, 256)
m_abun = mpl.cm.ScalarMappable(norm=norm_abun, cmap=colormap_abun)

def remove(xy, ax):
    if xy == 'x':
        ax.tick_params(axis='x',which='both',top='off', bottom='off')
        plt.setp(ax.get_xticklabels(), visible=False)
    elif xy == 'y':
        ax.tick_params(axis='y',which='both',left='off', right='on')
        #plt.setp(ax.get_yticklabels(), visible=False)
    return

for a in range(len(abun)):
    fig = plt.figure(figsize=(5,4))
    PhAc = P[a][0]
    DBP = P[a][1]
    DEHP = P[a][2]
    ATBC = P[a][3]
    PhAc_a = abun[a][1]
    DBP_a = abun[a][2]
    DEHP_a = abun[a][3]
    ATBC_a = abun[a][4]
    ax = plt.subplot(121)
    fs=40
    if DEHP > 0:
        #ax.bar([1,2], [1, 1], color=[m_abun.to_rgba(DEHP_a), m_up.to_rgba(DEHP)], width=1)#, edgecolor='k')
        ax.bar([1], [1], color=[m_up.to_rgba(DEHP)], bottom=[1], width=1)#, edgecolor='k')
        if DEHP > (5):tx = 'w'
        else:tx = 'k'
    else:
        if DEHP < (-4):tx = 'w'
        else:tx = 'k'
        #ax.bar([1,2], [1, 1], color=[m_abun.to_rgba(DEHP_a), m_down.to_rgba(DEHP)], width=1)#, edgecolor='k')
        ax.bar([1], [1, 1], color=[m_down.to_rgba(DEHP)], bottom=[1], width=1)#, edgecolor='k')
    ax.text(1, 1.5, str(round(DEHP,1)), color=tx, fontsize=fs, ha='center', va='center')
    if DBP > 0:
        #ax.bar([1,2], [1, 1], color=[m_abun.to_rgba(DBP_a), m_up.to_rgba(DBP)], bottom=[1,1], width=1)#, edgecolor='k')
        ax.bar([1], [1], color=[m_up.to_rgba(DBP)], bottom=[2], width=1)#, edgecolor='k')
        if DBP > (7.5):tx = 'w'
        else:tx = 'k'
    else:
        if DBP < (-4):tx = 'w'
        else:tx = 'k'
        #ax.bar([1,2], [1, 1], color=[m_abun.to_rgba(DBP_a), m_down.to_rgba(DBP)], bottom=[1,1], width=1)#, edgecolor='k')
        ax.bar([1], [1], color=[m_down.to_rgba(DBP)], bottom=[2], width=1)#, edgecolor='k')
    ax.text(1, 2.5, str(round(DBP,1)), color=tx, fontsize=fs, ha='center', va='center')
    if PhAc > 0:
        #ax.bar([1,2], [1, 1], color=[m_abun.to_rgba(PhAc_a), m_up.to_rgba(PhAc)], bottom=[2,2], width=1)#, edgecolor='k')
        ax.bar([1], [1], color=[m_up.to_rgba(PhAc)], bottom=[3], width=1)#, edgecolor='k')
        if PhAc > (7.5):tx = 'w'
        else:tx = 'k'
    else:
        if PhAc < (-4):tx = 'w'
        else:tx = 'k'
        #ax.bar([1,2], [1, 1], color=[m_abun.to_rgba(PhAc_a), m_down.to_rgba(PhAc)], bottom=[2,2], width=1)#, edgecolor='k')
        ax.bar([1], [1], color=[m_down.to_rgba(PhAc)], bottom=[3], width=1)#, edgecolor='k')
    ax.text(1, 3.5, str(round(PhAc,1)), color=tx, fontsize=fs, ha='center', va='center')
    if ATBC > 0:
        ax.bar([1], [1], color=[m_up.to_rgba(ATBC)], width=1)
        if ATBC > (7.5):tx = 'w'
        else:tx = 'k'
    else:
        if ATBC < (-4):tx = 'w'
        else:tx = 'k'
        ax.bar([1], [1], color=[m_down.to_rgba(ATBC)], width=1)
    #ax.text(1, 0.5, str(round(ATBC,1)), color=tx, fontsize=fs, ha='center', va='center')
    y_lab = ['PETB ('+str(round(ATBC_a,2))+'%)', 'PET ('+str(round(DEHP_a,2))+'%)', 'BHET ('+str(round(DBP_a,2))+'%)', 'TPA ('+str(round(PhAc_a,2))+'%)']
    remove('x', ax), remove('y', ax)
    ax.plot([0.5,2.5], [1,1], 'k-')
    ax.plot([0.5,2.5], [2,2], 'k-')
    ax.plot([0.5,2.5], [3,3], 'k-')
    #ax.text(1.5, 0.5, 'DEHP', fontsize=fs, horizontalalignment='center', verticalalignment='center')
    #ax.text(1.5, 1.5, 'DBP', fontsize=fs, horizontalalignment='center', verticalalignment='center')
    #ax.text(1.5, 2.5, 'Phthalic acid', fontsize=fs, horizontalalignment='center', verticalalignment='center')
    ax.yaxis.tick_right()
    #plt.yticks([0.5, 1.5, 2.5, 3.5], y_lab, fontsize=fs)
    #ax.set_ylim([0,4])
    plt.yticks([1.5, 2.5, 3.5], y_lab[1:], fontsize=fs)
    ax.set_ylim([1,4])
    ax.set_xlim([0.5,1.5])
    title = title1
    adding = False
    count = 0
    for b in range(len(labels[a])):
        if labels[a][b] == '_':
            adding = True
        if labels[a][b] == ' ':
            count += 1
            if count == 2:
                title += '\n'
        if adding:
            title += labels[a][b]
    ax.text(2.2, 4.3, title[2:], fontsize=fs, ha='center', va='bottom')
    #fig.text(0.5, 1, title[2:], ha='center', va='top')
    plt.savefig(labels[a]+'.pdf', bbox_inches='tight')
    plt.close()

ax1 = plt.subplot2grid((6,2), (0,0), colspan=2)

norm = mpl.colors.Normalize(vmin=0, vmax=1)
cb1 = mpl.colorbar.ColorbarBase(ax1, cmap='seismic', norm=norm, orientation='horizontal')

ax1.text(0.5,1, 'Fold change', ha='center', va='bottom', fontsize=fs)
cb1.set_ticks([0, 1])
cb1.set_ticklabels(['<-10', '>10'])
cb1.ax.tick_params(labelsize=fs-10)

plt.subplots_adjust(wspace=0)
plt.savefig('Colorbars.pdf', bbox_inches='tight')