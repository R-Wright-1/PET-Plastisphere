import csv
import matplotlib.pyplot as plt
import numpy

name = 'pred_metagenome_unstrat_ordered_info.csv'
pways = ['EC:1.13.11.3', 'EC:1.13.11.8', 'EC:1.14.12.7', 'EC:4.1.1.55',
         'EC:1.1.1.312', 'EC:1.1.1.77', 'EC:1.2.1.21', 'EC:1.1.3.15']
pways = ['EC:1.14.12.7', 'EC:1.3.1.64', 'EC:4.1.1.55', 
         'EC:1.13.11.8', 'EC:1.1.1.312', 'EC:3.1.1.57', 'EC:5.3.2.8', 
         'EC:4.2.1.83', 'EC:4.1.3.17', 'EC:1.13.11.3', 'EC:5.5.1.2', 'EC:4.1.1.44', 'EC:3.1.1.24', 
         'EC:1.2.1.85', 'EC:5.3.2.6', 'EC:4.1.1.77']
#pways = ['ALL-CHORISMATE-PWY']
colors = ['#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#EBF6FD', '#C5E7FD', '#8FD2FD', '#4FB7F9', '#029AFA', '#016DB1', '#013D64', 'w', '#7D3C98']
count = 1
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
    print(pway)
    title = pway+': '+using[1][1]
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
    plt.savefig(str(count)+pway+'.png', bbox_inches='tight', dpi=300)
    plt.close()
    count += 1
    """
    ax1 = plt.subplot(111)
    ax1.barh(this_trt_x, this_trt_mean, xerr=this_trt_sd, align='center', capsize=3)
    ax1.set_yticks(this_trt_x)
    ax1.set_yticklabels(xlab)
    """