import matplotlib.pyplot as plt
import csv
import numpy

with open('Raw_plastics.csv', 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)
        
x = []
labels = rows[0][1:]
del rows[0]
for a in range(len(rows)):
    for b in range(len(rows[a])):
        if b == 0:
            x.append(round(float(rows[a][b]), 0))
        else:
            rows[a][b] = round(float(rows[a][b]), 2)

cols = []
for a in range(1, len(rows[0])):
    col = []
    for b in range(len(rows)):
        col.append(rows[b][a])
    cols.append(col)

for b in range(len(cols)):
    zero = cols[b][0]
    for c in range(len(cols[b])):
        cols[b][c] = (cols[b][c]-zero)*(-1)

new_x = [[], [], []]  
for a in range(len(cols[0])):
    this_x = []
    count = 0
    for b in range(len(cols)):
        this_x.append(cols[b][a])
        if (b+1)%9==0:
            new_x[count].append(numpy.mean(this_x))
            this_x = []
            count += 1
            

plt.figure(figsize=(10,12))
ax1 = plt.subplot2grid((4,2), (0,0), colspan=2, rowspan=2)
ax2, ax3, ax4, ax5 = plt.subplot(425), plt.subplot(426), plt.subplot(427), plt.subplot(428)
axis = [ax1, ax2, ax3, ax4, ax5]
#y = [20, 30, 40]
#ylab = [20, 30, 40, 50, 60, 70, 80, 90, 100]
cols = new_x
labels = ['Amorphous PET', 'PET powder', 'Weathered PET powder']

for c in range(len(cols)):
    for d in range(len(axis)):
        axis[d].plot(x, cols[c], label=labels[c])
        plt.sca(axis[d])
        plt.ylabel('Absorbance (%)')
        plt.xlabel('Wavenumber (cm$^{-1}$)')
        #plt.yticks(y, ylab)

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
plt.savefig('Raw plastics.png', dpi=600)