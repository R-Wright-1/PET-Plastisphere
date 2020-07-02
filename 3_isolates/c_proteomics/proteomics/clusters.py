import csv
import numpy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

fn = 'Gene_cluster_Tdali.csv'

with open(fn, 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)

del rows[0]

names, enzymes, size, FC, colors = [], [], [], [], []
for a in range(len(rows)):
    names.append(rows[a][1])
    enzymes.append(rows[a][2])
    size.append(rows[a][3])
    FC.append(rows[a][4])
    colors.append(rows[a][5])

start, length = [], []
count = 10
plt_count = 0
for a in range(len(size)):
    if size[a] == '':
        size[a] = 0
        plt_count = count
        count += 1000
    size[a] = float(size[a])
    start.append(count)
    length.append(size[a])
    count += size[a]+10




plt.figure(figsize=(100, 40))
axs = plt.subplot(613, frameon=False)
axs1 = plt.subplot(614, frameon=False, sharex=axs, sharey=axs)
#axsline = plt.subplot(615, frameon=False, sharex=axs, sharey=axs)
#axs.set_xlim([-200, start[-1]+length[-1]+200])
axs.set_xlim([-200, start[-1]+length[-1]+200])
axs.set_ylim([-2.5, 2.5])

#startPA = [10, 754.0, 2008.0, 2212.0, 3031.0, 3340.0, 3973.0, 5428.0, 6235.0, 6994.0, 7783.0, 8347.0, 9559.0, 10717.0, 11395.0]

def remove(xy, ax):
    if xy == 'x':
        ax.tick_params(axis='x',which='both',top='off', bottom='off')
        plt.setp(ax.get_xticklabels(), visible=False)
    elif xy == 'y':
        ax.tick_params(axis='y',which='both',left='off', right='off')
        plt.setp(ax.get_yticklabels(), visible=False)
    return
remove('x', axs), remove('y', axs)
#remove('x', axsline), remove('y', axsline)

#axsline.plot([start[0], start[0]+1000], [0,0], 'k', lw=10)
#axsline.text(start[0]+500, 1, '1 kb', fontsize=70, ha='center')

arrowstyle = mpatches.ArrowStyle.Simple(head_width=150,tail_width=80,head_length=50)
axs.plot([-400, start[0]], [0,0], 'k--')
axs.plot([start[-1]+length[-1], start[-1]+length[-1]+200], [0,0], 'k--')
colors = ['k', 'k', 'k', 'k', 'k', 'k', 'k', '#800080', 'k']
#colors = ['g', 'g', 'g', 'g', 'g', 'g', 'g']

for a in range(len(start)):
    if FC[a] == 'F':
        arrow = mpatches.FancyArrowPatch((start[a], 0), (start[a]+length[a], 0), arrowstyle=arrowstyle, facecolor=colors[a])
    else:
        arrow = mpatches.FancyArrowPatch((start[a]+length[a], 0), (start[a], 0), arrowstyle=arrowstyle, facecolor=colors[a])
    midpoint = (length[a]/2)+start[a]
    axs.add_patch(arrow)
    end = start[a]+length[a]
    for b in range(len(names[a])):
        if names[a][b] == ' ':
            names[a] = names[a][:b]+'\n'+names[a][b:]
            break
    axs.text(midpoint, 0.6, names[a], rotation=45, horizontalalignment='center', verticalalignment='bottom', fontsize=80)
axs.text(-800, 0, 'Benzoate\n pathway', ha='center', va='center', fontsize=80)
#axs.text(-800, 0, 'Long chain\nfatty acid\n degradation', ha='center', va='center', fontsize=80)
axs.plot([plt_count, plt_count+1000], [0,0], 'k--')
axs.text(0, -5, '41584', ha='center', va='center', fontsize=70, color='gray')
axs.text(end, -5, '57822', ha='center', va='center', fontsize=70, color='gray')



fn = 'Gene_cluster_Tdali2.csv'

with open(fn, 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)

del rows[0]

names, enzymes, size, FC, colors = [], [], [], [], []
for a in range(len(rows)):
    names.append(rows[a][1])
    enzymes.append(rows[a][2])
    size.append(rows[a][3])
    FC.append(rows[a][4])
    colors.append(rows[a][5])

start, length = [], []
count = 10
for a in range(len(size)):
    if size[a] == '':
        size[a] = 200
    size[a] = float(size[a])
    start.append(count)
    length.append(size[a])
    count += size[a]+10

#startPA = [10, 754.0, 2008.0, 2212.0, 3031.0, 3340.0, 3973.0, 5428.0, 6235.0, 6994.0, 7783.0, 8347.0, 9559.0, 10717.0, 11395.0]

def remove(xy, ax):
    if xy == 'x':
        ax.tick_params(axis='x',which='both',top='off', bottom='off')
        plt.setp(ax.get_xticklabels(), visible=False)
    elif xy == 'y':
        ax.tick_params(axis='y',which='both',left='off', right='off')
        plt.setp(ax.get_yticklabels(), visible=False)
    return
remove('x', axs1), remove('y', axs1)

arrowstyle = mpatches.ArrowStyle.Simple(head_width=150,tail_width=80,head_length=50)
axs1.plot([-400, start[0]], [0,0], 'k--')
axs1.plot([start[-1]+length[-1], start[-1]+length[-1]+200], [0,0], 'k--')
colors = ['k', 'k', 'k', 'k']

for a in range(len(start)):
    if FC[a] == 'F':
        arrow = mpatches.FancyArrowPatch((start[a], 0), (start[a]+length[a], 0), arrowstyle=arrowstyle, facecolor=colors[a])
    else:
        arrow = mpatches.FancyArrowPatch((start[a]+length[a], 0), (start[a], 0), arrowstyle=arrowstyle, facecolor=colors[a])
    midpoint = (length[a]/2)+start[a]
    axs1.add_patch(arrow)
    end = start[a]+length[a]
    for b in range(len(names[a])):
        if names[a][b] == ' ':
            names[a] = names[a][:b]+'\n'+names[a][b:]
            break
    axs1.text(midpoint, 0.6, names[a], rotation=45, horizontalalignment='center', verticalalignment='bottom', fontsize=80)
#axs.text(-800, 0, 'Phthalate\n degradation', ha='center', va='center', fontsize=80)
axs1.text(-800, 0, 'Terephthalate\npathway', ha='center', va='center', fontsize=80)
axs1.text(0, -5, '48661', ha='center', va='center', fontsize=70, color='gray')
axs1.text(end, -5, '52395', ha='center', va='center', fontsize=70, color='gray')


plt.subplots_adjust(hspace=1.5)

plt.savefig('Genes.pdf')
plt.close()