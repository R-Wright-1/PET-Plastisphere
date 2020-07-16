#isolate growth
import matplotlib.pyplot as plt
import numpy
import csv
from colorsys import hls_to_rgb
import random
from matplotlib.lines import Line2D

f = '13-7-18_16-7-18.csv'

with open(f, 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)
control, b1, b2, b3, times, time = [], [], [], [], [], 0
del rows[0:26]
for a in range(len(rows[0])):
    if a > 2:
        this_rep = []
        for b in range(144):
            if a == 5:
                times.append(time)
                time += 0.5
            this_rep.append(float(rows[b][a]))
        if 2 < a < 30:
            b1.append(this_rep)
        elif 29 < a < 57:
            b2.append(this_rep)
        elif 56 < a < 84:
            b3.append(this_rep)
        elif a < 100:
            control.append(this_rep)
            
    
def get_distinct_colors(n):
    colors = []
    for i in numpy.arange(0., 360., 360. / n):
        h = i / 360.
        l = (50 + numpy.random.rand() * 10) / 100.
        s = (90 + numpy.random.rand() * 10) / 100.
        colors.append(hls_to_rgb(h, l, s))
    random.shuffle(colors)
    return colors

def sep_plots(bac, name, colors, title, ax):
    names = ['No carbon', 'Glucose', 'Succinate', 'Fructose', 'Pyruvate', 'Glycerol', 'GlcNAc', 'Marine broth']
    xlabels = [0, 24, 48, 72]
    count = 0
    for a in range(len(bac)):
        if count > 7: continue
        n = a % 3
        if n == 2:
            ax[n].plot(times, bac[a], color=colors[count], label=names[count])
            count += 1
        else:
            ax[n].plot(times, bac[a], color=colors[count])
        ax[n].set_xticks(xlabels)
    label = title+'\n Absorbance (600 nm)'
    ax[0].set_ylabel(label)    
    ax[1].set_xlabel('Hours')
    plt.setp(ax[1].get_yticklabels(), visible=False)
    plt.setp(ax[2].get_yticklabels(), visible=False)
    #plt.tight_layout()
    #plt.savefig(name+'.pdf', bbox_inches='tight')
    #plt.close()
    return names

plt.figure(figsize=(9,6))
ax1 = plt.subplot(231)
ax2 = plt.subplot(232, sharey=ax1)
ax3 = plt.subplot(233, sharey=ax1)
ax4 = plt.subplot(234)
ax5 = plt.subplot(235, sharey=ax4)
ax6 = plt.subplot(236, sharey=ax4)

#colors = ['k']+get_distinct_colors(8)
colors = ['k', '#e6194B', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#469990', '#dcbeff']
ax = [ax1, ax2, ax3]
names = sep_plots(b1, 'Bac 1 jul', colors, r'$Thioclava$ sp. BHET1', ax)
lines = [Line2D([0], [0], color=c, linewidth=2) for c in colors]
ax[2].legend(lines, names, bbox_to_anchor=(1.1,1.05))
ax[0].set_title('A', loc='left')
ax[1].set_title('B', loc='left')
ax[2].set_title('C', loc='left')
ax = [ax4, ax5, ax6]
sep_plots(b2, 'Bac 2 jul', colors, r'$Bacillus$ sp. BHET2', ax)
ax[0].set_title('D', loc='left')
ax[1].set_title('E', loc='left')
ax[2].set_title('F', loc='left')

plt.tight_layout()
plt.savefig('Both plots.png', dpi=600, bbox_inches='tight')