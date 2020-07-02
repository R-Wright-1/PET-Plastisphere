import csv

fasta = 'Hcamp.faa'

with open(fasta, 'rU') as f:
    rows = []
    for row in csv.reader(f):
        rows.append(row)

