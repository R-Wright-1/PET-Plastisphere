import numpy
import matplotlib.pyplot as plt
import math
import matplotlib as mpl
from matplotlib import rcParams



names = ['trt_BHET_prod_MHET', 'trt_BHET_prod_BHET', 'trt_BHET_prod_TPA', 'trt_BHET_prod_c3', 'trt_BHET_prod_c2', 'trt_TPA_prod_TPA', 'trt_PET_prod_BHET', 'trt_PET_prod_TPA']
name_trt = ['BHET', 'BHET', 'BHET', 'BHET', 'BHET', 'TPA', 'PET', 'PET']
signif = [['*', '*', '*'], ['', '', '*'], ['', '*', '*'], ['*', '', '*'], ['*', '', '*'], ['*', '', ''], ['*', '*', ''], ['', '', '']]
trts = [[0.9856852, 0.2284946, 2.8603021], [-0.4481430, 0.1803383, -1.1974504], [-0.1438281, 4.7297514, 9.1709141], [3.0770337, -0.2454477, 3.5523414], [4.9719465, 0.2709630, 3.8404374], [0.3614663, 0.0392268, -0.2012013], [4.4559584, 1.3796201, 0.9139600], [-0.0591389, 0.0438245, -0.0801876]]
colors = []
txt_col = []

cmap_up = 'winter'
norm_up = mpl.colors.Normalize(vmin=-18, vmax=10)
colormap_up = mpl.cm.get_cmap(cmap_up, 256)
m_up = mpl.cm.ScalarMappable(norm=norm_up, cmap=colormap_up)

cmap_down = 'winter'
norm_down = mpl.colors.Normalize(vmin=-10, vmax=18)
colormap_down = mpl.cm.get_cmap(cmap_down, 256)
m_down = mpl.cm.ScalarMappable(norm=norm_down, cmap=colormap_down)

for a in range(len(trts)):
    this_color = []
    this_txt = []
    for b in range(len(trts[a])):
        trts[a][b] = math.pow(2, trts[a][b])
        if trts[a][b] < 1:
            trts[a][b] = -(1/trts[a][b])
        trts[a][b] = round(trts[a][b], 2)
        if trts[a][b] < 0:
            this_color.append(m_down.to_rgba(trts[a][b]))
        else:
            this_color.append(m_up.to_rgba(trts[a][b]))
        if trts[a][b] < 1:
            this_txt.append('w')
        else:
            this_txt.append('k')
        trts[a][b] = str(trts[a][b])#+r'$^{'+signif[a][b]+'}$'
        if signif[a][b] == '*':
            trts[a][b] = r'$\bf{'+trts[a][b]+'}$'
    colors.append(this_color)
    txt_col.append(this_txt)
    
print(trts[1])
bugs = ['Thio', 'Baci', 'Ideo']

for a in range(len(trts)):
    fig = plt.figure(figsize=(9,2))
    ax1 = plt.subplot(111)
    plt.xticks([])
    plt.yticks([0.5], [name_trt[a]], rotation=90, ha='right', va='center', fontsize=40)
    ax1.bar([1,2,3], [1,1,1], width=1, color=colors[a], edgecolor='k')
    ax1.set_xlim([0.5, 3.5])
    ax1.set_ylim([0,1])
    for b in range(3):
        ax1.text(b+1, 0.5, bugs[b]+'\n'+trts[a][b], ha='center', va='center', fontsize=40, color=txt_col[a][b])
    plt.savefig(names[a]+'.png', dpi=600, bbox_inches='tight')
    plt.close()

fs = 40   
ax1 = plt.subplot2grid((6,2), (0,0), colspan=2)

cmap = 'winter'
norm = mpl.colors.Normalize(vmin=0, vmax=1)
colormap = mpl.cm.get_cmap(cmap, 256)
cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=colormap, norm=norm, orientation='horizontal')

ax1.text(0.5,1, 'Metabolomics\nfold change', ha='center', va='bottom', fontsize=fs)
cb1.set_ticks([0, 1])
cb1.set_ticklabels(['<-10', '>10'])
cb1.ax.tick_params(labelsize=fs-10)

plt.subplots_adjust(wspace=0)
plt.savefig('Colorbar.png', bbox_inches='tight', dpi=600)
        