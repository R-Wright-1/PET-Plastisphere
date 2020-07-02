import csv
import numpy

fi = 'all_samples.csv'
tax = 'Taxonomy.csv'
sn = 'sample_names.csv'
new_file = 'all_samples_log.csv'
transform_only = 'all_samples_transform.csv'

rel_abun = False
log_trans = True
trans_R = True
rem = True
mi = 10

#funtion to transpose rows to columns or vice verse
def transpose(rows):
    cols = []
    for a in range(len(rows[0])):
        col = []
        for b in range(len(rows)):
            col.append(rows[b][a])
        cols.append(col)
    return cols

#open files
with open(fi, 'rU') as f:
    fi = []
    for row in csv.reader(f):
        fi.append(row)

with open(tax, 'rU') as f:
    tax = []
    for row in csv.reader(f):
        tax.append(row)

with open(sn, 'rU') as f:
    sn = []
    for row in csv.reader(f):
        sn.append(row)

#change ASV names in original file to best classification from tax file (i.e. species if possible, or the lowest)
for a in range(len(fi)):
    if a > 0:
        tax[a].reverse()
        fi[a][0] = 'ASV'+str(int(fi[a][0][3:]))+' '
        for b in range(len(tax[a])):
            if tax[a][b] != 'NA':
                if b == 0:
                    tax[a] = tax[a][b+1]+' '+tax[a][b]
                elif b == 1:
                    tax[a] = tax[a][b]
                else:
                    tax[a] = tax[a][b]
                break
        fi[a][0] += tax[a]

#turn all numbers into floats
for a in range(len(fi)):
    for b in range(len(fi[a])):
        if a > 0 and b > 0:
            fi[a][b] = float(fi[a][b])
#remove low abundance
if rem:
    new_fi = [fi[0]]
    for a in range(len(fi)):
        if a > 0:
            if max(fi[a][1:]) > mi:
                new_fi.append(fi[a])
    print(len(fi), len(new_fi))
    fi = new_fi
    
#if log transforming, do this:
for a in range(len(fi)):
    for b in range(len(fi[a])):
        if a > 0 and b > 0:
            if fi[a][b] == 0: 
                fi[a][b] = 0.0001
            fi[a][b] = numpy.log(fi[a][b])

#if getting relative abundance then do this
if rel_abun:
    fi = transpose(fi)
    for a in range(len(fi)):
        if a > 0:
            s = sum(fi[a][1:])
            for b in range(len(fi[a])):
                if b > 0:
                    fi[a][b] = (fi[a][b]/s)*100
    fi = transpose(fi)

#write a file of the changes so far
with open(transform_only, 'w') as f:
    writer = csv.writer(f)
    for row in fi:
        writer.writerow(row)

#get treatment names from the sample names file and add these in with treatment, time and replicate number details
fi = transpose(fi)
trt, time, rep = ['Treatment'], ['Time'], ['Replicate']
new = [fi[0]]
for a in range(len(sn)):
    for b in range(len(fi)):
        if sn[a][0] == fi[b][0]:
            fi[b][0] = sn[a][1]
            new.append(fi[b])
            trt.append(sn[a][2])
            time.append(int(sn[a][3]))
            rep.append(int(sn[a][4]))
fi = transpose(new)
#fi = [fi[0], trt, time, rep]+fi[1:]
print(trt)
print(time)
print(rep)

#if we're transposing this for R, then do this
if trans_R:
    fi = transpose(fi)

#write this new file
with open(new_file, 'w') as f:
    writer = csv.writer(f)
    for row in fi:
        writer.writerow(row)