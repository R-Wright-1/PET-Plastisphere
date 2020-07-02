import csv
import numpy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from matplotlib.patches import Ellipse
from matplotlib.patches import Ellipse
from sklearn import manifold
import matplotlib as mpl
from scipy.spatial import distance
import matplotlib.patches as mpatches
from matplotlib.patches import Patch
import statsmodels.stats.multitest as smm
from pylab import *
from matplotlib.lines import Line2D
import matplotlib

def get_gens_and_samples(fn):
    with open(fn, 'rU') as f:
        rows = []
        for row in csv.reader(f):
            rows.append(row)
    samples = []
    for b in range(3, len(rows)):
        this_row = []
        for c in range(1, len(rows[b])):
            this_row.append(float(rows[b][c]))
        samples.append(this_row)
    color_dict = {'NoC':'y', 'LC':'#ff0080', 'PET':'b', 'WPET':'g', 'BHET':'orange'}
    shape_dict = {'NoInoc':'x', 'Community':'o'}
    colors, shapes = [], []
    for a in range(1, len(rows[0])):
        colors.append(color_dict[rows[0][a]])
    for a in range(1, len(rows[1])):
        shapes.append(shape_dict[rows[1][a]])
    return samples, colors, shapes
    
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
    samples, colors, shapes = get_gens_and_samples(fn)
    s = pd.DataFrame(samples)
    s = s.transpose()
    pos, npos, stress = transform_for_NMDS(s)
    ind, ind1 = 0, 0
    x, y = [], []
    tx, ty = [], []
    al = 0.15
    labels = ['No carbon', 'Amorphous PET', 'PET powder', 'Weathered PET powder', 'BHET']
    count = 0
    for a in range(len(samples[0])):
        tx.append(npos[a,0])
        ty.append(npos[a,1])
        ax.scatter(npos[a,0], npos[a,1], marker=shapes[a], color=colors[a], s=100)
        if a < len(samples[0])-1:
            if (a+1) % 21 == 0 and a > 0:
                x.append(tx)
                y.append(ty)
                #el_cols.append(colors[a])
                tx, ty = [], []
                #ax.scatter(npos[a-1,0], npos[a-1,1], marker=shapes[a-1], color=colors[a-1], alpha=alpha[a-1], label=labels[count], s=100)
                count += 1
    """
    ellipses = []
    el_cols = ['y', 'r', 'm', 'b', 'g', 'orange']
    for z in range(6):
        nstd = 2
        x1, y1 = x[z], y[z]
        cov = np.cov(x1, y1)
        vals, vecs = eigsorted(cov)
        theta = np.degrees(np.arctan2(*vecs[:,0][::-1]))
        w, h = 2 * nstd * np.sqrt(vals)
        ell = Ellipse(xy=(np.mean(x1), np.mean(y1)),width=w, height=h,angle=theta, edgecolor=el_cols[z], alpha=1)     
        ell.set_facecolor(el_cols[z])
        ell.set_edgecolor(el_cols[z])
        ellipses.append(ell)
    for e in ellipses:
        e.set_clip_box(ax.bbox)
        e.set_alpha(0.03)
        ax.add_artist(e)
    """
    legend_elements = []
    marker_cols = ['y', '#ff0080', 'b', 'g', 'orange']
    for a in range(len(marker_cols)):
        legend_elements.append(Line2D([0], [0], marker='s', markerfacecolor=marker_cols[a], markeredgecolor=marker_cols[a], label=labels[a], markersize=10, color='none'))
    ax.legend(handles=legend_elements, loc='upper right', fontsize=16, scatterpoints=1)
    matplotlib.rcParams['legend.handlelength'] = 0
    #ax.legend(loc='upper right', fontsize=16)
    ax.set_xlabel('nMDS 1', fontsize=16)
    ax.set_ylabel('nMDS 2', fontsize=16)
    plt.sca(ax)
    plt.annotate('Stress = %.3f'%stress, xy=(0.05, 0.95), xycoords='axes fraction', fontsize=16)
    return
fig = plt.figure(figsize=(14, 10))   
ax1 = plt.subplot(111)

plot_nmds('areas.csv', ax1)


#ax2.set_ylabel('')

#plt.show()
#plt.subplots_adjust(hspace=1, wspace=0.4)
plt.savefig('Metabolomics.png', bbox_inches='tight', dpi=600)
#plt.close()


