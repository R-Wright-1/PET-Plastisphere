import csv
import matplotlib.pyplot as plt
import numpy
from scipy import stats

#This should be run three times, for each of the sets of filenames, save names and letters, and the printed numbers should be used for the ratios_plot.py test
fn, sn, letter = 'DT_LC_edit.csv', 'Degradation test low crystallinity', 'A'
#fn, sn, letter = 'DT_WPET.csv', 'Degradation test WPET', 'B'
#fn, sn, letter = 'DT_PET.csv', 'Degradation test PET', 'C'


with open(fn, 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)

def transpose(rows):
    cols = []
    for a in range(len(rows[0])):
        col = []
        for b in range(len(rows)):
            col.append(rows[b][a])
        cols.append(col)
    return cols

xplt = []
for a in range(1, len(rows)):
    for b in range(len(rows[a])):
        if b == 0:
            rows[a][b] = round(float(rows[a][b]))
            xplt.append(rows[a][b])
        else:
            rows[a][b] = float(rows[a][b])

plt.figure(figsize=(10,12))
ax1 = plt.subplot(431)
ax2, ax3 = plt.subplot(432, sharey=ax1), plt.subplot(433, sharey=ax1)
ax4, ax5, ax6 = plt.subplot(434, sharey=ax1), plt.subplot(435, sharey=ax1), plt.subplot(436, sharey=ax1)
ax7, ax8, ax9 = plt.subplot(437, sharey=ax1), plt.subplot(438, sharey=ax1), plt.subplot(439, sharey=ax1)
ax10, ax11, ax12 = plt.subplot(4,3,10, sharey=ax1), plt.subplot(4,3,11, sharey=ax1), plt.subplot(4,3,12, sharey=ax1)

rmy = [ax2, ax3, ax5, ax6, ax8, ax9, ax11, ax12]
rmx = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9]

for y in rmy:
    plt.sca(y)
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False, labelright=False)
for x in rmx:
    plt.sca(x)
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

axis = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10, ax11, ax12]
new_axis = []
for a in range(len(axis)):
    for b in range(3):
        new_axis.append(axis[a])

labels = rows[0]   
del labels[0]  
del rows[0]
rows = transpose(rows)
del rows[0]
for a in range(len(rows)):
    new_axis[a].plot(xplt, rows[a])
    plt.sca(new_axis[a])
    plt.xticks([500, 1000, 1500, 2000, 2500, 3000, 3500, 4000])
    plt.xlim([4000, 500])
    plt.title(labels[a])
    plt.ylabel('Transmittance (%)')
    plt.xlabel('Wavenumber (cm$^{-1}$)')

plt.savefig('raw_plots/'+sn+'.png')
plt.close()
means = []
mean_labels = []
for a in range(len(rows)):
    if (a+1)%3==0:
        this_mean = []
        for b in range(len(rows[a])):
            this_mean.append(numpy.mean([rows[a][b], rows[a-1][b], rows[a-2][b]]))
        means.append(this_mean)
        mean_labels.append(labels[a])

for a in range(len(means)):
    zero = means[a][0]
    for b in range(len(means[a])):
        means[a][b] = (means[a][b]-zero)*(-1)

plt.figure(figsize=(10,12))
ax1 = plt.subplot(431)
ax2, ax3 = plt.subplot(432, sharey=ax1), plt.subplot(433, sharey=ax1)
ax4, ax5, ax6 = plt.subplot(434, sharey=ax1), plt.subplot(435, sharey=ax1), plt.subplot(436, sharey=ax1)
ax7, ax8, ax9 = plt.subplot(437, sharey=ax1), plt.subplot(438, sharey=ax1), plt.subplot(439, sharey=ax1)
ax10, ax11, ax12 = plt.subplot(4,3,10, sharey=ax1), plt.subplot(4,3,11, sharey=ax1), plt.subplot(4,3,12, sharey=ax1)

rmy = [ax2, ax3, ax5, ax6, ax8, ax9, ax11, ax12]
rmx = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9]

for y in rmy:
    plt.sca(y)
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False, labelright=False)
for x in rmx:
    plt.sca(x)
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

axis = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10, ax11, ax12]

y = [-60, -50, -40, -30, -20, -10, 0]
ylab = [40, 50, 60, 70, 80, 90, 100]

mean_labels = ['Control 1', 'Control 2', 'Control 3', 'Thioclava 1', 'Thioclava 2', 'Thioclava 3', 'Bacillus 1', 'Bacillus 2', 'Bacillus 3', 'Community 1', 'Community 2', 'Community 3']

for a in range(len(means)):
    axis[a].plot(xplt, means[a])
    plt.sca(axis[a])
    plt.xticks([500, 1000, 1500, 2000, 2500, 3000, 3500, 4000])
    plt.xlim([4000, 500])
    plt.title(mean_labels[a])
    #plt.yticks(y, ylab)
    plt.ylabel('Absorbance (%)')
    plt.xlabel('Wavenumber (cm$^{-1}$)')

plt.tight_layout()
plt.savefig('raw_plots/'+sn+' mean.png')
plt.close()

"""
means_1340, means_1410 = [], []

for a in range(len(means)):
   for b in range(len(means[a])):
        if xplt[b] == 1340:
            means_1340.append(means[a][b])
        elif xplt[b] == 1410 or xplt[b] == 1411:
            means_1410.append(means[a][b])

ratio = []
for a in range(len(means_1340)):
    ratio.append(means_1410[a]/means_1340[a])

means_rat, stds = [], []
for a in range(len(ratio)):
    if (a+1)%3 == 0:
        this_rat = [ratio[a], ratio[a-1], ratio[a-2]]
        means_rat.append(numpy.mean(this_rat))
        stds.append(numpy.std(this_rat))

labels = ['Control', r'$Thioclava$', r'$Bacillus$', 'Community']
x = [1,2,3,4]
ax1 = plt.subplot(111)
for a in range(len(x)):
    ax1.bar(x[a], means_rat[a], yerr=stds[a], label=labels[a])

plt.savefig('1340 1410 ratio.png')
plt.close()
"""
ref = 2501
bonds = ['C=O\n1710 cm$^{-1}$\ncarboxylic acid', 'OH\n2920 cm$^{-1}$\ncarboxylic acid', 'C-O\n1235 cm$^{-1}$\ncarboxylic acid', 'O-H\n3300 cm$^{-1}$\nalcohol', 'C-O\n1090 cm$^{-1}$\nalcohol']
waves = [1711, 2920, 1236, 3301, 1090]
ratios = []
ref_waves = []

for a in range(len(means)):
   for b in range(len(means[a])):
        if xplt[b] == ref:
            ref_waves.append(means[a][b])

for a in range(len(waves)):
    this_wave = []
    for b in range(len(means)):
        for c in range(len(means[b])):
            if xplt[c] == waves[a]:
                this_wave.append(means[b][c])
    for c in range(len(this_wave)):
        this_wave[c] = this_wave[c]-ref_waves[c]
        #this_wave[c] = this_wave[c]/abs(ref_waves[c])
    ratios.append(this_wave)

ttests = []
mean_ratios, std_ratios = [], []
for a in range(len(ratios)):
    this_mean, this_std = [], []
    ttest = ['']
    for b in range(len(ratios[a])):
        if (b+1)%3==0:
            this_ratio = [ratios[a][b], ratios[a][b-1], ratios[a][b-2]]
            this_mean.append(numpy.mean(this_ratio))
            this_std.append(numpy.std(this_ratio))
            if b == 2:
                cont = this_ratio
            else:
                t = stats.ttest_ind(cont, this_ratio)
                if t[1] <= 0.05:
                    ttest.append('*')
                else:
                    ttest.append('')
    ttests.append(ttest)
    mean_ratios.append(this_mean)
    std_ratios.append(this_std)

x = [1, 2, 3, 4]
xplc = 2.5
xlabs = []
ax1 = plt.subplot(111)
labels = ['Control', r'$Thioclava$ sp. BHET1', r'$Bacillus$ sp. BHET2', 'Community']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
for a in range(len(mean_ratios)):
    if a == 0:
        for b in range(len(mean_ratios[a])):
            ax1.bar(x[b], mean_ratios[a][b], yerr=std_ratios[a][b], capsize=2, label=labels[b], color=colors[b], width=0.8)
    else:
        ax1.bar(x, mean_ratios[a], yerr=std_ratios[a], capsize=2, color=colors, width=0.8)
    ttxt = []
    for b in range(len(mean_ratios[a])):
        ttxt.append(mean_ratios[a][b]+std_ratios[a][b]+0.5)
    for b in range(len(ttxt)):
        ax1.text(x[b], ttxt[b], ttests[a][b], ha='center', va='bottom')
    for b in range(len(x)):
        x[b] += 5
    xlabs.append(xplc)
    xplc += 5
plt.sca(ax1)
plt.ylabel('Ratio between wavelengths')
plt.title(letter, loc='left')
plt.xticks(xlabs, bonds)
ax1.legend()
print(mean_ratios, std_ratios, ttests)

plt.tight_layout()
plt.savefig('raw_plots/'+sn+' bonds.png', dpi=300)
plt.close()

    
mean_trt = []
for a in range(len(means)):
    if (a+1)%3==0:
        this_mean = []
        for b in range(len(means[a])):
            this_mean.append(numpy.mean([means[a][b], means[a-1][b], means[a-2][b]]))
        mean_trt.append(this_mean)


plt.figure(figsize=(10,12))
ax1 = plt.subplot2grid((4,2), (0,0), colspan=2, rowspan=2)
ax2, ax3, ax4, ax5 = plt.subplot(425), plt.subplot(426), plt.subplot(427), plt.subplot(428)
axis = [ax1, ax2, ax3, ax4, ax5]



for a in range(len(mean_trt)):
    for b in range(len(axis)):
        axis[b].plot(xplt, mean_trt[a], label=labels[a])
        plt.sca(axis[b])
        #plt.yticks(y, ylab)
        plt.ylabel('Absorbance (%)')
        plt.xlabel('Wavenumber (cm$^{-1}$)')

ax1.set_title('A', loc='left')
ax2.set_title('B', loc='left')
ax3.set_title('C', loc='left')
ax4.set_title('D', loc='left')
ax5.set_title('E', loc='left')

plt.sca(ax1)
plt.xlim(4000,500)
plt.xticks([500, 1000, 1500, 2000, 2500, 3000, 3500, 4000])

plt.sca(ax2)
plt.xlim(1000,650)
plt.xticks([700, 800, 900, 1000])

plt.sca(ax3)
plt.xlim([1200,1000])
plt.xticks([1000, 1040, 1080, 1120, 1160, 1200])

plt.sca(ax4)
plt.xlim([1600, 1200])
plt.xticks([1200, 1300, 1400, 1500, 1600])

plt.sca(ax5)
plt.xlim([1800, 1600])
plt.xticks([1600, 1640, 1680, 1720, 1760, 1800])


ax1.legend()
plt.tight_layout()
plt.savefig(sn+' treatment mean.png', dpi=300)
plt.close()