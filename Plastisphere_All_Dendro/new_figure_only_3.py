import csv
import numpy
import matplotlib.pyplot as plt
import matplotlib
import matplotlib as mpl
from scipy.cluster import hierarchy
from operator import add

def transpose(rows):
    cols = []
    for a in range(len(rows[0])):
        col = []
        for b in range(len(rows)):
            col.append(rows[b][a])
        cols.append(col)
    return cols

with open('Treatment1_All_percent.csv', 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)

cols = transpose(rows)
names = ['Day00Inoc', 'Day01NoC', 'Day03NoC', 'Day07NoC', 'Day14NoC', 'Day21NoC', 'Day30NoC', 'Day42NoC', 'Day01LowCrysWater', 'Day03LowCrysWater', 'Day07LowCrysWater', 'Day14LowCrysWater', 'Day21LowCrysWater', 'Day30LowCrysWater', 'Day42LowCrysWater', 'Day01LowCrys', 'Day03LowCrys', 'Day07LowCrys', 'Day14LowCrys', 'Day21LowCrys', 'Day30LowCrys', 'Day42LowCrys', 'Day01PET', 'Day03PET', 'Day07PET', 'Day14PET', 'Day21PET', 'Day30PET', 'Day42PET', 'Day01WeatherPET', 'Day03WeatherPET','Day07WeatherPET', 'Day14WeatherPET', 'Day21WeatherPET', 'Day30WeatherPET', 'Day42WeatherPET', 'Day01BHET', 'Day03BHET', 'Day07BHET', 'Day14BHET', 'Day21BHET', 'Day30BHET', 'Day42BHET']
grouped = [cols[0]]

for a in range(len(names)):
    if names[a][5:] != 'ExtractionContro' and names[a] != 'MiSeqControl':
        this_group = []
        for b in range(len(cols)):
            if cols[b][0][:-1] == names[a]:
                this_group.append(cols[b])
        group_mean = [this_group[0][0][:-1]]
        for c in range(1, len(this_group[0])):
            nums = []
            for d in range(len(this_group)):
                nums.append(float(this_group[d][c]))
            if min(nums) > 0:
                group_mean.append(numpy.mean(nums))
            else:
                group_mean.append(0)
        grouped.append(group_mean)
rows = transpose(grouped)

"""
with open('over_time_all.csv', 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)
ASV_order = ["ASV000028", "ASV000007", "ASV000153", "ASV004528", "ASV000145", "ASV000203", "ASV000052", "ASV000041", 
"ASV000061", "ASV000057", "ASV000005", "ASV000079", "ASV004313", "ASV000068", "ASV000038",
"ASV000066", "ASV000032", "ASV000042", "ASV000010", "ASV000014", "ASV000016", "ASV000022",
"ASV000074", "ASV000064", "ASV000085", "ASV000035", "ASV000056", "ASV000030", "ASV000051",
"ASV000046", "ASV006228", "ASV000009", "ASV000045", "ASV000034", "ASV000054", "ASV000027",
"ASV000058", "ASV000024", "ASV000050", "ASV000047", "ASV000067", "ASV000036", "ASV000060",
"ASV000025", "ASV000772", "ASV000044", "ASV000059", "ASV000037", "ASV000033", "ASV000082",
"ASV017996", "ASV000015", "ASV000008", "ASV000020", "ASV000043", "ASV000049", "ASV000018",
"ASV000062", "ASV000011", "ASV000040", "ASV000026", "ASV000003", "ASV000076", "ASV000002",
"ASV000031", "ASV001733", "ASV000012", "ASV000021", "ASV000006", "ASV000063", "ASV000075", "ASV000053",
"ASV000023", "ASV000004", "ASV000013", "ASV000001", "ASV000017", "ASV000039", "ASV000019",
"ASV000073", "ASV000065", "ASV000055", "ASV000078", "ASV000111", "ASV000048", "ASV000070"]
"""
ASV_order = ["ASV000003", "ASV000096", "ASV000109", "ASV000026", "ASV000040", #Bacilli
             "ASV000243", "ASV000145", "ASV000203", 
             "ASV000153", "ASV000141", "ASV000007", "ASV000005", "ASV000334", "ASV000028", #Bacteroidia
             "ASV000009", "ASV000165", "ASV000046", "ASV000054", "ASV000034", "ASV000045", 
             "ASV000064", "ASV000087", "ASV000125", "ASV000080", "ASV000024", "ASV000030",
             "ASV000085", "ASV000056", "ASV000071", "ASV000014", "ASV000010", "ASV000022", 
             "ASV000016", "ASV000069", "ASV000042", #Alphaproteobacteria
             "ASV000043", 
             "ASV000020", "ASV000098", "ASV000105", "ASV000072", "ASV000147", "ASV000049", 
             "ASV000062", "ASV000018", "ASV000008", "ASV000015", "ASV000108", "ASV000033", 
             "ASV000025", "ASV000036", "ASV000011", "ASV000031", "ASV000002", "ASV000076",
             "ASV000075", "ASV000063", "ASV000023", "ASV000053", "ASV000012", "ASV000198", 
             "ASV000099", "ASV000006", "ASV000021", "ASV000073", "ASV000019", "ASV000065",
             "ASV000286", "ASV000039", "ASV000070", "ASV000048", "ASV000078", "ASV000084", 
             "ASV000055", "ASV000238", "ASV000086", "ASV000004", "ASV000102", "ASV000077", 
             "ASV000013", "ASV000001", "ASV000017", "ASV000029"] #Gammaproteobacteria

new_rows = []
for a in range(len(rows)):
    if a == 0:
        new_rows.append(rows[a])
    else:
        for b in range(len(ASV_order)):
            if rows[a][0] == ASV_order[b]:
                new_rows.append(rows[a])
print(len(new_rows), len(ASV_order))
rows = new_rows

#transpose rows
def transpose(rows):
    cols, names = [], []
    for a in range(len(rows[0])):
        col = []
        for b in range(len(rows)):
            col.append(rows[b][a])
        names.append(col[0])
        del col[0]
        cols.append(col)
    return cols, names

def transpose2(rows):
    cols = []
    for a in range(len(rows[0])):
        col = []
        for b in range(len(rows)):
            col.append(float(rows[b][a]))
        cols.append(col)
    return cols

def log2(cols):
    new_cols = []
    for a in range(len(cols)):
        new_col = []
        for b in range(len(cols[a])):
            num = float(cols[a][b])
            num = int(num*1000)
            if num == 0: num = 0.0001
            num = numpy.log2(num)
            new_col.append(num)
        new_cols.append(new_col)
    return new_cols

cols, names = transpose(rows)

#delete ASV numbers
ASVs = cols[0]
del cols[0]
del names[0]

#get axis
fig = plt.figure(figsize=(20,30))
ax1 = plt.subplot2grid((32,4), (0,0), rowspan=3, colspan=3, frameon=False)
ax2 = plt.subplot2grid((32,4), (3,0), rowspan=1, colspan=3)
ax3 = plt.subplot2grid((32,4), (4,0), rowspan=32, colspan=3)
ax4 = plt.subplot2grid((32,48), (4,36), rowspan=32,colspan=1)
axday = plt.subplot2grid((64,32), (0,24), rowspan=1, colspan=4)
axtrt = plt.subplot2grid((64,32), (1,24), rowspan=1, colspan=4)
axcolbar = plt.subplot2grid((64,32), (5,24), rowspan=1, colspan=4)
axblob = plt.subplot2grid((64,32), (6,24), rowspan=1, colspan=4)

#get dendrogram
plt.sca(ax1)
Z = hierarchy.linkage(cols, 'average', metric='braycurtis')
matplotlib.rcParams['lines.linewidth'] = 2
dn = hierarchy.dendrogram(Z)
#change labels to sample names
x_labels = list(ax1.get_xticklabels())
locs, labels = [], []
locs = list(ax1.get_xticks())
for x in x_labels:
    labels.append(x.get_text())
new_labels = []
new_cols = []
for a in range(len(labels)):
    new_labels.append(names[int(labels[a])-1])
    new_cols.append(cols[int(labels[a])-1])
matplotlib.rcParams['lines.linewidth'] = 2
hierarchy.set_link_color_palette(['k'])
dn = hierarchy.dendrogram(Z, no_labels=True, above_threshold_color='k')
ax1.set_xticklabels(labels=new_labels, fontsize=10)
plt.setp(ax1.get_yticklabels(), visible=False)
ax1.tick_params(axis='y',which='both',left='off', right='off')

cols = new_cols
log_cols = log2(cols)
abun_cols = cols

#get colors for days and sample types and plot them
cols = ['k', 'orange', 'r', 'b', 'g', 'm', 'c']
treats = ['Inoc', 'LowCrysWater', 'LowCrys', 'PET', 'WeatherPET', 'BHET', 'NoC']
cols_day = ['k', 'b', 'g', 'y', 'r', 'orange', 'm', 'c']
days = [0, 1, 3, 7, 14, 21, 30, 42]
alphas = [0, 0.1, 0.25, 0.4, 0.55, 0.7, 0.85, 1]
ax2.set_ylim([0,2])
ax2.set_xlim([0,locs[-1]+5])
colors = []
alphs = []
for a in range(len(new_labels)):
    treat = new_labels[a][5:]
    day = new_labels[a][3:5]
    for b in range(len(treats)):
        if treats[b] == treat:
            colors.append(cols[b])
    for c in range(len(days)):
        if int(day) == int(days[c]):
            alphs.append(alphas[c])
            #alphs.append(cols_day[c])
            
y = []
for a in range(len(locs)):
    y.append(1)
    ax2.bar(locs[a], [1], bottom=[1], width=10, edgecolor='k', color='k', alpha=alphs[a])
#ax2.bar(locs, y, width=10, bottom=y, edgecolor='k', color=alphs, alpha=1)
ax2.bar(locs, y, width=10, edgecolor='k', color=colors, alpha=1)
plt.sca(ax2)
#plt.yticks([0.5, 1.5], ['Treatment', 'Day'])
plt.setp(ax2.get_yticklabels(), visible=False)
#ax2.yaxis.tick_right()
ax2.tick_params(axis='y',which='both',left='off', right='off')
plt.setp(ax2.get_xticklabels(), visible=False)
ax2.tick_params(axis='x',which='both',bottom='off', top='off')
for a in range(8):
    axday.bar([a+1], [1], width=1, edgecolor='k', color='k', alpha=alphas[a])
axtrt.bar([1,2,3,4,5,6,7], [1,1,1,1,1,1,1], width=1, edgecolor='k', color=cols)
axday.set_ylim([0,1]), axtrt.set_ylim([0,1])
axtrt.set_xlim([0.5,7.5])
axday.set_xlim([0.5,8.5])
plt.sca(axtrt)
plt.yticks([0.5], ['Treatment'])
treats = ['Inoculum', 'Amorphous PET \nplanktonic', 'Amorphous PET\nbiofilm', 'PET powder', 'Weathered \nPET powder', 'BHET', 'No Carbon']
plt.xticks([1,2,3,4,5,6,7], treats, rotation=90, fontsize=8)
plt.sca(axday)
plt.yticks([0.5], ['Day'])
plt.xticks([1,2,3,4,5,6,7,8], ['0', '1', '3', '7', '14', '21', '30', '42'])
axtrt.yaxis.tick_right(), axday.yaxis.tick_right()
axday.xaxis.tick_top()

axbx, axby, axbs = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 1, 5, 10, 20, 30, 50]
for a in range(len(axbs)):
    axbs[a] = round(axbs[a]*7, 1)
    axblob.plot([axbx[a]-0.5, axbx[a]-0.5], [0,1], 'k', lw=1)
axblob.scatter(axbx, axby, color='k', s=axbs)
axblob.set_xlim([0,7])
plt.sca(axblob)
plt.xticks(axbx, ['0.5', '1', '5', '10', '20', '30', '50'])
plt.yticks([0.5], ['Maximum relative\nabundance (%)'], fontsize=8)
axblob.yaxis.tick_right()
cmap = mpl.cm.seismic
norm = mpl.colors.Normalize(vmin=0, vmax=1)
cb1 = mpl.colorbar.ColorbarBase(axcolbar, cmap=cmap, norm=norm, orientation='horizontal')
cb1.set_ticks([])
axcolbar.text(0.1, 0.5, 'Low', va='center', ha='left', color='w')
axcolbar.text(0.9, 0.5, 'High', va='center', ha='right', color='w')
plt.sca(axcolbar)
plt.yticks([0.5], ['Relative abundance\n(within ASV)'])



#get fold change between inoculum and all other samples
for a in range(len(log_cols)):
    if a > 0:
        for b in range(len(log_cols[a])):
            log_cols[a][b] = log_cols[a][b]-log_cols[0][b]

#plot fold change or relative abundance, but only if the ASV is in this list
ASV_order.reverse()
with open('Taxonomy.csv', 'rU') as f:
    taxo = []
    for row in csv.reader(f):
        taxo.append(row)
order_taxo = []
for a in range(len(ASV_order)):
    for b in range(len(taxo)):
        if taxo[b][0] == ASV_order[a]:
            order_taxo.append(taxo[b])
for a in range(len(order_taxo)):
    del order_taxo[a][0]
    order_taxo[a].reverse()
    for b in range(len(order_taxo[a])):
        if order_taxo[a][b] != 'NA':
            if b == 0:
                order_taxo[a] = '$'+order_taxo[a][b+1]+'$ $'+order_taxo[a][b]+'$'
            elif b == 1:
                order_taxo[a] = '$'+order_taxo[a][b]+'$'
            else:
                order_taxo[a] = order_taxo[a][b]
            break

log_cols = transpose2(log_cols)
abun_cols = transpose2(abun_cols)
using_log, using_abun, using_ASVs = [], [], []
for a in range(len(ASV_order)):
    for b in range(len(ASVs)):
        if ASVs[b] == ASV_order[a]:
            using_log.append(log_cols[b])
            using_abun.append(abun_cols[b])
            using_ASVs.append(ASVs[b])
cmap = 'seismic'
y1 = y
using = using_abun
ylabs = [1.5]
for a in range(len(using)):
    norm = mpl.colors.Normalize(vmin=min(using[a]), vmax=max(using[a]))
    colormap = mpl.cm.get_cmap(cmap, 256)
    m = mpl.cm.ScalarMappable(norm=norm, cmap=colormap)
    s = max(using[a])*7
    for b in range(len(using[a])):
        using[a][b] = m.to_rgba(using[a][b])
    ax3.bar(locs, y, bottom=y1, color=using[a], edgecolor='k', width=10)
    ax4.scatter(0.5, y1[0]+0.5, marker='o', color='k', s=round(s, 1))
    ax4.plot([0,1], [y1[0],y1[0]], 'k', lw=1)
    y1 = list(map(add, y, y1))
    ylabs.append(y1[0]+0.5)
    using_ASVs[a] = 'ASV'+str(int(using_ASVs[a][3:]))+': '+order_taxo[a]
ax3.set_xlim([0,locs[-1]+5])
ax3.set_ylim([1,ylabs[-2]+0.5])
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)
ax3.tick_params(axis='x',which='both',bottom='off', top='off')
ax3.tick_params(axis='y',which='both',left='off', right='off')

ax4.set_xlim([0,1])
plt.setp(ax4.get_xticklabels(), visible=False)
ax4.tick_params(axis='x',which='both',bottom='off', top='off')
ax4.yaxis.tick_right()
plt.sca(ax4)
plt.yticks(ylabs, using_ASVs)
ax4.set_ylim([1,ylabs[-2]+0.5])


plt.savefig('Samples dendro only 3.png', dpi=600)
