import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy
import matplotlib
from colorsys import hls_to_rgb
import random
#from matplotlib.mlab import bivariate_normal

unique_to_trt = [5, 14, 20, 21, 24, 25, 30, 33, 34, 38, 40, 43, 45, 48, 54, 55, 56, 64, 65, 73, 76, 77, 78, 80, 84, 86, 87, 88, 98, 99, 102, 108, 109, 114, 124, 125, 140, 141, 147, 149, 165, 334]

cs, cf = [2, 9, 16, 23, 30, 37], [9, 16, 23, 30, 37, 44]
with open('Taxonomy.csv', 'rU') as f:
    this_tax = []
    for row in csv.reader(f):
        this_tax.append(row)

plt.figure(figsize=(16,20))
ax1 = plt.subplot2grid((43,18), (2,0), colspan=4, rowspan=19)
ax2 = plt.subplot2grid((43,18), (2,5), colspan=4, rowspan=19)
ax3 = plt.subplot2grid((43,18), (2,10), colspan=4, rowspan=19)
ax4 = plt.subplot2grid((43,18), (23,0), colspan=4, rowspan=19)
ax5 = plt.subplot2grid((43,18), (23,5), colspan=4, rowspan=19)
ax6 = plt.subplot2grid((43,18), (23,10), colspan=4, rowspan=19)

ax7 = plt.subplot2grid((43,54), (3,46), colspan=1, rowspan=10)

axcolbar = plt.subplot2grid((43,54), (1,46), colspan=8)
plt.sca(axcolbar)
plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)
plt.tick_params(axis='x', which='both', top=False, bottom=False, labelbottom=False)
axcolbar.text(0.1, 0.5, '0', ha='center', va='center', color='w')
axcolbar.text(0.9, 0.5, '1', ha='center', va='center', color='k')
norm = mpl.colors.Normalize(vmin=0, vmax=1)
colormap = mpl.cm.get_cmap('plasma', 256)
matplotlib.colorbar.ColorbarBase(axcolbar, cmap=colormap, norm=norm, orientation='horizontal')
plt.tick_params(axis='x', which='both', top=False, bottom=False, labelbottom=False)
plt.xlabel('Normalised relative abundance')

def get_distinct_colors(n):
    colors = []
    for i in numpy.arange(0., 360., 360. / n):
        h = i / 360.
        l = (50 + numpy.random.rand() * 10) / 100.
        s = (90 + numpy.random.rand() * 10) / 100.
        colors.append(hls_to_rgb(h, l, s))
    random.shuffle(colors)
    return colors

axis = [ax6, ax1, ax2, ax3, ax4, ax5]
titles = ['No carbon', 'BHET', 'Amorphous PET biofilm', 'Amorphous PET\nplanktonic', 'PET powder', 'Weathered PET powder']
letter = ['F', 'A', 'B', 'C', 'D', 'E']
lim = 0.49
all_unique_tax = sorted(['Caulobacterales', 'Rhodobacterales', 'Xanthomonadales', 'Vibrionales', 'Bacteroidales', 'Alteromonadales', 'Rhodovibrionales', 'Oceanospirillales', 'Cytophagales', 'Rhodospirillales', 'Nitrosococcales', 'Bacillales', 'Rhizobiales', 'Parvibaculales', 'Betaproteobacteriales', 'Chitinophagales', 'Micrococcales', 'Sphingomonadales', 'Pseudomonadales', 'Nitrospirales'])
#all_unique_tax = sorted(['Caulobacterales', 'Alphaproteobacteria', 'Rhodobacterales', 'Xanthomonadales', 'Vibrionales', 'Bacteroidales', 'Alteromonadales', 'Rhodovibrionales', 'Oceanospirillales', 'Cytophagales', 'Rhodospirillales', 'Nitrosococcales', 'Bacillales', 'Rhizobiales', 'Parvibaculales', 'Betaproteobacteriales', 'Chitinophagales', 'Micrococcales', 'Sphingomonadales', 'Pseudomonadales', 'Nitrospirales', 'Gammaproteobacteria'])
tax_colors = get_distinct_colors(len(all_unique_tax))
all_unique_tax.append('Other')
tax_colors.append('k')

for a in range(6):
    with open('Taxonomy.csv', 'rU') as f:
        tax = []
        for row in csv.reader(f):
            tax.append(row)
    #if a != 0:
    #    break
    with open('over_time_all.csv', 'rU') as f:
        rows = []
        for row in csv.reader(f):
            rows.append(row)
    this_treat = []
    for b in range(len(rows)):
        this_treat.append(rows[b][0:2]+rows[b][cs[a]:cf[a]])
    treat_order = [this_treat[0]]
    new_treat = []
    name = this_treat[0][2][5:]
    for b in range(1, len(this_treat)):
        for c in range(1, len(this_treat[b])):
            this_treat[b][c] = float(this_treat[b][c])
        if round(max(this_treat[b][1:]),1) > lim:
            new_treat.append(this_treat[b])
            if b == 1:
                omi = min(this_treat[b][1:])
                oma = max(this_treat[b][1:])
            else:
                if min(this_treat[b][1:]) < omi:
                    omi = min(this_treat[b][1:])
                if max(this_treat[b][1:]) > oma:
                    oma = max(this_treat[b][1:])
    this_treat = new_treat
    for b in this_treat: #Day 1
        if max(b[1:]) == b[2]:
            treat_order.append(b)
    for b in this_treat: #Day 2
        if max(b[1:]) == b[3]:
            treat_order.append(b)
    for b in this_treat: #Day 3
        if max(b[1:]) == b[4]:
            treat_order.append(b)
    for b in this_treat: #Day 4
        if max(b[1:]) == b[5]:
            treat_order.append(b)
    for b in this_treat: #Day 5
        if max(b[1:]) == b[6]:
            treat_order.append(b)
    for b in this_treat: #Day 6
        if max(b[1:]) == b[7]:
            treat_order.append(b)
    for b in this_treat: #Day 7
        if max(b[1:]) == b[8]:
            treat_order.append(b)
    for b in range(1, len(treat_order)):
        for c in range(1, len(treat_order[b])):
            if treat_order[b][c] == 0:
                treat_order[b][c] = 0.001
    ax = axis[a]
    bottom = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #y = [1, 1, 1, 1, 1, 1, 1, 1]
    #x = [0, 1, 2.5, 5.5, 11, 18, 26, 36.5]
    #width = [1, 1, 2, 4, 7, 7, 9, 12]
    xlab = [1, 3, 7, 14, 21, 30, 42]
    y = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    x = [0, 1, 2.5, 5.5, 11, 18, 26, 36.5, 44]
    width = [1, 1, 2, 4, 7, 7, 9, 12, 3]
    
    xtxt = ['1', '3', '7', '14', '21', '30', '42']
    colormap = mpl.cm.get_cmap('plasma', 256)
    labels = []
    ylabs = []
    treat_order.reverse()
    PRC_ASV_LCPB = ['ASV31', 'ASV11', 'ASV81', 'ASV3', 'ASV6', 'ASV19', 'ASV12']
    PRC_ASV_BHET = ['ASV48', 'ASV97', 'ASV49', 'ASV22', 'ASV88', 'ASV92', 'ASV7', 'ASV100', 'ASV14', 'ASV86']
    tax_order = []
    for b in range(len(treat_order)):
        for c in range(len(tax)):
            if treat_order[b][0] == tax[c][0]:
                if tax[c][4] != 'NA':
                    tax_order.append(tax[c][4])
                else:
                    tax_order.append('Other')
        if treat_order[b][0] != 'Group':
            beg, end = '', ''
            for c in range(len(unique_to_trt)):
                if unique_to_trt[c] == int(treat_order[b][0][3:]):
                    beg = r'$\bf{'
                    end = '}$'
            treat_order[b][0] = beg+'ASV'+str(int(treat_order[b][0][3:]))+end
        for c in range(len(PRC_ASV_LCPB)):
            if PRC_ASV_LCPB[c] == treat_order[b][0]:
                treat_order[b][0] += '**'
        for d in range(len(PRC_ASV_BHET)):
            if PRC_ASV_BHET[d] == treat_order[b][0]:
                treat_order[b][0] += '*'
    """
    unique_tax = []
    for b in range(len(tax_order)):
        adding = True
        for c in range(len(unique_tax)):
            if tax_order[b] == unique_tax[c]:
                adding = False
        if adding:
            unique_tax.append(tax_order[b])
        adding = True
        for c in range(len(all_unique_tax)):
            if tax_order[b] == all_unique_tax[c]:
                adding = False
        if adding:
            all_unique_tax.append(tax_order[b])
    """
    #print(unique_tax)
    this_tax_color = []
    for b in range(len(tax_order)):
        for c in range(len(all_unique_tax)):
            if tax_order[b] == all_unique_tax[c]:
                this_tax_color.append(tax_colors[c])
    if omi == 0: omi = 0.001
    alphas = [1, 1, 1, 1, 1, 1, 1, 1, 0.7]
    for c in range(0, len(treat_order)-1):
        norm = mpl.colors.Normalize(vmin=min(treat_order[c][1:]), vmax=max(treat_order[c][1:]))
        #norm = mpl.colors.LogNorm(vmin=omi, vmax=oma)
        ma = max(treat_order[c][1:])
        m = mpl.cm.ScalarMappable(norm=norm, cmap=colormap)
        abundance = []
        for d in range(1, len(treat_order[c])):
            abundance.append(str(round(treat_order[c][d], 2)))
            treat_order[c][d] = m.to_rgba(treat_order[c][d])
        treat_order[c].append(this_tax_color[c])
        ax.bar(x[:-1], y[:-1], bottom=bottom[:-1], color=treat_order[c][1:-1], width=width[:-1], edgecolor='gray')
        ax.bar(x[-1], y[-1], bottom=bottom[-1], color=treat_order[c][-1], width=width[-1], edgecolor='k', alpha=0.7)
        ax.text(44, bottom[-1]+0.5, tax_order[c][0], ha='center', va='center')
        """
        for e in range(6, len(abundance)):
            ax.text(x[e], bottom[-1]+0.5, abundance[e], ha='center', va='center')
        """
        #ax.scatter(43.5, bottom[-1]+0.5, marker='o', color='k', s=ma*5)
        #ax1.plot(x+[10], bottom+[bottom[-1]], 'k-')
        ylabs.append(bottom[-1]+0.5)
        labels.append(treat_order[c][0])
        for d in range(len(bottom)):
            bottom[d] += 1
        #ax1.plot(x+[10], bottom+[bottom[-1]], 'k-')
    plt.sca(ax)
    plt.xlim([0.5, 45.5])
    plt.ylim([0, bottom[-1]])
    plt.yticks(ylabs, labels)
    plt.xticks(xlab, xtxt)
    plt.xlabel('Day')
    ax.yaxis.tick_right()
    plt.title(titles[a], fontweight='bold')
    plt.title(letter[a], loc='left')
    labels.reverse()
    #print(name, '=', labels)

#print(all_unique_tax)
  
tax_colors.reverse()
all_unique_tax.reverse()
    
ylabs = []
ytxt = []
for a in range(len(all_unique_tax)):
    ax7.bar([0.5], [1], width=[1], color=[tax_colors[a]], bottom=[a-1], edgecolor='k', alpha=0.7)
    ax7.text(0.5, a-0.5, all_unique_tax[a][0], ha='center', va='center')
    ylabs.append(a-0.5)
    ytxt.append(all_unique_tax[a])
ax7.set_ylim([-1, len(all_unique_tax)-1])
ax7.set_xlim([0,1])
ax7.yaxis.tick_right()
plt.sca(ax7)
plt.yticks(ylabs, ytxt)
plt.xticks([])

plt.subplots_adjust(hspace=1)
plt.savefig('Overall fig order abundance.png', dpi=300, bbox_inches='tight')
plt.close()
