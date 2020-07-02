import csv
import matplotlib.pyplot as plt

labels = ['No carbon', 'BHET', 'Amorphous PET biofilm', 'Amorphous PET planktonic', 'PET powder', 'Weathered PET powder']
markers = ['o', 'p', 's', '^', '1', 'x']
colors = ['k', 'orange', 'm', 'r', 'b', 'g']

inoc = [4.362]
inoc_sd = [1.002939679]

nc = [0.392666667, 0.3996, 0.690666667, 0.409866667, 0.4144, 0.666666667, 1.026666667]
nc_sd = [0.08960744, 0.033401796, 0.165618034, 0.077092499, 0.11047244, 0.071703092, 0.176378381]

lcpp = [0.437733333, 0.714666667, 1.041333333, 0.844, 0.928, 1.045333333, 1.638666667]
lcpp_sd = [0.114435193, 0.282342582, 0.380448858, 0.068234888, 0.052, 0.170098011, 0.332393341]

lcpb = [0, 0, 0.006666667, 0.007866667, 0, 0.031333333, 0.022933333]
lcpb_sd = [0, 0, 0.011547005, 0.013625466, 0, 0.006744875, 0.002663331]

pp = [0.4696, 0.585333333, 0.781333333, 1.170666667, 1.182666667, 2.952, 3.105333333]
pp_sd = [0.127541679, 0.112593665, 0.128768526, 0.062524662, 0.045489926, 0.492, 1.310940629]

wpp = [0.349066667, 0.5044, 0.728, 1.441333333, 1.276, 2.321333333, 2.801333333]
wpp_sd = [0.129743953, 0.113844104, 0.207846097, 0.565435525, 0.130782262, 0.002309401, 0.278002398]

bhet = [0.197066667, 0.48, 0.648, 0.906666667, 0.722666667, 0.801333333, 0.677333333]
bhet_sd = [0.07340445, 0.064373908, 0.181592951, 0.078008547, 0.206701072, 0.207164991, 0.556809962]

x = [1, 3, 7, 14, 21, 30, 42]
ax1 = plt.subplot(111)

ax1.errorbar(x, nc, yerr=nc_sd, color=colors[0], marker=markers[0], label=labels[0], capsize=2)
ax1.errorbar(x, bhet, yerr=bhet_sd, color=colors[1], marker=markers[1], label=labels[1], capsize=2)
ax1.errorbar(x, lcpb, yerr=lcpb_sd, color=colors[2], marker=markers[2], label=labels[2], capsize=2)
ax1.errorbar(x, lcpp, yerr=lcpp_sd, color=colors[3], marker=markers[3], label=labels[3], capsize=2)
ax1.errorbar(x, pp, yerr=pp_sd, color=colors[4], marker=markers[4], label=labels[4], capsize=2)
ax1.errorbar(x, wpp, yerr=wpp_sd, color=colors[5], marker=markers[5], label=labels[5], capsize=2)

ax1.legend(loc='best')
ax1.set_ylabel('DNA concentration ng '+'$\mu$'+'L$^{-1}$')
ax1.set_xlabel('Day')
ax1.set_xticks(x)
plt.savefig('DNA concentrations.png', dpi=300, bbox_inches='tight')