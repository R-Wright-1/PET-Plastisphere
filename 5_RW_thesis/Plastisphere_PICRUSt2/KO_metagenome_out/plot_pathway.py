import csv
import matplotlib.pyplot as plt
import numpy
from matplotlib.patches import Patch

name = 'pred_metagenome_unstrat_ordered.csv'
pways = ['K18068	', 'K18067', 'K04102', 'K18252', 'K00624', 'K18256', 'K18074', 'K18075', 'K18077', 'K18076', 'K04100', 'K04101', 'K10219', 'K10221', 'K16514', 'K10220', 'K16515', 'K10218', 'K00448', 'K00449', 'K01857', 'K01607', 'K14727', 'K01055', 'K14727','K00455', 'K10217', 'K01821', 'K01617', 'K15556', 'K15557', 'K15558', 'K01031', 'K01032']
descriptors = ['Phthalate 4,5-dioxygenase','Phthalate 4,5-dihydrodiol dehydrogenase','4,5-dihydroxyphthalate decarboxylase','Phthalate 3,4-dioxygenase','Phthalate 3,4-dihydrodiol dehydrogenase','3,4-dihydroxyphthalate decarboxylase','Terephthalate 1,2-dioxygenase', 'Terephthalate 1,2-dioxygenase', 'Terephthalate 1,2-dioxygenase','1,2-dihydroxy-3,5-cyclohexadiene-1,4-dicarboxylate dehydrogenase','Protocatechuate:oxygen 4,5-oxidoreductase', 'Protocatechuate 4,5-dioxygenase','2-hydroxy-4-carboxymuconate-6-semialdehyde dehydrogenase','2-pyrone-4,6-dicarboxylate dehydrogenase/hydrolase','Spontaneous/4-oxalomesaconate tautomerase','4-oxalomesaconate hydratase', '4-oxalomesaconate hydratase','4-carboxy-4-hydroxy-2-oxoadipate aldolase','Protocatechuate:oxygen 3,4-oxidoreductase', 'Protocatechuate:oxygen 3,4-oxidoreductase','3-carboxymuconate cycloisomerase','4-carboxymuconolactone decarboxylase', '4-carboxymuconolactone decarboxylase','B-ketoadipate-enol-lactone hydrolase', 'B-ketoadipate-enol-lactone hydrolase','Protocatechuate 2,3-dioxygenase','6-hydroxymuconate-6-semialdehyde dehydrogenase','4-oxalocrotonate tautomerase','2-oxo-3-hexenedioate decarboxylase', 'Phthalate transporter', 'Phthalate transporter', 'Phthalate transporter', '3-oxoadipate CoA transferase', '3-oxoadipate CoA transferase']
addtitle = ''
#pways = ['K00248', 'K00232', 'K00249', 'K00255', 'K09478', 'K07511', 'K07514', 'K07515', 'K00626', 'K07508']
#descriptors = ['butyryl-CoA dehydrogenase', 'acyl-CoA oxidase', 'acyl-CoA dehydrogenase', 'long-chain-acyl-CoA dehydrogenase', 'short/branched chain acyl-CoA dehydrogenase', 'enoyl-CoA hydratase', 'enoyl-CoA hydratase', 'enoyl-CoA hydratase', 'acetyl-CoA C-acetyltransferase', 'acetyl-CoA acyltransferase 2']
#pways = ['ALL-CHORISMATE-PWY']
#addtitle = 'Fatty'
colors = ['#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#7D3C98']
count = 0
countdes = 0
only_plot, only_plot_SD, only_plot_kegg = [], [], []
for pway in pways:
    count += 1
    with open(name, 'rU') as f:
        rows = []
        for row in csv.reader(f):
            rows.append(row)
    using = []
    for a in range(len(rows)):
        if a == 0:
            using.append(rows[a])
        elif rows[a][0] == pway:
            using.append(rows[a])
    #print(pway)
    title = addtitle+pway+': '+descriptors[countdes]
    countdes+=1
    if len(using) > 1:
        if len(title) > 150:
            for a in range(len(title)):
                if (a+1) % 150 == 0:
                    title = title[:a]+'\n'+title[a:]
        
        del using[0][0]
        del using[1][0]
        del using[0][0]
        del using[1][0]
        
        mean, sd, x = [], [], []
        this, prev = '', ''
        this_num = []
        xnum = 0
        this_trt_mean, this_trt_sd, this_trt_x = [], [], []
        this_trt = []
        xtrt = 0
        for a in range(len(using[0])):
            prev = this
            if this == '' and prev == '':
                this = using[0][a][:-1]
                prev = using[0][a][:-1]
            else:
                this = using[0][a][:-1]
            if this != prev or a == len(using[0])-1:
                this_num.append(float(using[1][a]))
                this_trt.append(float(using[1][a]))
                mean.append(numpy.mean(this_num))
                sd.append(numpy.std(this_num))
                xnum += 1
                x.append(xnum)
                this_num = []
                if this[5:] != prev[5:] or this == 'Inoc':
                    xnum += 1
                    x.append(xnum)
                    mean.append(0)
                    sd.append(0)
                    this_trt_mean.append(numpy.mean(this_trt))
                    this_trt_sd.append(numpy.std(this_trt))
                    xtrt += 1
                    this_trt_x.append(xtrt)
                    this_trt = []
            else:
                this_num.append(float(using[1][a]))
                this_trt.append(float(using[1][a]))
        """
        plt.figure(figsize=(10,10))
        ax1 = plt.subplot(111)
        ax1.barh(x, mean, xerr=sd, capsize=3, color=colors, edgecolor='gray', ecolor='gray')
        ax1.set_ylim([0, x[-1]+1])
        ax1.set_xlim(left=0)
        ax1.set_title(title)
        xloc = [4, 12, 20, 28, 36, 44, 49]
        xlab = ['BHET', 'Low crystallinity biofilm', 'Low crystallinity planktonic', 'No carbon', 'PET', 'Weathered PET', 'Inoculum']
        ax1.set_xlabel('Pathway abundance (%)')
        
        plt.sca(ax1)
        plt.yticks(xloc, xlab)
        plt.savefig(addtitle+str(count)+pway+'.png', bbox_inches='tight', dpi=300)
        plt.close()
        """
        
        x = [0]+x[:16]
        mean = [mean[48]]+[0]+mean[:15]
        sd = [sd[48]]+[0]+sd[:15]
        only_plot.append(mean)
        only_plot_SD.append(sd)
        only_plot_kegg.append(pway)
        #colors = ['#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#7D3C98']
        xloc = [4, 12, 17]
        xlab = ['BHET', 'Low\ncrystallinity\nbiofilm', 'Inoculum']
        """
        ax1.barh(x, mean, xerr=sd, color=colors, edgecolor='gray', error_kw=dict(lw=1, capsize=2, capthick=1, color='gray', alpha=0.8), ecolor='gray')
        ax1.set_xlabel('Pathway abundance (%)')
        plt.sca(ax1)
        plt.yticks(xloc, xlab)
        ax1.set_ylim([0, x[-1]+1])
        ax1.set_xlim(left=0)
        ax1.set_title(title)
        plt.savefig(addtitle+'BH_LC_'+str(count)+pway+'.png', bbox_inches='tight', dpi=300)
        plt.close()
        ax1 = plt.subplot(111)
        ax1.barh(this_trt_x, this_trt_mean, xerr=this_trt_sd, align='center', capsize=3)
        ax1.set_yticks(this_trt_x)
        ax1.set_yticklabels(xlab)
        """

plt.figure(figsize=(8.27,12))
fs = 10
ax1 = plt.subplot2grid((7,2), (0,0))
ax2 = plt.subplot2grid((7,2), (1,0))
ax3 = plt.subplot2grid((20,2), (0,0), rowspan=3)
ax3.set_title('K00448: Protocatechuate\n3,4-dioxygenase', fontsize=fs)
ax3.set_title('1', loc='left', fontsize=fs+2)
ax3b = plt.subplot2grid((20,2), (0,1), rowspan=3)
ax3b.set_title('K00449: Protocatechuate\n3,4-dioxygenase', fontsize=fs)
ax3b.set_title('1', loc='left', fontsize=fs+2)
ax4 = plt.subplot2grid((20,2), (4,0), rowspan=3)
ax4.set_title('K01857: 3-carboxymuconate\ncycloisomerase', fontsize=fs)
ax4.set_title('2', loc='left', fontsize=fs+2)
ax5 = plt.subplot2grid((20,2), (8,0), rowspan=3)
ax5.set_title('K01607: 4-carboxymuconolactone\ndecarboxylase', fontsize=fs)
ax5.set_title('3', loc='left', fontsize=fs+2)
ax5.set_ylabel('Abundance (%)', fontsize=fs)
ax5b = plt.subplot2grid((20,2), (10,1), rowspan=3)
ax5b.set_title('K14727: 4-carboxymuconolactone\ndecarboxylase', fontsize=fs)
ax5b.set_title('3/4', loc='left', fontsize=fs+2)
ax6 = plt.subplot2grid((20,2), (12,0), rowspan=3)
ax6.set_title(r'K01055: $\beta$-ketoadipate-enol-'+'\nlactone hydrolase', fontsize=fs)
ax6.set_title('4', loc='left', fontsize=fs+2)
#ax6b = plt.subplot2grid((5,2), (3,1))
#ax6b.set_title(r'K14727: $\beta$-ketoadipate-enol-'+'\nlactone hydrolase', fontsize=fs)
#ax6b.set_title('4', loc='left', fontsize=fs+2)
ax7 = plt.subplot2grid((20,2), (16,0), rowspan=3)
ax7.set_title('K01031: 3-oxoadipate\nCoA-transferase', fontsize=fs)
ax7.set_title('5', loc='left', fontsize=fs+2)
ax7b = plt.subplot2grid((20,2), (16,1), rowspan=3)
ax7b.set_title('K01032: 3-oxoadipate\nCoA-transferase', fontsize=fs)
ax7b.set_title('5', loc='left', fontsize=fs+2)
ax = [ax1, ax2, ax3, ax3b, ax4, ax5, ax5b, ax6, ax7, ax7b]
ko = ['', '', 'K00448', 'K00449', 'K01857', 'K01607', 'K14727', 'K01055', 'K01031', 'K01032']
colors = ['#7D3C98', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#ECFDDC', '#D0FDA9', '#C4FC92', '#A5FC58', '#30CE02', '#208C01', '#1B7101']

xloc = [0,1.5, 2.5,3.5,4.5,5.5,6.5,7.5, 9,10,11,12,13,14,15]
xlab = ['0','1', '3', '7', '14', '21', '30', '42', '1', '3', '7', '14', '21', '30', '42']
x2 = [0,1,1.5, 2.5,3.5,4.5,5.5,6.5,7.5,8.5,9,10,11,12,13,14,15]
          
for a in range(len(ko)):
    for b in range(len(only_plot_kegg)):
        if ko[a] == only_plot_kegg[b]:
            #print(ko[a], only_plot[b])
            ax[a].bar(x2, only_plot[b], yerr=only_plot_SD[b], color=colors, edgecolor='gray', error_kw=dict(lw=1, capsize=2, capthick=1, color='gray', alpha=0.8), ecolor='gray')
            #print(ko[a], a)
            plt.sca(ax[a])
            plt.xlim([-0.5, 15.5])
            plt.xticks(xloc, xlab, fontsize=fs-2)
            plt.xlabel('Day', fontsize=fs)

leg = [Patch(facecolor='#7D3C98', edgecolor='gray', label='      Inoculum'),Patch(facecolor='#013D64', edgecolor='gray', label='      BHET'), Patch(facecolor='#1B7101', edgecolor='gray', label='      Amorphous PET biofilm')] 
leg = ax4.legend(handles=leg, bbox_to_anchor=(1.1,1.1))
for patch in leg.get_patches():
    patch.set_width(15)
plt.subplots_adjust(wspace=0.2, hspace=10)
#plt.tight_layout()
plt.savefig('PICRUSt PET degradation.png', dpi=600)
