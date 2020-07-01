import matplotlib.pyplot as plt
import csv


simpers = ['Treatment2_LC_P_B_simper_means.csv', 'Treatment3_BHET_LCB_simper_means.csv', 'Treatment4_PET_simper_means.csv', 'Treatment5_PET_BHET_simper_means.csv']
group2 = [['Day01LowCrys', 'Day03LowCrys', 'Day07LowCrys', 'Day14LowCrys', 'Day21LowCrys', 'Day30LowCrys', 'Day42LowCrys'], ['Day01LowCrysWater', 'Day03LowCrysWater', 'Day07LowCrysWater', 'Day14LowCrysWater', 'Day21LowCrysWater', 'Day30LowCrysWater', 'Day42LowCrysWater']]
group3 = [['Day01BHET', 'Day03BHET', 'Day07BHET', 'Day14BHET', 'Day21BHET', 'Day30BHET', 'Day42BHET'], ['Day01LowCrys', 'Day03LowCrys', 'Day07LowCrys', 'Day14LowCrys', 'Day21LowCrys', 'Day30LowCrys', 'Day42LowCrys']]
group4 = [['Day01PET', 'Day03PET', 'Day07PET', 'Day14PET', 'Day21PET', 'Day30PET', 'Day42PET'], ['Day01WeatherPET', 'Day03WeatherPET', 'Day07WeatherPET', 'Day14WeatherPET', 'Day21WeatherPET', 'Day30WeatherPET', 'Day42WeatherPET']]
group5 = [['Day01LowCrys', 'Day03LowCrys', 'Day07LowCrys', 'Day14LowCrys', 'Day21LowCrys', 'Day30LowCrys', 'Day42LowCrys'], ['Day01PET', 'Day03PET', 'Day07PET', 'Day14PET', 'Day21PET', 'Day30PET', 'Day42PET'], ['Day01WeatherPET', 'Day03WeatherPET', 'Day07WeatherPET', 'Day14WeatherPET', 'Day21WeatherPET', 'Day30WeatherPET', 'Day42WeatherPET'], ['Day01BHET', 'Day03BHET', 'Day07BHET', 'Day14BHET', 'Day21BHET', 'Day30BHET', 'Day42BHET']]
groups = [group2, group3, group4, group5]

names = [['Amorphous PET biofilm', 'Amorphous PET planktonic'], ['BHET', 'Amorphous PET biofilm'], ['PET powder', 'Weathered PET powder'], ['Amorphous PET biofilm', 'PET powder', 'Weathered PET powder', 'BHET']]
ylabs = ['Amorphous PET\n Biofilm vs Planktonic\n\nDay', 'BHET vs Amorphous PET biofilm\n\nDay', 'PET powder vs Weathered PET powder\n\nDay', 'All PET vs BHET\n(Amorphous PET biofilm, Weathered PET powder, PET powder)\n\nDay']
colors = [['#3498DB', '#727FFD'], ['#E761FE', '#3498DB'], ['#FE9619', '#FCCF4D'], ['#3498DB', '#FE9619', '#FCCF4D', '#E761FE']]

#3498DB
#727FFD
#E761FE
#FE9619
#FCCF4D    
           
#y = [[1, 4, 7, 10, 13, 16, 19], [2, 5, 8, 11, 14, 17, 20]]
#y1 = [[1, 6, 11, 16, 21, 26, 31], [2, 7, 12, 17, 22, 27, 32], [3, 8, 13, 18, 23, 28, 33], [4, 9, 14, 19, 24, 29, 34]]
y = [[1, 2, 3, 4, 5, 6, 7], [9, 10, 11, 12, 13, 14, 15]]
y1 = [[1, 2, 3, 4, 5, 6, 7], [9, 10, 11, 12, 13, 14, 15], [17, 18, 19, 20, 21, 22, 23], [25, 26, 27, 28, 29, 30, 31]]
text = [['1', '3', '7', '14', '21', '30', '42'], ['1', '3', '7', '14', '21', '30', '42']]
text1 = [['1', '3', '7', '14', '21', '30', '42'], ['1', '3', '7', '14', '21', '30', '42'], ['1', '3', '7', '14', '21', '30', '42'], ['1', '3', '7', '14', '21', '30', '42']]
ylim = [0.5, 15.5]
ylim1 = 0.5, 31.5
rs = 1
firstax5 = ''

fig = plt.figure(figsize=(15,15))
for a in range(len(simpers)):
    if a == 3: rs = 2
    with open('over_time_all.csv', 'rU') as f:
        all_abun = []
        for row in csv.reader(f):
            all_abun.append(row)
    ax1 = plt.subplot2grid((5,5), (a,0), rowspan=rs)
    ax2 = plt.subplot2grid((5,5), (a,1), rowspan=rs)
    ax3 = plt.subplot2grid((5,5), (a,2), rowspan=rs)
    ax4 = plt.subplot2grid((5,5), (a,3), rowspan=rs)
    ax5 = plt.subplot2grid((5,5), (a,4), rowspan=rs)
    if a == 0:
        firstax5 = ax5
    ax1.set_ylabel(ylabs[a])
    axs = [ax1, ax2, ax3, ax4, ax5]
    with open(simpers[a], 'rU') as f:
        simper = []
        for row in csv.reader(f):
            simper.append(row)
    asv, cont, kstat, kp = [], [], [], []
    for b in range(5):
        b += 1
        asv.append(simper[b][0])
        cont.append(float(simper[b][1])*100)
        kstat.append(float(simper[b][-2]))
        kp.append(float(simper[b][-1]))
    new_abun = [all_abun[0]]
    for c in range(len(asv)):
        for d in range(len(all_abun)):
            if asv[c] == all_abun[d][0]:
                new_abun.append(all_abun[d])
    with open('Taxonomy.csv', 'rU') as f:
        tax = []
        for row in csv.reader(f):
            tax.append(row)
    print_tax = []
    for e in range(len(new_abun)):
        for f in range(len(tax)):
            if new_abun[e][0] == tax[f][0]:
                ntax = 'ASV'+str(int(tax[f][0][3:]))+': '
                del tax[f][0]
                tax[f].reverse()
                for g in range(len(tax[f])):
                    if tax[f][g] != 'NA':
                        if g == 0:
                            ntax += '$'+tax[f][g+1]+'$ $'+tax[f][g]+'$'
                        elif g == 1:
                            ntax += '$'+tax[f][g]+'$'
                        else:
                            ntax += tax[f][g]
                        break
                new_abun[e][0] = ntax
                print_tax.append(ntax)
    for z in range(len(print_tax)):
        txt = 'SIMPER: '+str(round(cont[z],2))+'%\n'
        txt += 'H='+str(round(kstat[z],2))+', $p$='+str(round(kp[z], 4))
        print_tax[z] += '\n'+txt
    group = groups[a]
    this_group = []
    if a == 3: y, text, ylim = y1, text1, ylim1
    this_ticks, this_loc = [], []
    for m in range(len(names[a])):
        this_loc += y[m]
        this_ticks += text[m]
    for h in range(len(group)):
        this = [[], [], [], [], []]
        for i in range(len(group[h])):
            for j in range(len(new_abun[0])):
                if group[h][i] == new_abun[0][j]:
                    for k in range(len(new_abun)):
                        if k > 0:
                            this[k-1].append(float(new_abun[k][j]))
        this_group.append(this)
        for l in range(len(this)):
            axs[l].barh(y[h], this[l], label=names[a][h], color=colors[a][h])
            plt.sca(axs[l])
            plt.yticks(this_loc, this_ticks)
            axs[l].set_ylim(ylim)
            axs[l].set_title(print_tax[l], fontsize=8)
            if a == 0:
                h1, l1 = axs[l].get_legend_handles_labels()
            elif a == 3:
                h2, l2 = axs[l].get_legend_handles_labels()
ax3.set_xlabel('Relative abundance')
firstax5.legend(h1+h2[1:], l1+l2[1:], bbox_to_anchor=(1.1,1))
plt.tight_layout()
plt.savefig('All simpers.png', bbox_inches='tight')
plt.close()