import csv

name = 'pred_metagenome_unstrat_ordered.csv'
pways = 'EC_function.csv'
with open(name, 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)

with open(pways, 'rU') as f:
    pways = []
    for row in csv.reader(f):
        pways.append(row)

for a in range(len(rows)):
    for b in range(len(pways)):
        if rows[a][0] == pways[b][0]:
            rows[a] = [rows[a][0]]+[pways[b][1]]+rows[a][1:]

with open(name[:-4]+'_info.csv', 'w') as f:
    writer = csv.writer(f)
    for r in rows:
        writer.writerow(r)