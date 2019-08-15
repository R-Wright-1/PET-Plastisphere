import csv
import matplotlib.pyplot as plt
import numpy

name = 'path_abun_unstrat_ordered_info.csv'
pways = ['CATECHOL-ORTHO-CLEAVAGE-PWY', 'PROTOCATECHUATE-ORTHO-CLEAVAGE-PWY', 'ALL-CHORISMATE-PWY', 
         'P161-PWY', 'P184-PWY', 'P23-PWY', 'PWY-3941', 'PWY-5178', 'PWY-5179', 'PWY-5180', 'PWY-5181', 
         'PWY-5182', 'PWY-5183', 'PWY-5415', 'PWY-5417', 'PWY-5419', 'PWY-5420', 'PWY-5430', 'PWY-5431', 
         'PWY-5676', 'PWY-5747', 'PWY-6182', 'PWY-6708', 'PWY-6957', 'PWY-7097', 'PWY-7098', 'BENZCOA-PWY']
pways = ['BENZCOA-PWY']
#pways = ['ALL-CHORISMATE-PWY']
colors = ['#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#7D3C98']
for pway in pways:
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
    
    title = using[1][1]
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
    
    plt.figure(figsize=(10,10))
    ax1 = plt.subplot(111)
    ax1.barh(x, mean, xerr=sd, capsize=3, color=colors, edgecolor='gray', ecolor='gray')
    ax1.set_ylim([0, x[-1]+1])
    ax1.set_xlim(left=0)
    ax1.set_title(title)
    xloc = [4, 12, 20, 28, 36, 44, 49]
    xlab = ['BHET', 'Low crystallinity biofilm', 'Low crystallinity planktonic', 'No carbon', 'PET', 'Weathered PET', 'Inoculum']
    ax1.set_xlabel('Pathway abundance')
    
    plt.sca(ax1)
    plt.yticks(xloc, xlab)
    plt.savefig(pway+'.png', bbox_inches='tight', dpi=300)
    plt.close()
    
    """
    ax1 = plt.subplot(111)
    ax1.barh(this_trt_x, this_trt_mean, xerr=this_trt_sd, align='center', capsize=3)
    ax1.set_yticks(this_trt_x)
    ax1.set_yticklabels(xlab)
    """