import csv
import numpy
from skbio import DistanceMatrix as dm
from skbio.stats.distance import anosim
from skbio.stats.distance import permanova
from skbio.stats.distance import permdisp
from scipy.spatial.distance import braycurtis
from scipy.spatial.distance import euclidean

fn = 'all_samples.csv'
with open(fn, 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)

sample_names_long = rows[0][1:]
sample_names = rows[1][1:]
samples = []
for a in range(len(rows[0])):
    if a > 0:
        this_sample = []
        for b in range(len(rows)):
            if b > 1:
                this_sample.append(float(rows[b][a]))
        samples.append(this_sample)

sam_dm = dm.from_iterable(samples, metric=braycurtis)
pdisp = permdisp(sam_dm, sample_names, column=None, test='median', permutations=999)
print(pdisp)
asim = anosim(sam_dm, sample_names, column=None, permutations=999)
print(asim)
perm = permanova(sam_dm, sample_names, column=None, permutations=999)
print(perm)

"""
#run these to get values for each treatment
only_samples = ['Inoc', 'NoC', 'LowCrysWater', 'LowCrys', 'PET', 'WeatherPET', 'BHET']
for a in range(len(only_samples)):
    for b in range(len(only_samples)):
        if only_samples[a] != only_samples[b]:
            new_samples, new_names = [], []
            for c in range(len(sample_names)):
                if sample_names[c] == only_samples[a] or sample_names[c] == only_samples[b]:
                    new_samples.append(samples[c])
                    new_names.append(sample_names[c])
            sam_dm = dm.from_iterable(new_samples, metric=euclidean)
            print(only_samples[a], 'vs', only_samples[b])
            asim = permanova(sam_dm, new_names, column=None, permutations=999)
            print(asim)
"""