import matplotlib.pyplot as plt
import csv

with open('Raw_plastics2.csv', 'rU') as f:
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

ax1 = plt.subplot(111)
#y = [20, 30, 40]
#ylab = [20, 30, 40, 50, 60, 70, 80, 90, 100]

for c in range(len(cols)):
    ax1.plot(x, cols[c], label=labels[c])
    plt.sca(ax1)
    plt.xticks([500, 1000, 1500, 2000, 2500, 3000, 3500, 4000], rotation=90)
    plt.xlim([4000, 500])
    plt.ylabel('Transmittance (%)')
    plt.xlabel('Wavenumber (cm$^{-1}$)')
    #plt.yticks(y, ylab)

ax1.legend()
plt.tight_layout()
plt.savefig('Raw plastics.png', dpi=300)