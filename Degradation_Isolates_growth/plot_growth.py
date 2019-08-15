import csv
import numpy
import matplotlib.pyplot as plt

days = ['Day 1.csv', 'Day 2.csv', 'Day 4.csv', 'Day 7.csv', 'Day 14.csv']
days_TPA = ['Day 1 TPA.csv', 'Day 2 TPA.csv', 'Day 4 TPA.csv', 'Day 7 TPA.csv', 'Day 14 TPA.csv']
x = [1, 2, 4, 7, 14]

def get_file(fn):
    with open(fn, 'rU') as f:
        rows = []
        for row in csv.reader(f):
            rows.append(row)
    td = rows[23][2:-1]
    ba = rows[24][2:-1]
    bl = rows[25][2:-1]
    isak = rows[26][2:-1]
    bl_ns = rows[27][2:-1]
    bl_mean, bl_ns_mean = [], []
    this_bl, this_bl_ns = [], []
    tdal, baqu, isaki = [], [], []
    this_tdal, this_baqu, this_isaki = [], [], []
    for a in range(len(bl)):
        this_bl.append(float(bl[a]))
        this_bl_ns.append(float(bl_ns[a]))
        this_tdal.append(float(td[a]))
        this_baqu.append(float(ba[a]))
        this_isaki.append(float(isak[a]))
        if (a+1) % 3 == 0:
            bl_mean.append(numpy.mean(this_bl))
            bl_ns_mean.append(numpy.mean(this_bl_ns))
            this_bl, this_bl_ns = [], []
            tdal.append(this_tdal)
            baqu.append(this_baqu)
            isaki.append(this_isaki)
            this_tdal, this_baqu, this_isaki = [], [], []
    """
    for a in range(len(tdal)):
        for b in range(len(tdal[a])):
            tdal[a][b] -= bl_mean[b]
            baqu[a][b] -= bl_mean[b]
            isaki[a][b] -= bl_ns_mean[b]
    """
    return tdal, baqu, isaki


def get_plot(days, x, savename):
    td, ba, isak = [[], [], [], []], [[], [], [], []], [[], [], [], []]
    for a in range(len(days)):
        tdal, baqu, isaki = get_file(days[a])
        for b in range(len(tdal)):
            td[b].append(tdal[b])
            ba[b].append(baqu[b])
            isak[b].append(isaki[b])
    plt.figure(figsize=(10, 5))
    ax1 = plt.subplot(131)
    ax2, ax3 = plt.subplot(132, sharex=ax1, sharey=ax1), plt.subplot(133, sharex=ax1, sharey=ax1)
    axis = [ax1, ax2, ax3]
    cols = ['k', 'b', 'g', 'r']
    labels = ['Positive', 'TPA', 'BHET', 'Amorphous PET']
    for a in range(3):
        if a == 0:
            plotting = td
        elif a == 1:
            plotting = ba
        elif a == 2:
            plotting = isak
        for b in range(len(plotting)):
            this_mean, this_std = [], []
            for c in range(len(plotting[b])):
                this_mean.append(numpy.mean(plotting[b][c]))
                this_std.append(numpy.std(plotting[b][c]))
            if a == 0 or a == 1:
                if b == 0 or b == 2:
                    axis[a].errorbar(x[:4], this_mean[:4], yerr=this_std[:4], marker='o', color=cols[b], capsize=3, label=labels[b])
                else:
                    axis[a].errorbar(x, this_mean, yerr=this_std, marker='o', color=cols[b], capsize=3, label=labels[b])
            else:
                axis[a].errorbar(x, this_mean, yerr=this_std, marker='o', color=cols[b], capsize=3, label=labels[b])
    ax3.legend(bbox_to_anchor=(1.8, 1.05))
    ax1.set_xlim([x[0]-0.5, x[-1]+0.5])
    ax1.set_ylabel('Absorbance (600 nm)')
    ax2.set_xlabel('Days')
    ax1.set_title(r'$Thioclava$ sp. BHET1')
    ax2.set_title(r'$Bacillus$ sp. BHET2')
    ax3.set_title(r'$I. sakaiensis$')
    plt.savefig('Growth day '+str(x[-1])+savename+'.png', dpi=600, bbox_inches='tight')
get_plot(days, x, '')