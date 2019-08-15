import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
#import numpy
import matplotlib
#from matplotlib.mlab import bivariate_normal

cs, cf = [2, 9, 16, 23, 30, 37], [9, 16, 23, 30, 37, 44]
with open('Taxonomy.csv', 'rU') as f:
    this_tax = []
    for row in csv.reader(f):
        this_tax.append(row)

plt.figure(figsize=(16,20))
ax1 = plt.subplot2grid((43,15), (2,0), colspan=4, rowspan=19)
ax2 = plt.subplot2grid((43,15), (2,5), colspan=4, rowspan=19)
ax3 = plt.subplot2grid((43,15), (2,10), colspan=4, rowspan=19)
ax4 = plt.subplot2grid((43,15), (23,0), colspan=4, rowspan=19)
ax5 = plt.subplot2grid((43,15), (23,5), colspan=4, rowspan=19)
ax6 = plt.subplot2grid((43,15), (23,10), colspan=4, rowspan=19)

axcolbar = plt.subplot2grid((43,15), (0,5), colspan=4)
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

axis = [ax6, ax1, ax2, ax3, ax4, ax5]
titles = ['No carbon', 'BHET', 'Amorphous PET biofilm', 'Amorphous PET\nplanktonic', 'PET powder', 'Weathered PET powder']
letter = ['F', 'A', 'B', 'C', 'D', 'E']
lim = 0.49

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
    bottom = [0, 0, 0, 0, 0, 0, 0, 0]
    y = [1, 1, 1, 1, 1, 1, 1, 1]
    x = [0, 1, 2.5, 5.5, 11, 18, 26, 36.5]
    width = [1, 1, 2, 4, 7, 7, 9, 12]
    xlab = [1, 3, 7, 14, 21, 30, 42]
    
    xtxt = ['1', '3', '7', '14', '21', '30', '42']
    colormap = mpl.cm.get_cmap('plasma', 256)
    labels = []
    ylabs = []
    treat_order.reverse()
    PRC_ASV_LCPB = ['ASV31', 'ASV11', 'ASV81', 'ASV3', 'ASV6', 'ASV19', 'ASV12']
    PRC_ASV_BHET = ['ASV48', 'ASV97', 'ASV49', 'ASV22', 'ASV88', 'ASV92', 'ASV7', 'ASV100', 'ASV14', 'ASV86']
    for b in range(len(treat_order)):
        if treat_order[b][0] != 'Group':
            treat_order[b][0] = 'ASV'+str(int(treat_order[b][0][3:]))
        for c in range(len(PRC_ASV_LCPB)):
            if PRC_ASV_LCPB[c] == treat_order[b][0]:
                treat_order[b][0] += '**'
        for d in range(len(PRC_ASV_BHET)):
            if PRC_ASV_BHET[d] == treat_order[b][0]:
                treat_order[b][0] += '*'
        """
        for c in range(len(tax)):
            if treat_order[b][0] == tax[c][0]:
                treat_order[b][0] = 'ASV'+str(int(treat_order[b][0][3:]))+': '
                del tax[c][0]
                tax[c].reverse()
                for d in range(len(tax[c])):
                    if tax[c][d] != 'NA':
                        if d == 0:
                            tax[c] = '$'+tax[c][d+1]+'$ $'+tax[c][d]+'$'
                        elif d == 1:
                            tax[c] = '$'+tax[c][d]+'$'
                        else:
                            tax[c] = tax[c][d]
                        break
                treat_order[b][0] += tax[c]
        """
    if omi == 0: omi = 0.001
    for c in range(0, len(treat_order)-1):
        norm = mpl.colors.Normalize(vmin=min(treat_order[c][1:]), vmax=max(treat_order[c][1:]))
        #norm = mpl.colors.LogNorm(vmin=omi, vmax=oma)
        ma = max(treat_order[c][1:])
        m = mpl.cm.ScalarMappable(norm=norm, cmap=colormap)
        for d in range(1, len(treat_order[c])):
            treat_order[c][d] = m.to_rgba(treat_order[c][d])
        ax.bar(x, y, bottom=bottom, color=treat_order[c][1:], width=width, edgecolor='gray')
        ax.scatter(43.5, bottom[-1]+0.5, marker='o', color='k', s=ma*5)
        #ax1.plot(x+[10], bottom+[bottom[-1]], 'k-')
        ylabs.append(bottom[-1]+0.5)
        labels.append(treat_order[c][0])
        for d in range(len(bottom)):
            bottom[d] += 1
        #ax1.plot(x+[10], bottom+[bottom[-1]], 'k-')
    plt.sca(ax)
    plt.xlim([0.5, 42.5])
    plt.ylim([0, bottom[-1]])
    plt.yticks(ylabs, labels)
    plt.xticks(xlab, xtxt)
    plt.xlabel('Day')
    ax.yaxis.tick_right()
    plt.title(titles[a], fontweight='bold')
    plt.title(letter[a], loc='left')
    labels.reverse()
    #print(name, '=', labels)
plt.subplots_adjust(hspace=1)
plt.savefig('Overall fig.png', dpi=300, bbox_inches='tight')
plt.close()
