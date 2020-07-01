import csv
import numpy
import matplotlib.pyplot as plt
import matplotlib as mpl

with open('over_time_all.csv', 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)

new_rows = [rows[0]]
for a in range(1, len(rows)):
    for b in range(1, len(rows[a])):
        rows[a][b] = float(rows[a][b])
    if max(rows[a][1:]) > 0:
        new_rows.append(rows[a])

def transpose(new_rows):
    cols = []
    for a in range(len(new_rows[0])):
        col = []
        for b in range(len(new_rows)):
            col.append(new_rows[b][a])
        cols.append(col)
    return cols
cols = transpose(new_rows)

def get_diversity(diversity, sample):
    for a in range(len(sample)):
        sample[a] = float(sample[a])
    total = sum(sample)
    if diversity == 'Simpsons':
        for b in range(len(sample)):
            sample[b] = (sample[b]/total)**2
        simpsons = 1-(sum(sample))
        return simpsons
    elif diversity == 'Shannon':
        for b in range(len(sample)):
            sample[b] = (sample[b]/total)
            if sample[b] != 0:
                sample[b] = -(sample[b] * (numpy.log(sample[b])))
        shannon = sum(sample)
        return shannon
    elif diversity == 'Richness':
        rich = 0
        for b in range(len(sample)):
            if sample[b] != 0:
                rich += 1
        return rich
    elif diversity == 'Evenness':
        for b in range(len(sample)):
            sample[b] = (sample[b]/total)
            if sample[b] != 0:
                sample[b] = -(sample[b] * (numpy.log(sample[b])))
        shannon = sum(sample)
        rich = 0
        for b in range(len(sample)):
            if sample[b] != 0:
                rich += 1
        even = shannon/(numpy.log(rich))
        return even
    return

measures = ['Simpsons', 'Shannon', 'Richness', 'Evenness']
cs, cf = [1, 8, 15, 22, 29, 36], [8, 15, 22, 29, 36, 43]
div_files = []
for a in range(4):
    diversity = []
    for b in range(1, len(cols)):
        col = [cols[b][0]]
        sample = cols[b][1:]
        div = get_diversity(measures[a], sample)
        col.append(div)
        diversity.append(col)
    diversity = transpose(diversity)
    with open('Diversity '+measures[a]+'.csv', 'w') as f:
        writer = csv.writer(f)
        for row in diversity:
            writer.writerow(row)
    div_files.append('Diversity '+measures[a]+'.csv')

for a in range(4):
    with open(div_files[a], 'rU') as f:
        rows = []
        for row in csv.reader(f):
            rows.append(row)
    for b in range(len(rows[1])):
        rows[1][b] = float(rows[1][b])
    plt.figure(figsize=(8,6))
    ax1 = plt.subplot2grid((12,8), (5,0), rowspan=2)
    ax2 = plt.subplot2grid((6,8), (0,2), colspan=6)
    ax3 = plt.subplot2grid((6,8), (1,2), colspan=6)
    ax4 = plt.subplot2grid((6,8), (2,2), colspan=6)
    ax5 = plt.subplot2grid((6,8), (3,2), colspan=6)
    ax6 = plt.subplot2grid((6,8), (4,2), colspan=6)
    ax7 = plt.subplot2grid((6,8), (5,2), colspan=6)
    
    cmap = 'Blues'
    norm = mpl.colors.Normalize(vmin=min(rows[1]), vmax=max(rows[1]))
    colormap = mpl.cm.get_cmap(cmap, 256)
    m = mpl.cm.ScalarMappable(norm=norm, cmap=colormap)
    colors = []
    for b in range(len(rows[1])):
        colors.append(m.to_rgba(rows[1][b]))
    x, y = [1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1, 1]
    split = []
    ax1.bar([1], [1], color=colors[0], width=1, edgecolor='k')
    split.append([rows[1][0]])
    ax2.bar(x, y, color=colors[cs[0]:cf[0]], width=1, edgecolor='k')
    split.append(rows[1][cs[0]:cf[0]])
    ax3.bar(x, y, color=colors[cs[1]:cf[1]], width=1, edgecolor='k')
    split.append(rows[1][cs[1]:cf[1]])
    ax4.bar(x, y, color=colors[cs[2]:cf[2]], width=1, edgecolor='k')
    split.append(rows[1][cs[2]:cf[2]])
    ax5.bar(x, y, color=colors[cs[3]:cf[3]], width=1, edgecolor='k')
    split.append(rows[1][cs[3]:cf[3]])
    ax6.bar(x, y, color=colors[cs[4]:cf[4]], width=1, edgecolor='k')
    split.append(rows[1][cs[4]:cf[4]])
    ax7.bar(x, y, color=colors[cs[5]:cf[5]], width=1, edgecolor='k')
    split.append(rows[1][cs[5]:cf[5]])
    
    ax = [ax1, ax2, ax3, ax4, ax5, ax6, ax7]
    titles = ['Inoculum', 'No carbon', 'planktonic', 'biofilm', 'PET\npowder', 'Weathered\nPET\npowder', 'BHET']
    ax3.text(-0.01, -0.08, 'Amorphous PET', va='center', ha='center', rotation=90)
    
    for b in range(len(split)):
        for c in range(len(split[b])):
            if split[b][c] == max(rows[1]):
                col = 'w'
            else:
                col = 'k'
            txt = round(split[b][c], 2)
            ax[b].text(x[c], 0.5, str(txt), ha='center', va='center', color=col)
    
    for x in range(len(ax)):
        y = ax[x]
        plt.sca(y)
        plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False, labelright=False)
        if y != ax7:
            plt.tick_params(axis='x', which='both', top=False, bottom=False, labeltop=False, labelbottom=False)
        y.set_ylim([0,1])
        if y != ax1:
            y.set_xlim([0.5, 7.5])
        else:
            y.set_xlim([0.5, 1.5])
        y.set_ylabel(titles[x])
    plt.sca(ax7)
    plt.xticks([1, 2, 3, 4, 5, 6, 7], ['1', '3', '7', '14', '21', '30', '42'])
    plt.savefig(div_files[a][:-4]+'.png', bbox_inches='tight', dpi=600)
    plt.close()