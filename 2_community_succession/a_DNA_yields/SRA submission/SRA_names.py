import csv
import os

d = '/Users/u1560915/Documents/OneDrive/PhD_Plastic_Oceans/Experiments/MiSeq2/Analysis_PET2/raw_files/'

files = sorted(os.listdir(d))
print(files)
name1, name2 = [], []

def get_num_r(f):
    num, count, r1 = 0, 0, 0
    for b in range(len(f)):
        if f[b] == '_' and count == 0:
            num = (f[1:b])
            count += 1
        elif f[b] == 'R':
            r1 = f[b]+f[b+1]
    return num, r1



for a in range(len(files)):
    for b in range(len(files)):
        n1, r1 = get_num_r(files[a])
        n2, r2 = get_num_r(files[b])
        if n1 == n2 and r1 != r2:
            adding = True
            for c in range(len(name1)):
                if name1[c] == files[a] or name1[c] == files[b]:
                    adding = False
            for d in range(len(name2)):
                if name2[d] == files[a] or name2[d] == files[b]:
                    adding = False
            if adding:
                name1.append(files[a])
                name2.append(files[b])

with open('r1r2.csv', 'w') as f:
    writer = csv.writer(f)
    for a in range(len(name1)):
        writer.writerow([name1[a], name2[a]])
    