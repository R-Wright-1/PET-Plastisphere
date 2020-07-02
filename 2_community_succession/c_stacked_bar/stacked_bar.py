import csv
import numpy
import matplotlib.pyplot as plt
import matplotlib
import matplotlib as mpl
from scipy.cluster import hierarchy
from operator import add
import random
from colorsys import hls_to_rgb

with open('over_time_all_tax.csv', 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)

plt.figure(figsize=(20,20))
#ASV
axa1 = plt.subplot2grid((5,50), (0,0))
axa2 = plt.subplot2grid((5,50), (0,2), colspan=7)
axa3 = plt.subplot2grid((5,50), (0,10), colspan=7)
axa4 = plt.subplot2grid((5,50), (0,18), colspan=7)
axa5 = plt.subplot2grid((5,50), (0,26), colspan=7)
axa6 = plt.subplot2grid((5,50), (0,34), colspan=7)
axa7 = plt.subplot2grid((5,50), (0,42), colspan=7)
axASV = [axa1, axa2, axa3, axa4, axa5, axa6, axa7]
axa1.set_title('Inoculum')
axa2.set_title('No carbon')
axa3.set_title('Amorphous PET planktonic')
axa4.set_title('Amorphous PET biofilm')
axa5.set_title('PET powder')
axa6.set_title('Weathered PET powder')
axa7.set_title('BHET')

#Genus
axg1 = plt.subplot2grid((5,50), (1,0))
axg2 = plt.subplot2grid((5,50), (1,2), colspan=7)
axg3 = plt.subplot2grid((5,50), (1,10), colspan=7)
axg4 = plt.subplot2grid((5,50), (1,18), colspan=7)
axg5 = plt.subplot2grid((5,50), (1,26), colspan=7)
axg6 = plt.subplot2grid((5,50), (1,34), colspan=7)
axg7 = plt.subplot2grid((5,50), (1,42), colspan=7)
axGenus = [axg1, axg2, axg3, axg4, axg5, axg6, axg7]

#Family
axf1 = plt.subplot2grid((5,50), (2,0))
axf2 = plt.subplot2grid((5,50), (2,2), colspan=7)
axf3 = plt.subplot2grid((5,50), (2,10), colspan=7)
axf4 = plt.subplot2grid((5,50), (2,18), colspan=7)
axf5 = plt.subplot2grid((5,50), (2,26), colspan=7)
axf6 = plt.subplot2grid((5,50), (2,34), colspan=7)
axf7 = plt.subplot2grid((5,50), (2,42), colspan=7)
axFamily = [axf1, axf2, axf3, axf4, axf5, axf6, axf7]

#Order
axo1 = plt.subplot2grid((5,50), (3,0))
axo2 = plt.subplot2grid((5,50), (3,2), colspan=7)
axo3 = plt.subplot2grid((5,50), (3,10), colspan=7)
axo4 = plt.subplot2grid((5,50), (3,18), colspan=7)
axo5 = plt.subplot2grid((5,50), (3,26), colspan=7)
axo6 = plt.subplot2grid((5,50), (3,34), colspan=7)
axo7 = plt.subplot2grid((5,50), (3,42), colspan=7)
axOrder = [axo1, axo2, axo3, axo4, axo5, axo6, axo7]

#Class
axc1 = plt.subplot2grid((5,50), (4,0))
axc2 = plt.subplot2grid((5,50), (4,2), colspan=7)
axc3 = plt.subplot2grid((5,50), (4,10), colspan=7)
axc4 = plt.subplot2grid((5,50), (4,18), colspan=7)
axc5 = plt.subplot2grid((5,50), (4,26), colspan=7)
axc6 = plt.subplot2grid((5,50), (4,34), colspan=7)
axc7 = plt.subplot2grid((5,50), (4,42), colspan=7)
axClass = [axc1, axc2, axc3, axc4, axc5, axc6, axc7]
axes = [axASV, axGenus, axFamily, axOrder, axClass]

remx = [axa1, axa2, axa3, axa4, axa5, axa6, axa7, axg1, axg2, axg3, axg4, axg5, axg6, axg7, axf1, axf2, axf3, axf4, axf5, axf6, axf7, axo1, axo2, axo3, axo4, axo5, axo6, axo7]
remy = [axa2, axa3, axa4, axa5, axa6, axa7, axg2, axg3, axg4, axg5, axg6, axg7, axf2, axf3, axf4, axf5, axf6, axf7, axo2, axo3, axo4, axo5, axo6, axo7, axc2, axc3, axc4, axc5, axc6, axc7]

for a in remx:
    plt.setp(a.get_xticklabels(), visible=False)
    a.tick_params(axis='x',which='both',bottom='off', top='off')
for a in remy:
    plt.setp(a.get_yticklabels(), visible=False)
    a.tick_params(axis='y',which='both',left='off', right='off')

def get_only_above_min(rows, mi):
    new_rows, other = [], []
    for a in range(len(rows)):
        for b in range(len(rows[a])):
            if b > 0:
                rows[a][b] = float(rows[a][b])
        if max(rows[a][1:]) > mi:
            new_rows.append(rows[a])
        else:
            if other == []:
                other = rows[a]
                other[0] = 'Other'
            else:
                for b in range(len(rows[a])):
                    if b > 0:
                        other[b] += rows[a][b]
    new_rows.append(other)
    return new_rows

def group_to_level(rows):
    unique = []
    for a in range(len(rows)):
        adding = True
        for b in range(len(unique)):
            if unique[b] == rows[a][0]:
                adding = False
        if adding:
            unique.append(rows[a][0])
    unique = sorted(unique)
    grouped_rows = []
    for a in range(len(unique)):
        this_row = []
        for b in range(len(rows)):
            if unique[a] == rows[b][0]:
                this_row.append(rows[b])
        new_row = []
        for c in range(len(this_row[0])):
            if c == 0:
                new_row.append(this_row[c][0])
            else:
                this_num = 0
                for d in range(len(this_row)):
                    this_num += float(this_row[d][c])
                new_row.append(this_num)
        grouped_rows.append(new_row)
    return grouped_rows


for a in range(len(rows)):
    if a > 0:
        for b in range(5):
            if b == 0:
                rows[a][b] = 'ASV'+str(int(rows[a][b][3:]))
            if b == 1:
                if rows[a][b] != 'NA':
                    rows[a][b] = '$'+rows[a][b]+'$'
ASV_rows, genus_rows, family_rows, order_rows, class_rows = [], [], [], [], []
new_rows = [ASV_rows, genus_rows, family_rows, order_rows, class_rows]
for a in range(5):
    for b in range(len(rows)):
        new_rows[a].append([rows[b][a]]+rows[b][5:])

"""
def get_distinct_colors(n):
    colors = []
    for i in numpy.arange(0., 360., 360. / n):
        h = i / 360.
        l = (50 + numpy.random.rand() * 10) / 100.
        s = (90 + numpy.random.rand() * 10) / 100.
        colors.append(hls_to_rgb(h, l, s))
    random.shuffle(colors)
    return colors
"""

def get_distinct_colors(num):
    colormap_20, colormap_40b, colormap_40c = mpl.cm.get_cmap('tab20', 256), mpl.cm.get_cmap('tab20b', 256), mpl.cm.get_cmap('tab20c', 256)
    norm, norm2 = mpl.colors.Normalize(vmin=0, vmax=19), mpl.colors.Normalize(vmin=20, vmax=39)
    m1, m2, m3 = mpl.cm.ScalarMappable(norm=norm, cmap=colormap_20), mpl.cm.ScalarMappable(norm=norm, cmap=colormap_40b), mpl.cm.ScalarMappable(norm=norm2, cmap=colormap_40c)
    colors_20 = [m1.to_rgba(a) for a in range(20)]
    colors_40 = [m2.to_rgba(a) for a in range(20)]+[m3.to_rgba(a) for a in range(20,40)]
    if num < 21: return colors_20
    elif num < 41: return colors_40
    else: return colors_40+colors_40+colors_40

numrows = [4, 3, 3, 2, 1]
saving = []
for a in range(len(new_rows)):
    del new_rows[a][0]
    if a != 0:
        new_rows[a] = group_to_level(new_rows[a])
    l = len(new_rows[a])
    new_rows[a] = get_only_above_min(new_rows[a], 1)
    # if a == 2:
    #     print(new_rows[a])
    Inoc, NoC, LCW, LC, PET, WPET, BHET = [], [], [], [], [], [], []
    labels = []
    for b in range(len(new_rows[a])):
        labels.append(new_rows[a][b][0])
        Inoc.append(new_rows[a][b][1])
        NoC.append(new_rows[a][b][2:9])
        LCW.append(new_rows[a][b][9:16])
        LC.append(new_rows[a][b][16:23])
        PET.append(new_rows[a][b][23:30])
        WPET.append(new_rows[a][b][30:37])
        BHET.append(new_rows[a][b][37:44])
    #print(sum(Inoc))
    y = [Inoc, NoC, LCW, LC, PET, WPET, BHET]
    x = [[1], [1,2,3,4,5,6,7], [1,2,3,4,5,6,7], [1,2,3,4,5,6,7], [1,2,3,4,5,6,7], [1,2,3,4,5,6,7], [1,2,3,4,5,6,7]]
    colors = get_distinct_colors(len(new_rows[a]))
    for c in range(len(y)):
        data = numpy.array(y[c])
        bottom = numpy.cumsum(data, axis=0)
        ax = axes[a][c]
        ax.bar(x[c], data[0], color=colors[0], width=0.8, label=labels[0], edgecolor='k')
        saving.append(labels[0])
        for j in range(1, data.shape[0]):
            ax.bar(x[c], data[j], color=colors[j], bottom=bottom[j-1], width=0.8, label=labels[j], edgecolor='k')
            saving.append(labels[j])
        ax.set_xlim([x[c][0]-0.5, x[c][-1]+0.5])
        ax.set_ylim([0,100])
    numrow = numrows[a]
    axes[a][-1].legend(bbox_to_anchor=(1,1), ncol=numrow)
xlab = ['1', '3', '7', '14', '21', '30', '42']
plt.sca(axc1), plt.xticks([1], ['0'])
plt.sca(axc2), plt.xticks(x[1], xlab)
plt.sca(axc3), plt.xticks(x[1], xlab)
plt.sca(axc4), plt.xticks(x[1], xlab)
plt.sca(axc5), plt.xticks(x[1], xlab)
plt.sca(axc6), plt.xticks(x[1], xlab)
plt.sca(axc7), plt.xticks(x[1], xlab)
axa1.set_ylabel('ASV\nRelative abundance (%)')
axg1.set_ylabel('Genus\nRelative abundance (%)')
axf1.set_ylabel('Family\nRelative abundance (%)')
axo1.set_ylabel('Order\nRelative abundance (%)')
axc1.set_ylabel('Class\nRelative abundance (%)')
    
#print(saving)
        
plt.savefig('Bars_1pc.png', bbox_inches='tight', dpi=300)