import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import math

Hcol, Mcol = '#F4B183', '#9DC3E6'
#Hcol, Mcol = (248,203,173), (189,215,238)

def remove(ax, fs, myco, halo):
    ax.tick_params(axis='x',which='both',top='on', bottom='off')
    ax.xaxis.tick_top()
    plt.xticks([])
    ax.text(0, 3.1, 'Thio\n', fontsize=fs, color='k', va='bottom', ha='center')
    ax.text(0, 3.1, myco, fontsize=fs-5, color='k', va='bottom', ha='center')
    #ax.text(1.1, 3.1, 'Baci\n', fontsize=fs, color='k', va='bottom', ha='center')
    #ax.text(1.1, 3.1, halo, fontsize=fs-5, color='k', va='bottom', ha='center')
    plt.yticks([])
    ax.tick_params(axis='y',which='both',left='off', right='off')
    ax.yaxis.tick_right()
    return

def get_plot(n1, n2, name, fs, halo, myco, enzyme, count):
    n1.reverse()
    n2.reverse()
    cmap_up = 'spring'
    norm_up = mpl.colors.Normalize(vmin=-8, vmax=10)
    colormap_up = mpl.cm.get_cmap(cmap_up, 256)
    m_up = mpl.cm.ScalarMappable(norm=norm_up, cmap=colormap_up)

    cmap_down = 'spring'
    norm_down = mpl.colors.Normalize(vmin=-10, vmax=8)
    colormap_down = mpl.cm.get_cmap(cmap_down, 256)
    m_down = mpl.cm.ScalarMappable(norm=norm_down, cmap=colormap_down)
    fig = plt.figure(figsize=(2.5,4))
    ax1 = plt.subplot(111, frameon=False)
    txt = ['TPA\n', 'BHET\n', 'PET\n']
    for a in range(len(n1)):
        tx1, tx2 = 'k', 'k'
        edge1, edge2 = 'k', 'k'
        if n1[a] == 'ND':
            color1, edge1 = 'w', 'w'
        elif n1[a] > 0:
            color1 = m_up.to_rgba(n1[a])
            if n1[a] > 7.5: tx1 = 'k'
        else:
            color1 = m_down.to_rgba(n1[a])
        if n2[a] == 'ND':
            color2, edge2 = 'w', 'w'
        elif n2[a] > 0:
            color2 = m_up.to_rgba(n2[a])
            if n2[a] > 7.5: tx2 = 'k'
        else: 
            color2 = m_down.to_rgba(n2[a])
        if a > 0:
            #ax1.bar([0,1.1], [1,1], bottom=[a, a], color=[color1, color2], width=[0.99,0.99], edgecolor=[edge1, edge2])
            ax1.bar([0], [1], bottom=[a], color=[color1], width=[0.99], edgecolor=[edge1])
        else:
            #ax1.bar([0,1.1], [1,1], width=[0.99,0.99], edgecolor=[edge1, edge2], color=[color1, color2])
            ax1.bar([0], [1], width=[0.99], edgecolor=[edge1], color=[color1])
        if n1[a] != 'ND':
            ax1.text(0, a+0.5, txt[a]+str(round(n1[a], 1)), color=tx1, fontsize=fs-12, ha='center', va='center')
        """
        if n2[a] != 'ND':
            ax1.text(1.1, a+0.5, txt[a]+str(round(n2[a], 1)), color=tx2, fontsize=fs-12, ha='center', va='center')
        """
    #ax1.set_xlim([-0.5, 2])
    ax1.set_xlim([-0.5,0.5])
    ax1.set_ylim([0, 3])
    if count > 3:
        #ax1.text(2.2, 1.5, enzyme, fontsize=fs-15, color='k', ha='center', va='center', rotation=90)
        ax1.text(1.1, 1.5, enzyme, fontsize=fs-15, color='k', ha='center', va='center', rotation=90)
    elif count > 2:
        #ax1.text(2, 1.5, enzyme, fontsize=fs-15, color='k', ha='center', va='center', rotation=90)
        ax1.text(0.9, 1.5, enzyme, fontsize=fs-15, color='k', ha='center', va='center', rotation=90)
    else:
        #ax1.text(1.8, 1.5, enzyme, fontsize=fs-15, color='k', ha='center', va='center', rotation=90)
        ax1.text(0.7, 1.5, enzyme, fontsize=fs-15, color='k', ha='center', va='center', rotation=90)
    remove(ax1, fs, myco, halo)
    plt.savefig(name+'.png', bbox_inches='tight', dpi=300)
    plt.close()
    return

fs = 44

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

with open('Pathways_confirmed.csv', 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)

for a in range(1, len(rows)):
    nums = rows[a][4:-1]
    name = rows[a][0]
    halo, myco = rows[a][2], rows[a][1]
    enzyme = rows[a][-1]
    if len(halo) > 5:
        halo = 'Multiple'
    if len(myco) > 5:
        myco = 'Multiple'
    new_enzyme = ''
    count = 1
    for a in range(len(enzyme)):
        if enzyme[a] == '_':
            new_enzyme += '\n'
            count += 1
        else:
            new_enzyme += enzyme[a]
    if nums != ['', '', '', '', '', '']:
        for b in range(len(nums)):
            if is_number(nums[b]) and nums[b] != 'ND':
                nums[b] = float(nums[b])
                nums[b] = math.pow(2, nums[b])
                if nums[b] < 1:
                    nums[b] = -(1/nums[b])
        get_plot(nums[:3], nums[3:], name, fs, halo, myco, new_enzyme, count)


fs = 40   
ax1 = plt.subplot2grid((6,2), (0,0), colspan=2)

cmap = 'spring'
norm = mpl.colors.Normalize(vmin=0, vmax=1)
colormap = mpl.cm.get_cmap(cmap, 256)
cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=colormap, norm=norm, orientation='horizontal')

ax1.text(0.5,1, 'Proteomics\nfold change', ha='center', va='bottom', fontsize=fs)
cb1.set_ticks([0, 1])
cb1.set_ticklabels(['<-10', '>10'])
cb1.ax.tick_params(labelsize=fs-10)

plt.subplots_adjust(wspace=0)
plt.savefig('Colorbar.png', bbox_inches='tight', dpi=600)