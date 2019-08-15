import numpy
import matplotlib.pyplot as plt
import csv
import matplotlib as mpl
from matplotlib import rcParams
import math

with open('BasicIR_Wavenumbers.csv', 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row[0])
del rows[0]

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
    #plt.xlim([min(rows), max(rows)])

axis = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10, ax11, ax12]
files = [['DT13_LCNeg1_2019-06-04T15-59-48.asp', 'DT13_LCNeg2_2019-06-04T16-05-00.asp', 'DT13_LCNeg3_2019-06-04T16-08-50.asp'],
         ['DT14_LCNeg1_2019-06-04T16-17-14.asp', 'DT14_LCNeg2_2019-06-04T16-16-49.asp', 'DT14_LCNeg3_2019-06-04T16-15-04.asp'],
         ['DT15_LCNeg1_2019-06-04T16-18-14.asp', 'DT15_LCNeg2_2019-06-04T16-19-04.asp', 'DT15_LCNeg3_2019-06-04T16-19-47.asp'],
         ['DT16_LCB4_1_2019-06-04T16-27-56.asp', 'DT16_LCB4_2_2019-06-04T16-27-08.asp', 'DT16_LCB4_3_2019-06-04T16-26-19.asp'],
         ['DT17_LCB4_1_2019-06-04T16-28-55.asp', 'DT17_LCB4_2_2019-06-04T16-29-51.asp', 'DT17_LCB4_3_2019-06-04T16-30-34.asp'],
         ['DT18_LCB4_1_2019-06-04T16-36-01.asp', 'DT18_LCB4_2_2019-06-04T16-35-21.asp', 'DT18_LCB4_3_2019-06-04T16-34-38.asp'],
         ['DT19_LCB6_1_2019-06-04T16-37-08.asp', 'DT19_LCB6_2_2019-06-04T16-37-46.asp', 'DT19_LCB6_3_2019-06-04T16-38-27.asp'],
         ['DT20_LCB6_1_2019-06-04T16-40-45.asp', 'DT20_LCB6_2_2019-06-04T16-40-04.asp', 'DT20_LCB6_3_2019-06-04T16-39-21.asp'],
         ['DT21_LCB6_1_2019-06-04T16-41-39.asp', 'DT21_LCB6_2_2019-06-04T16-42-18.asp', 'DT21_LCB6_3_2019-06-04T16-43-00.asp'],
         ['DT22_LCComm_1_2019-06-04T16-45-52.asp', 'DT22_LCB6_2_2019-06-04T16-45-11.asp', 'DT22_LCComm_3_2019-06-04T16-43-54.asp'],
         ['DT23_LCComm_1_2019-06-04T16-46-50.asp', 'DT23_LCComm_2_2019-06-04T16-47-27.asp', 'DT23_LCComm_3_2019-06-04T16-48-12.asp'],
         ['DT24_LCComm_1_2019-06-04T16-50-21.asp', 'DT24_LCComm_2_2019-06-04T16-49-46.asp', 'DT24_LCComm_3_2019-06-04T16-49-10.asp']]
colors = ['r', 'b', 'g']

for a in range(len(axis)):
    for b in range(3):
        with open(files[a][b], 'rU') as f:
            nums = []
            for row in f:
                nums.append(float(row))
        del nums[:6]
    axis[a].plot(rows, nums, color=colors[b])

plt.savefig('Test plot.png')


"""
with open('DT13_LCNeg1_2019-06-04T15-59-48.asp', 'rU') as f:
    nums = []
    for row in f:
        nums.append(float(row))

del nums[:6]

plt.plot(rows, nums)
plt.savefig('Test.png')
"""
