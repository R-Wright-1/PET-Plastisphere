import csv
import matplotlib.pyplot as plt
import numpy
from matplotlib.patches import Patch
import os

name = 'pred_metagenome_unstrat_ordered.csv'
#name = 'path_abun_unstrat_ordered.csv'
with open(name, 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)

os.chdir(os.getcwd()+'/KO_metagenome_plots')
#os.chdir('/Users/robynwright/Documents/OneDrive/PhD_Plastic_Oceans/Experiments/MiSeq2/Analysis_PET2/server/PICRUSt2/Robyn_PICRUSt2_out/plotting_all/pathway_plots/')
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
     10, 11, 12, 13, 14, 15, 16, 17,
     18, 19, 20, 21, 22, 23, 24, 25,
     26, 27, 28, 29, 30, 31, 32, 33,
     34, 35, 36, 37, 38, 39, 40, 41,
     42]
colors = ['k',
          'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange',
          'm', 'm', 'm', 'm', 'm', 'm', 'm',
          'r', 'r', 'r', 'r', 'r', 'r', 'r', 
          'y', 'y', 'y', 'y', 'y', 'y', 'y',
          'b', 'b', 'b', 'b', 'b', 'b', 'b',
          'g', 'g', 'g', 'g', 'g', 'g', 'g']
alpha = [1, 
        0.18, 0.3, 0.42, 0.54, 0.76, 0.88, 1, 
        0.18, 0.3, 0.42, 0.54, 0.76, 0.88, 1, 
        0.18, 0.3, 0.42, 0.54, 0.76, 0.88, 1, 
        0.18, 0.3, 0.42, 0.54, 0.76, 0.88, 1, 
        0.18, 0.3, 0.42, 0.54, 0.76, 0.88, 1, 
        0.18, 0.3, 0.42, 0.54, 0.76, 0.88, 1]
labels = ['Inoc', 'BHET', 'Amorphous PET biofilm', 'Amorphous PET planktonic', 'No carbon', 'PET', 'Weathered PET']

new_file_means, new_file_sd = [], []

for a in range(1, len(rows)):
    """
    if rows[a][0] != 'K00449':
        continue
    if rows[a][0] != 'K00448':
        continue
    """
    plt.close()
    this_rep_name, this_rep, this_rep_sd = [], [], []
    trn, tr = [], []
    for b in range(1, len(rows[0])):
        if trn == []:
            trn.append(rows[0][b])
            tr.append(rows[a][b])
        else:
            if trn[0][:-1] == rows[0][b][:-1]:
                trn.append(rows[0][b])
                tr.append(rows[a][b])
            do_this = False
            if trn[0][:-1] != rows[0][b][:-1]:
                do_this = True 
            if b == 127:
                do_this = True
            if do_this:
                this_rep_name.append(trn[0][:-1])
                for c in range(len(tr)):
                    tr[c] = float(tr[c])
                this_rep.append(numpy.mean(tr))
                this_rep_sd.append(numpy.std(tr))
                trn, tr = [], []
                trn.append(rows[0][b])
                tr.append(rows[a][b])
    if a == 1:
        new_file_means.append([rows[0][0]]+this_rep_name)
        new_file_sd.append([rows[0][0]]+this_rep_name)
    new_file_means.append([rows[a][0]]+this_rep)
    new_file_sd.append([rows[a][0]]+this_rep_sd)
    fig = plt.figure(figsize=(10,10))
    ax = plt.subplot(111, projection='polar')
    #print(len(x), len(this_rep), len(colors), len(this_rep_sd), len(alpha))
    for b in range(len(x)):
        if b == 0:
            pltx = 5.49778714+0.39269908
        else:
            pltx = (x[b]*0.11219974)+(0.39269908*1.86)
        plt.bar(pltx, this_rep[b], color=colors[b], yerr=this_rep_sd[b], edgecolor='gray', width=0.11219974, alpha=alpha[b], error_kw=dict(ecolor='gray', lw=1, alpha=alpha[b]))
    title = rows[a][0]
    if title == 'tphA2':
        title = 'K18074\nTerephthalate 1,2-dioxygenase alpha subunit'
    elif title == 'tphA3':
        title = 'K18075\nTerephthalate 1,2-dioxygenase beta subunit'
    elif title == 'tphB':
        title = 'K18076\n1,2-dihydroxy-3,5-cyclohexadiene-1,4-dicarboxylate\ndehydrogenase'
    elif title == 'PETase':
        title = 'K21104\nPETase'
    elif title == 'K00448':
        title  += '\nProtocatechuate 3,4-dioxygenase alpha subunit'
    elif title == 'K00449':
        title  += '\nProtocatechuate 3,4-dioxygenase beta subunit'
    plt.title(title, fontsize=18)
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    axes = ax.get_ylim()
    diff = axes[1]*0.3
    ax.set_ylim([0, axes[1]])
    m = axes[1]+(0.05*axes[1])
    ax.set_rorigin(-diff)
    plt.text(5.49778714+0.39269908, m, 'Inoculum', ha='center', va='center', fontsize=12, rotation=70)
    plt.text(5.49778714-0.39269908, m, 'Weathered PET', ha='center', va='center', fontsize=12, rotation=25)
    plt.text(5.49778714-(0.39269908*3), m, 'PET', ha='center', va='center', fontsize=12, rotation=-20)
    plt.text(5.49778714-(0.39269908*5), m, 'No carbon', ha='center', va='center', fontsize=12, rotation=-65)
    plt.text(5.49778714-(0.39269908*7), m, 'Amorphous PET planktonic', ha='center', va='center', fontsize=12, rotation=70)
    plt.text(5.49778714-(0.39269908*9), m, 'Amorphous PET biofilm', ha='center', va='center', fontsize=12, rotation=25)
    plt.text(5.49778714-(0.39269908*11), m, 'BHET', ha='center', va='center', fontsize=12, rotation=-20)
    plt.text(5.49778714-(0.39269908*13), m, 'Abundance (%)', ha='center', va='center', fontsize=12, rotation=-65)
    #plt.xticks([5.49778714+0.39269908, 5.49778714-0.39269908, 5.49778714-(0.39269908*3), 5.49778714-(0.39269908*5), 5.49778714-(0.39269908*7), 5.49778714-(0.39269908*9), 5.49778714-(0.39269908*11)], ['Inoculum', 'Weathered PET', 'PET', 'No carbon', 'Amorphous PET\nplanktonic', 'Amorphous PET\nbiofilm', 'BHET'], fontsize=8)
    plt.savefig(rows[a][0]+'.png', bbox_inches='tight', dpi=200)


    
    
    