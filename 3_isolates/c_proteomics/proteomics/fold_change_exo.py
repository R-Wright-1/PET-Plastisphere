import csv
import numpy
from scipy import stats
import math
import matplotlib.pyplot as plt
import matplotlib as mpl


fn = 'Thioclava_exo.csv'
beg = 'TD'
#ls, mw, ms = 40, 5, 30
ls, mw, ms = 10, 2, 10
new_fn = fn[:-4]+'_fc.csv'

with open(fn, 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)

means = [['P', 'TPA', 'BHET', 'PET']]
sd = [['P_sd', 'TPA_sd', 'BHET_sd', 'PET_sd']]
fc = [['P_TPA_fc', 'P_BHET_fc', 'P_PET_fc']]
t_test = [['P_TPA_ttest', 'P_BHET_ttest', 'P_PET_ttest']]
t_test_sig = [['P_TPA_ttest_sig', 'P_BHET_ttest_sig', 'P_PET_ttest_sig']]
t_test_TPA = [['TPA_BHET_ttest', 'TPA_PET_ttest']]
t_test_TPA_sig = [['TPA_BHET_ttest_sig', 'TPA_PET_ttest_sig']]
rel_abun = [['P_relabun', 'TPA_relabun', 'BHET_relabun', 'PET_relabun']]
fc_TPA = [['TPA_BHET_fc', 'TPA_PET_fc']]
t_test_BHET = [['BHET_PET_ttest']]
t_test_BHET_sig = [['BHET_PET_ttest_sig']]
fc_BHET = [['BHET_PET_fc']]


for a in range(len(rows)):
    for b in range(len(rows[a])):
        if a > 0 and b > 0:
            rows[a][b] = float(rows[a][b])
        
for a in range(len(rows)):
    if a > 0:
        P, TPA, BHET, PET = [rows[a][1], rows[a][2], rows[a][3]], [rows[a][4], rows[a][5], rows[a][6]], [rows[a][7], rows[a][8], rows[a][9]], [rows[a][10], rows[a][11], rows[a][12]]
        P_mean, TPA_mean, BHET_mean, PET_mean = numpy.mean(P), numpy.mean(TPA), numpy.mean(BHET), numpy.mean(PET)
        this_means = [P_mean, TPA_mean, BHET_mean, PET_mean]
        this_sd = [numpy.std(P),
                      numpy.std(TPA),
                      numpy.std(BHET),
                      numpy.std(PET)]
        means.append(this_means)
        sd.append(this_sd)
        this_fc, this_fc_TPA, this_fc_BHET = [], [], []
        #this_fc.append(math.pow(2, TPA_mean/P_mean)), this_fc.append(math.pow(2, BHET_mean/P_mean)), this_fc.append(math.pow(2, PET_mean/P_mean)), this_fc.append(math.pow(2, PETB_mean/P_mean))
        this_fc.append((TPA_mean-P_mean)), this_fc.append((BHET_mean-P_mean)), this_fc.append((PET_mean-P_mean))
        fc.append(this_fc)
        this_fc_TPA.append((BHET_mean-TPA_mean)), this_fc_TPA.append((PET_mean-TPA_mean))
        fc_TPA.append(this_fc_TPA)
        this_fc_BHET.append((PET_mean-BHET_mean))
        fc_BHET.append(this_fc_BHET)
        this_ttest = [stats.ttest_ind(P,TPA)[1], stats.ttest_ind(P,BHET)[1], stats.ttest_ind(P,PET)[1]]
        t_test.append(this_ttest)
        this_ttest_TPA = [stats.ttest_ind(TPA,BHET)[1], stats.ttest_ind(TPA,PET)[1]]
        t_test_TPA.append(this_ttest_TPA)
        this_ttest_BHET = [stats.ttest_ind(BHET,PET)[1]]
        t_test_BHET.append(this_ttest_BHET)
        this_ttest_sig, this_ttest_TPA_sig, this_ttest_BHET_sig = [], [], []
        for b in range(len(this_ttest)):
            if this_ttest[b] <= 0.05:
                this_ttest_sig.append('+')
            else:
                this_ttest_sig.append('')
        for c in range(len(this_ttest_TPA)):
            if this_ttest_TPA[c] <= 0.05:
                this_ttest_TPA_sig.append('+')
            else:
                this_ttest_TPA_sig.append('')
        for d in range(len(this_ttest_BHET)):
            if this_ttest_BHET[d] <= 0.05:
                this_ttest_BHET_sig.append('+')
            else:
                this_ttest_BHET_sig.append('')
        t_test_sig.append(this_ttest_sig)
        t_test_TPA_sig.append(this_ttest_TPA_sig)
        t_test_BHET_sig.append(this_ttest_BHET_sig)
                

sums = []
for a in range(len(means[0])):
    count = 0
    for b in range(len(means)):
        if b > 0:
             count += math.pow(2, means[b][a])
    sums.append(count)

for a in range(len(means)):
    if a > 0:
        this_rel_abun = []
        for b in range(len(means[a])):
            this_rel_abun.append((math.pow(2, means[a][b])/sums[b])*100)
        rel_abun.append(this_rel_abun)
    

with open(new_fn, 'w') as f:
    writer = csv.writer(f)
    for a in range(len(rows)):
        writer.writerow(rows[a]+rel_abun[a]+means[a]+sd[a]+fc[a]+fc_TPA[a]+fc_BHET[a]+t_test[a]+t_test_sig[a]+t_test_TPA[a]+t_test_TPA_sig[a]+t_test_BHET[a]+t_test_BHET_sig[a])
"""
max_fc, min_fc, max_rel_abun = 0, 0, 0
for a in range(len(rel_abun)):
    if a > 0:
        for b in range(len(rel_abun[a])):
            if rel_abun[a][b] > max_rel_abun:
                max_rel_abun = rel_abun[a][b]
        for b in range(len(fc[a])):
            if fc[a][b] > max_fc:
                max_fc = fc[a][b]
            if fc[a][b] < min_fc:
                min_fc = fc[a][b]
print(max_rel_abun, max_fc, min_fc, len(rows))

def remove(xy, ax):
    if xy == 'x':
        ax.tick_params(axis='x',which='both',top='off', bottom='off')
        plt.setp(ax.get_xticklabels(), visible=False)
    elif xy == 'y':
        ax.tick_params(axis='y',which='both',left='off', right='off')
        plt.setp(ax.get_yticklabels(), visible=False)
    return

l1 = len(rows)
cmap_up = 'Reds'
norm_up = mpl.colors.Normalize(vmin=0, vmax=max_fc)
colormap_up = mpl.cm.get_cmap(cmap_up, 256)
m_up = mpl.cm.ScalarMappable(norm=norm_up, cmap=colormap_up)

cmap_down = 'Blues_r'
norm_down = mpl.colors.Normalize(vmin=min_fc, vmax=0)
colormap_down = mpl.cm.get_cmap(cmap_down, 256)
m_down = mpl.cm.ScalarMappable(norm=norm_down, cmap=colormap_down)

cmap_abun = 'Greens'
norm_abun = mpl.colors.Normalize(vmin=0, vmax=max_rel_abun)
colormap_abun = mpl.cm.get_cmap(cmap_abun, 256)
m_abun = mpl.cm.ScalarMappable(norm=norm_abun, cmap=colormap_abun)

colors_abun, colors_P, colors_TPA, labels = [], [], [], []
nums_abun, nums_P, nums_TPA = [], [], []
for a in range(len(rows)):
    if a > 0:
        name = beg
        for c in range(len(rows[a][0])):
            if rows[a][0][c] == '_':
                name += rows[a][0][c:]
        labels.append(name)
        ab, cp, cTPA = [], [], []
        nab, np, nTPA = [], [], []
        for b in range(len(rel_abun[a])):
            ab.append(m_abun.to_rgba(rel_abun[a][b]))
            nab.append(1)
        for c in range(len(fc[a])):
            if fc[a][c] > 0:
                m = m_up
            else:
                m = m_down
            cp.append(m.to_rgba(fc[a][c]))
            np.append(1)
        for d in range(len(fc_TPA[a])):
            if fc_TPA[a][d] > 0:
                m = m_up
            else:
                m = m_down
            cTPA.append(m.to_rgba(fc_TPA[a][d]))
            nTPA.append(1)
        colors_abun.append(ab)
        colors_P.append(cp)
        colors_TPA.append(cTPA)
        nums_abun.append(nab)
        nums_P.append(np)
        nums_TPA.append(nTPA)


fig = plt.figure(figsize=(30, 250))

colors_abun.reverse()
colors_P.reverse()
colors_TPA.reverse()
labels.reverse()
del t_test_sig[0]
del t_test_TPA_sig[0]
t_test_sig.reverse()
t_test_TPA_sig.reverse()
sig = []
for a in range(len(t_test_sig)):
    sig.append(t_test_sig[a]+t_test_TPA_sig[a])


data_abun = numpy.array(nums_abun)
bottom_abun = numpy.cumsum(data_abun, axis=0)
data_P = numpy.array(nums_P)
bottom_P = numpy.cumsum(data_P, axis=0)
data_TPA = numpy.array(nums_TPA)
bottom_TPA = numpy.cumsum(data_TPA, axis=0)

ax = plt.subplot2grid((40,1), (1,0), rowspan=39)

col_abun = plt.subplot2grid((80,14), (0,0), colspan=5)
col_down = plt.subplot2grid((80,28), (0,13), colspan=7)
col_up = plt.subplot2grid((80,28), (0,20), colspan=7)
remove('y', col_abun), remove('y', col_down), remove('y', col_up)

norm = mpl.colors.Normalize(vmin=0, vmax=1)
cb1 = mpl.colorbar.ColorbarBase(col_abun, cmap=colormap_abun, norm=norm, orientation='horizontal')
cb2 = mpl.colorbar.ColorbarBase(col_down, cmap=colormap_down, norm=norm, orientation='horizontal')
cb3 = mpl.colorbar.ColorbarBase(col_up, cmap=colormap_up, norm=norm, orientation='horizontal')

cb1.set_ticks([0, 0.5, 1]), cb2.set_ticks([0, 0.5, 1]), cb3.set_ticks([0, 0.5, 1])
cb1.set_ticklabels(['0', '', str(round(max_rel_abun,2))])
cb2.set_ticklabels([str(round(min_fc,2)), 'Down', '0'])
cb3.set_ticklabels(['', 'Up', str(round(max_fc,2))])

cb1.ax.tick_params(labelsize=30), cb2.ax.tick_params(labelsize=30), cb3.ax.tick_params(labelsize=30)
ax.bar([1, 2, 3, 4, 5], data_abun[0], color=colors_abun[0], width=1, edgecolor='k')
ax.bar([7, 8, 9, 10], data_P[0], color=colors_P[0], width=1, edgecolor='k')
ax.bar([12, 13, 14], data_TPA[0], color=colors_TPA[0], width=1, edgecolor='k')
y = [0.5]

for j in range(1, data_abun.shape[0]):
    ax.bar([1, 2, 3, 4, 5], data_abun[j], color=colors_abun[j], bottom=bottom_abun[j-1], width=1, edgecolor='k')
    ax.bar([7, 8, 9, 10], data_P[j], color=colors_P[j], bottom=bottom_P[j-1], width=1, edgecolor='k')
    ax.bar([12, 13, 14], data_TPA[j], color=colors_TPA[j], bottom=bottom_TPA[j-1], width=1, edgecolor='k')
    y.append(j+0.5)  
poss_x = [7, 8, 9, 10, 12, 13, 14]

for a in range(len(sig)):
    for b in range(len(sig[a])):
        if sig[a][b] == '+':
            ax.plot([poss_x[b], poss_x[b]], [a+0.5, a+0.5], marker='+', mew=mw, markersize=ms, color='k')

ax.yaxis.tick_right()
ax.xaxis.tick_top()
ylab = plt.setp(ax, yticks=y, yticklabels=labels)
xlab = plt.setp(ax, xticks=[1, 2, 3, 4, 5, 7, 8, 8.5, 9, 10, 12, 13, 14], xticklabels=['P', 'TPA', 'Relative abundance (%)\nBHET', 'PET', 'PETB', 'TPA', 'BHET', 'Fold change vs Positive\n', 'PET', 'PETB', 'BHET', 'Fold change vs TPA\nPET', 'BHET'])
ax.tick_params(axis='both', which='major', labelsize=ls)
ax.tick_params(axis='both', which='minor', labelsize=ls)
ax.set_xlim([0.5, 14.5])
ax.set_ylim([0, y[-1]+0.5])

plt.subplots_adjust(wspace=0, hspace=0.3)
plt.savefig(fn[:-4]+'.pdf', bbox_inches='tight')
plt.close()


fig = plt.figure(figsize=(30, 200))
for a in range(len(rows)):
    if a > 0:
        ax1 = plt.subplot2grid((l1, 15), (a, 0))
        ax2, ax3, ax4, ax5 = plt.subplot2grid((l1, 15), (a, 1), sharex=ax1, sharey=ax1), plt.subplot2grid((l1, 15), (a, 2), sharex=ax1, sharey=ax1), plt.subplot2grid((l1, 15), (a, 3), sharex=ax1, sharey=ax1), plt.subplot2grid((l1, 15), (a, 4), sharex=ax1, sharey=ax1)
        remove('x', ax1), remove('x', ax2), remove('x', ax3), remove('x', ax4), remove('x', ax5)
        remove('y', ax1), remove('y', ax2), remove('y', ax3), remove('y', ax4), remove('y', ax5)
        ax_blob = [ax1, ax2, ax3, ax4, ax5]
        for b in range(len(rel_abun[a])):
            ax_blob[b].barh(0.5, rel_abun[a][b])
            #plt.xlim([0, 1]), plt.ylim([0.5,1.5])
        ax1h = plt.subplot2grid((l1, 15), (a, 6))
        ax2h, ax3h, ax4h = plt.subplot2grid((l1, 15), (a, 7), sharex=ax1h, sharey=ax1h), plt.subplot2grid((l1, 15), (a, 8), sharex=ax1h, sharey=ax1h), plt.subplot2grid((l1, 15), (a, 9), sharex=ax1h, sharey=ax1h)
        remove('x', ax1h), remove('x', ax2h), remove('x', ax3h), remove('x', ax4h)
        remove('y', ax1h), remove('y', ax2h), remove('y', ax3h), remove('y', ax4h)
        ax_fc = [ax1h, ax2h, ax3h, ax4h]
        for b in range(len(fc[a])):
            if fc[a][b] > 0:
                m = m_up
            else:
                m = m_down
            ax_fc[b].bar(1, 1, color=m.to_rgba(fc[a][b]), width=1)
        ax1h.set_xlim([0.5,1.5]), ax1h.set_ylim([0,1])
        name = beg
        for c in range(len(rows[a][0])):
            if rows[a][0][c] == '_':
                name += rows[a][0][c:]
        
        #ax1.set_title('P'), ax2.set_title('TPA'), ax3.set_title('BHET'), ax4.set_title('PET'), ax5.set_title('PETB')
        #ax1h.set_title('P_TPA'), ax2h.set_title('P_BHET'), ax3h.set_title('P_PET'), ax4h.set_title('P_PETB')
        
        ax1TPA = plt.subplot2grid((l1, 15), (a, 11))
        ax2TPA, ax3TPA = plt.subplot2grid((l1, 15), (a, 12), sharex=ax1TPA, sharey=ax1TPA), plt.subplot2grid((l1, 15), (a, 13), sharex=ax1TPA, sharey=ax1TPA)
        remove('x', ax1TPA), remove('x', ax2TPA), remove('x', ax3TPA)
        remove('y', ax1TPA), remove('y', ax2TPA)
        ax_TPA = [ax1TPA, ax2TPA, ax3TPA]
        for b in range(len(fc_TPA[a])):
            if fc_TPA[a][b] > 0:
                m = m_up
            else:
                m = m_down
            ax_TPA[b].bar(1, 1, color=m.to_rgba(fc_TPA[a][b]), width=1)
        ax1TPA.set_xlim([0.5,1.5]), ax1TPA.set_ylim([0,1])
        ax3TPA.yaxis.tick_right()
        plt.setp(ax3TPA, yticks=[0.5], yticklabels=[name])
"""

        