import matplotlib.pyplot as plt
import csv
import numpy
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from matplotlib.patches import Ellipse
from sklearn import manifold
from scipy.spatial import distance
from matplotlib.lines import Line2D
import matplotlib
import matplotlib as mpl

figure = plt.figure(figsize=(20,30))

def get_gens_and_samples(fn):
    with open(fn, 'rU') as f:
        rows = []
        for row in csv.reader(f):
            rows.append(row)
    samples = []
    for b in range(len(rows)):
        if b > 0:
            this_row = []
            for c in range(len(rows[b])):
                if c > 0:
                    this_row.append(float(rows[b][c]))
            samples.append(this_row)
    return samples
    
def transform_for_NMDS(df):
    X = df.iloc[0:].values
    y = df.iloc[:,0].values
    n_samples = 14
    seed = np.random.RandomState(seed=3)
    X_true = seed.randint(0, 20, 2 * n_samples).astype(np.float)
    X_true = X_true.reshape((n_samples, 2))
    X_true = X
    similarities = distance.cdist(X_true, X_true, 'braycurtis')
    mds = manifold.MDS(n_components=2, max_iter=3000, eps=1e-9, random_state=seed,
                   dissimilarity="precomputed", n_jobs=1)
    pos = mds.fit(similarities).embedding_
    
    nmds = manifold.MDS(n_components=2, metric=False, max_iter=3000, eps=1e-12,
                        dissimilarity="precomputed", random_state=seed, n_jobs=1,
                        n_init=1)
    npos = nmds.fit_transform(similarities, init=pos)
    print(nmds.stress_)
    # Rescale the data
    pos *= np.sqrt((X_true ** 2).sum()) / np.sqrt((pos ** 2).sum())
    npos *= np.sqrt((X_true ** 2).sum()) / np.sqrt((npos ** 2).sum())
    # Rotate the data
    clf = PCA()
    X_true = clf.fit_transform(X_true)
    pos = clf.fit_transform(pos)
    npos = clf.fit_transform(npos)
    return pos, npos, nmds.stress_
    
def eigsorted(cov):
    vals, vecs = np.linalg.eigh(cov)
    order = vals.argsort()[::-1]
    return vals[order], vecs[:,order]


def plot_nmds(fn, ax):
    samples = get_gens_and_samples(fn)
    s = pd.DataFrame(samples)
    s = s.transpose()
    pos, npos, stress = transform_for_NMDS(s)
    colors = ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y',
              'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r',
              'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 
              'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 
              'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
              'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'k', 'k', 'k']
    shapes = ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
              '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^',
              's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 
              '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', 
              'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x',
              'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', '*', '*', '*']
    alpha = [0.06, 0.06, 0.06, 0.2, 0.2, 0.2, 0.34, 0.34, 0.34, 0.48, 0.48, 0.48, 0.62, 0.62, 0.62, 0.86, 0.86, 0.86, 1, 1, 1, 
             0.06, 0.06, 0.06, 0.2, 0.2, 0.2, 0.34, 0.34, 0.34, 0.48, 0.48, 0.48, 0.62, 0.62, 0.62, 0.86, 0.86, 0.86, 1, 1, 1, 
             0.06, 0.06, 0.06, 0.2, 0.2, 0.2, 0.34, 0.34, 0.34, 0.48, 0.48, 0.48, 0.62, 0.62, 0.62, 0.86, 0.86, 0.86, 1, 1, 
             0.06, 0.06, 0.06, 0.2, 0.2, 0.2, 0.34, 0.34, 0.34, 0.48, 0.48, 0.48, 0.62, 0.62, 0.62, 0.86, 0.86, 0.86, 1, 1, 
             0.06, 0.06, 0.06, 0.2, 0.2, 0.2, 0.34, 0.34, 0.34, 0.48, 0.48, 0.48, 0.62, 0.62, 0.62, 0.86, 0.86, 0.86, 1, 1, 1, 
             0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.34, 0.34, 0.34, 0.48, 0.48, 0.48, 0.62, 0.62, 0.62, 0.86, 0.86, 0.86, 1, 1, 1, 1, 1, 1]
    new_alpha = []
    for a in range(len(alpha)):
        new_alpha.append(alpha[a])
        new_alpha.append(alpha[a])
        new_alpha.append(alpha[a])
    ind, ind1 = 0, 0
    x, y = [], []
    tx, ty = [], []
    al = 0.15
    labels = ['No carbon', 'Amorphous PET planktonic', 'Amorphous PET biofilm', 'PET powder', 'Weathered PET powder', 'BHET', 'Inoculum']
    count = 0
    for a in range(len(samples[0])):
        tx.append(npos[a,0])
        ty.append(npos[a,1])
        al += alpha[ind]
        #nmds1.append(npos[a,0])
        #nmds2.append(npos[a,1])
        ax.scatter(npos[a,0], npos[a,1], marker=shapes[a], color=colors[a], alpha=alpha[a], s=100, edgecolor='gray')
        if a < len(samples[0])-1:
            if (a+1) % 21 == 0 and a > 0:
                x.append(tx)
                y.append(ty)
                #el_cols.append(colors[a])
                tx, ty = [], []
                #ax.scatter(npos[a-1,0], npos[a-1,1], marker=shapes[a-1], color=colors[a-1], alpha=alpha[a-1], label=labels[count], s=100)
                count += 1
    ax.scatter(npos[a,0], npos[a,1], marker=shapes[a], color=colors[a], alpha=alpha[a], label=labels[count], s=100, edgecolor='gray')
    ellipses, ellipses2 = [], []
    el_cols = ['y', 'r', 'm', 'b', 'g', 'orange']
    for z in range(6):
        nstd = 2
        x1, y1 = x[z], y[z]
        cov = np.cov(x1, y1)
        vals, vecs = eigsorted(cov)
        theta = np.degrees(np.arctan2(*vecs[:,0][::-1]))
        w, h = 2 * nstd * np.sqrt(vals)
        ell = Ellipse(xy=(np.mean(x1), np.mean(y1)),width=w, height=h,angle=theta, edgecolor=el_cols[z], alpha=1)
        ell2 = Ellipse(xy=(np.mean(x1), np.mean(y1)),width=w, height=h,angle=theta, edgecolor=el_cols[z], alpha=1, facecolor='none', lw=2)     
        ell2.set_edgecolor(el_cols[z])
        ell.set_edgecolor(el_cols[z])
        ell.set_facecolor(el_cols[z])
        ellipses.append(ell)
        ellipses2.append(ell2)
    for e in ellipses:
        e.set_clip_box(ax.bbox)
        e.set_alpha(0.1)
        ax.add_artist(e)
    for e in ellipses2:
        #e.set_alpha(1)
        e.set_clip_box(ax.bbox)
        ax.add_artist(e)
    leg_shapes = ['o', '^', 's', '1', 'x', 'p', '*']
    legend_elements = []
    marker_cols = el_cols+['k']
    #labels = ['BHET', 'Low crystallinity PET biofilm', 'Low crystallinity PET planktonic', 'PET powder', 'Weathered PET powder']
    #labels = ['No carbon', 'Low crystallinity PET planktonic', 'Low crystallinity PET biofilm', 'PET powder', 'Weathered PET powder', 'BHET', 'Inoculum']
    for a in range(len(leg_shapes)):
        legend_elements.append(Line2D([0], [0], marker=leg_shapes[a], markerfacecolor=marker_cols[a], markeredgecolor=marker_cols[a], label=labels[a], markersize=10, color='none'))
    new_legend_elements = []
    order = [6, 0, 5, 2, 1, 3, 4]
    for b in range(len(order)):
        new_legend_elements.append(legend_elements[order[b]])
    ax.legend(handles=new_legend_elements, loc='upper right', scatterpoints=1, frameon=False)
    matplotlib.rcParams['legend.handlelength'] = 0
    #ax.legend(loc='upper right', fontsize=16)
    ax.set_xlabel('nMDS 1')
    ax.set_ylabel('nMDS 2')
    plt.sca(ax)
    plt.annotate('Stress = %.3f'%stress, xy=(0.05, 0.95), xycoords='axes fraction')
    return x, y
axnMDS = plt.subplot2grid((3,24), (0,0), colspan=10)
fs=18
axnMDS.set_title('nMDS', fontsize=fs)
axnMDS.set_title('A', loc='left', fontsize=fs)
x, y = plot_nmds('Not_grouped_nMDS.csv', axnMDS)
plt.savefig('nMDS only.png')
nmds1, nmds2 = x, y

cutoff = 100

with open('PRC_values_treatments.csv', 'rU') as f:
    PRC_trt = []
    for row in csv.reader(f):
        PRC_trt.append(row)

for a in range(len(PRC_trt)):
    for b in range(len(PRC_trt[a])):
        if b > 0:
            PRC_trt[a][b] = float(PRC_trt[a][b])
ax1 = plt.subplot2grid((3,24), (0,12), colspan=7)
ax1.set_title('Principal Response Curve', fontsize=fs)
ax1.set_title('B', loc='left', fontsize=fs)


labels = ['BHET', 'Amorphous PET biofilm', 'Amorphous PET planktonic', 'PET powder', 'Weathered PET powder']
markers = ['p', 's', '^', '1', 'x']
colors = ['orange', 'm', 'r', 'b', 'g']
for a in range(1, len(PRC_trt)):
    ax1.plot(PRC_trt[0][1:], PRC_trt[a][1:], marker=markers[a-1], label=labels[a-1], color=colors[a-1])

ax1.plot(PRC_trt[0][1:], [0, 0, 0, 0, 0, 0, 0, 0], 'k--')
ax1.legend(loc='best', frameon=False)
ax1.set_ylabel('Effect')
ax1.set_xlabel('Day')
ax1.set_ylim([-0.25, 0.25])
ax1.set_xlim([-2, 44])
plt.sca(ax1)
plt.xticks(PRC_trt[0][1:], ['0', '1', '3', '7', '14', '21', '30', '42'])
plt.savefig('nMDS+PRC.png')

with open('PRC_values_species.csv', 'rU') as f:
    PRC_spc = []
    for row in csv.reader(f):
        PRC_spc.append(row)
with open('PRC_values_species_logabun.csv', 'rU') as f:
    PRC_logabun = []
    for row in csv.reader(f):
        PRC_logabun.append(row)

ASV, vals, log_abun = [], [], []
for a in range(len(PRC_spc)):
    if PRC_spc[a][0][0] == 'A':
        ASV.append(PRC_spc[a][0])
        ASV.append(PRC_spc[a][1])
    else:
        vals.append(PRC_spc[a][0])
        vals.append(PRC_spc[a][1])
        log_abun.append(PRC_logabun[a][0])
        log_abun.append(PRC_logabun[a][1])
for a in range(len(ASV)):
    this_ASV = ''
    for b in range(len(ASV[a])):
        if ASV[a][b] != '.':
            this_ASV+= ASV[a][b]
        elif ASV[a][b] == '.':
            break
    ASV[a] = this_ASV

with open('Taxonomy.csv', 'rU') as f:
    tax = []
    for row in csv.reader(f):
        tax.append(row)
del ASV[-1]
del vals[-1]
del log_abun[-1]

new_ASV, new_vals, new_logabun, old_vals = [], [], [], []
for a in range(len(log_abun)):
    if float(log_abun[a]) > cutoff:
        new_ASV.append(ASV[a])
        new_vals.append(numpy.exp(float(vals[a])))
        old_vals.append(float(vals[a]))
        new_logabun.append(float(log_abun[a]))
ASV = new_ASV


for a in range(len(ASV)):
    for b in range(1, len(tax)):
        if int(ASV[a][3:]) == int(tax[b][0][3:]):
            tax[b].reverse()
            for c in range(len(tax[b])):
                if tax[b][c] != 'NA':
                    if c == 0:
                        this_tax = '$'+tax[b][c+1]+'$ $'+tax[b][c]+'$'
                    elif c == 1:
                        this_tax = '$'+tax[b][c]+'$'
                    else:
                        this_tax = tax[b][c]
                    break
            tax[b].reverse()
            ASV[a] += ': '+this_tax
            break

ax2 = plt.subplot2grid((6,48), (0,40))
ax2.spines['top'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2a = plt.subplot2grid((6,48), (0,41), sharex=ax2, frameon=False, colspan=2)
ax3 = plt.subplot2grid((6,48), (1,40))
ax3.spines['top'].set_visible(False)
ax3.spines['bottom'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3a = plt.subplot2grid((6,48), (1,41), sharex=ax2, frameon=False, colspan=2)
ylocs2, ylabs2, ylocs3, ylabs3 = [], [], [], []
for a in range(len(ASV)):
    if new_vals[a] == 1 or new_vals[a] < 1:
        ax3.plot([0,1], [new_vals[a], new_vals[a]], 'k-', linewidth=1)
        ylocs3.append(new_vals[a])
        ylabs3.append(ASV[a])
    else:
        ax2.plot([0,1], [new_vals[a], new_vals[a]], 'k-', linewidth=1)
        ylocs2.append(new_vals[a])
        ylabs2.append(ASV[a])

#print(min(new_vals), max(new_vals))

y3 = [x for _,x in sorted(zip(ylocs3,ylabs3))]
ylocs3 = sorted(ylocs3)

interval = 0.6/len(y3)
newylocs3, newylabs3 = [], []
for a in range(len(y3)):
    ax3a.plot([0,1], [ylocs3[a], 0.4+(interval*(a))], 'k-')
    newylocs3.append(0.4+(interval*(a)))
    newylabs3.append(y3[a])

y2 = [x for _,x in sorted(zip(ylocs2,ylabs2))]
ylocs2 = sorted(ylocs2)

interval = 3.45/(len(y2)-1)
newylocs2, newylabs2 = [], []
for a in range(len(y2)):
    ax2a.plot([0,1], [ylocs2[a], 1+(interval*(a))], 'k-')
    newylocs2.append(1+(interval*(a)))
    newylabs2.append(y2[a])

plt.sca(ax2)
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.sca(ax2a)
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.yticks(newylocs2, newylabs2)
ax2a.tick_params(axis=u'both', which=u'both',length=0)
ax2a.yaxis.tick_right()
plt.sca(ax3)
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.sca(ax3a)
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.yticks(newylocs3, newylabs3)
ax3a.tick_params(axis=u'both', which=u'both',length=0)
ax3a.yaxis.tick_right()
ax2.set_xlim([0,1])
ax3.set_xlim([0,1])
ax2.set_ylim([1, 4.45])
ax2a.set_ylim([1, 4.45])
ax3.set_ylim([0.4, 1])
ax3a.set_ylim([0.4, 1])
plt.subplots_adjust(hspace=0, wspace=0)
ax2.text(-1.5, 1, 'Contribution to Effect', ha='left', va='center', rotation=90)

plt.savefig('nMDS+PRC+labels.png')

newylabs2.reverse()
newylabs3.reverse()
asv_find = newylabs2+newylabs3
asv_find.reverse()

axcolbar = plt.subplot2grid((120,58), (42,50), colspan=8)
plt.sca(axcolbar)
plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)
plt.tick_params(axis='x', which='both', top=False, bottom=False, labelbottom=False)
axcolbar.text(0.1, 0.5, '0', ha='center', va='center', color='w')
axcolbar.text(0.9, 0.5, '1', ha='center', va='center', color='k')
norm = mpl.colors.Normalize(vmin=0, vmax=1)
colormap = mpl.cm.get_cmap('viridis', 256)
matplotlib.colorbar.ColorbarBase(axcolbar, cmap=colormap, norm=norm, orientation='horizontal')
plt.tick_params(axis='x', which='both', top=False, bottom=False, labelbottom=False)
plt.xlabel('Normalised relative abundance')
    
axInoc = plt.subplot2grid((24,58), (9,0), rowspan=10)
axNC = plt.subplot2grid((24,58), (9,2), colspan=7, rowspan=10)
axBHET = plt.subplot2grid((24,58), (9,10), colspan=7, rowspan=10)
axLC = plt.subplot2grid((24,58), (9,18), colspan=7, rowspan=10)
axLCW = plt.subplot2grid((24,58), (9,26), colspan=7, rowspan=10)
axPET = plt.subplot2grid((24,58), (9,34), colspan=7, rowspan=10)
axWPET = plt.subplot2grid((24,58), (9,42), colspan=7, rowspan=10)
axblob = plt.subplot2grid((24,58), (9,50), rowspan=10)
axInoc.set_title('Inoculum')
axNC.set_title('No carbon', color='y')
axBHET.set_title('BHET', color=colors[0])
axLC.set_title('Amorphous\nPET biofilm', color=colors[1])
axLCW.set_title('Amorphous\nPET planktonic', color=colors[2])
axPET.set_title('PET powder', color=colors[3])
axWPET.set_title('Weathered PET powder', color=colors[4])
axInoc.text(0.5, len(asv_find)+2, 'C', va='center', ha='center', fontsize=fs)

plots = [axInoc, axNC, axBHET, axLC, axLCW, axPET, axWPET]
axLC.text(44, -1.8, 'Day', ha='center', va='center')

width = [1, 2, 4, 7, 7, 9, 12]
xlab = [1, 3, 7, 14, 21, 30, 42]
xtxt = ['1', '3', '7', '14', '21', '30', '42']

for y in plots:
    plt.sca(y)
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)
    if y != axInoc:
        plt.xticks(xlab, xtxt)
    y.set_xlim([0.5, 42.5])
    y.set_ylim([0,len(asv_find)])
plt.sca(axInoc)
plt.xticks([0.5], ['0'])
axInoc.set_xlim([0,1])
plt.sca(axblob)
plt.tick_params(axis='x', which='both', top=False, bottom=False, labelbottom=False)
axblob.yaxis.tick_right()
axblob.set_ylim([0,len(asv_find)])
axblob.set_xlim([0,1])
    
with open('over_time_all.csv', 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)

plot_rows = []
for a in range(len(asv_find)):
    asv = ''
    for b in range(3, len(asv_find[a])):
        if asv_find[a][b] != ':':
            asv += asv_find[a][b]
        elif asv_find[a][b] == ':':
            break
    for b in range(1, len(rows)):
        other_asv = ''
        for c in range(3, len(rows[b][0])):
            if rows[b][0][c] != ' ':
                other_asv += rows[b][0][c]
            elif rows[b][0][c] == ' ':
                break
        if int(asv) == int(other_asv):
            plot_rows.append(rows[b])

plot_rows.reverse()
with open('PRC_rows.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(rows[0])
    for row in plot_rows:
        writer.writerow(row)
plot_rows.reverse()

y = 0
cs, cf = [1, 2, 9, 16, 23, 30, 37], [2, 9, 16, 23, 30, 37, 44]
ally, ylab = [], []
pltx, plty = [1, 2.5, 5.5, 11, 18, 26, 36.5], [1,1,1,1,1,1,1]
for a in range(len(plot_rows)):
    for b in range(1, len(plot_rows[a])):
        plot_rows[a][b] = float(plot_rows[a][b])
        if plot_rows[a][b] == 0:
            plot_rows[a][b] = 0.0001
    #print(min(plot_rows[a][1:]))
    norm = mpl.colors.Normalize(vmin=min(plot_rows[a][1:]), vmax=max(plot_rows[a][1:]))
    #norm = mpl.colors.LogNorm(vmin=0.001, vmax=45)
    m = mpl.cm.ScalarMappable(norm=norm, cmap=colormap)
    s = max(plot_rows[a][1:])
    for b in range(1, len(plot_rows[a])):
        plot_rows[a][b] = m.to_rgba(plot_rows[a][b])
    axblob.scatter(0.5, y+0.5, s=(s*7), color='k')
    axblob.plot([0,1], [y+1, y+1], 'k-', linewidth=1)
    for c in range(len(plots)):
        if c == 0:
            plots[c].bar([0.5], [1], bottom=[y], color=plot_rows[a][cs[c]:cf[c]], width=1, edgecolor='k')
        else:
            plots[c].bar(pltx, plty, bottom=[y,y,y,y,y,y,y], color=plot_rows[a][cs[c]:cf[c]], width=width, edgecolor='k')
    ally.append(y+0.5)
    y+=1

plt.sca(axblob)
plt.yticks(ally, asv_find)   

plt.savefig('PRC_python_new_color_nMDS_log.png', dpi=600, bbox_inches='tight')
plt.close()






"""
labels = ['No carbon', 'Low crystallinity PET planktonic', 'Low crystallinity PET biofilm', 'PET powder', 'Weathered PET powder', 'BHET', 'Inoculum']

colors = ['y', 'r', 'm', 'b', 'g', 'orange']
shapes = ['o', '^', 's', '1', 'x', 'p']
    

ax1 = plt.subplot(211)
ax2 = plt.subplot(212)

for a in range(len(nmds1)-1):
    thisx, thisy = [], []
    overallx, overally = [], []
    overallxe, overallye = [], []
    for b in range(len(nmds1[a])):
        if (b+1) %3 == 0:
            thisx.append(nmds1[a][b])
            thisy.append(nmds2[a][b])
            thisxm = numpy.mean(thisx)
            thisxe = numpy.std(thisx)
            thisym = numpy.mean(thisy)
            thisye = numpy.std(thisy)
            thisx, thisy = [], []
            overallx.append(thisxm)
            overally.append(thisym)
            overallxe.append(thisxe)
            overallye.append(thisye)
        else:
            thisx.append(nmds1[a][b])
            thisy.append(nmds2[a][b])
    ax1.errorbar([1,3,7,14,21,30,42], overallx, yerr=overallxe, marker=shapes[a], color=colors[a])
    ax2.errorbar([1,3,7,14,21,30,42], overally, yerr=overallye, marker=shapes[a], color=colors[a])
"""   