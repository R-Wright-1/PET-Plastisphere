import csv

#names = [Day01LowCrysWater3	Day21BHET2	Day21BHET3	Day21ExtractionControl	Day30NoC1	Day30NoC2	Day30NoC3	Day30LowCrysWater1	Day30LowCrysWater2	Day30LowCrysWater3	Day30LowCrys1	Day01LowCrys1	Day30LowCrys2	Day30LowCrys3	Day30PET1	Day30PET2	Day30PET3	Day30WeatherPET1	Day30WeatherPET2	Day30WeatherPET3	Day30BHET1	Day30BHET2	Day01LowCrys2	Day30BHET3	Day30ExtractionControl	Day42NoC1	Day42NoC2	Day42NoC3	Day42LowCrysWater1	Day42LowCrysWater2	Day42LowCrysWater3	Day42LowCrys1	Day01LowCrys3	Day42LowCrys3	Day42PET2	Day42PET3	Day42WeatherPET1	Day42WeatherPET2	Day42WeatherPET3	Day42BHET1	Day42BHET2	Day42BHET3	Day01PET1	Day42ExtractionControl	Day01PET2	Day01PET3	Day01WeatherPET1	Day01WeatherPET2	Day01WeatherPET3	Inoc2	Day01BHET1	Day01BHET2	Day01BHET3	Day01ExtractionControl	Day03NoC1	Day03NoC2	Day03NoC3	Day03LowCrysWater1	Day03LowCrysWater2	Day03LowCrysWater3	Inoc3	Day03LowCrys1	Day03LowCrys2	Day03LowCrys3	Day03PET1	Day03PET2	Day03PET3	Day03WeatherPET1	Day03WeatherPET2	Day03WeatherPET3	Day03BHET1	Inoc4	Day03BHET2	Day03BHET3	Day03ExtractionControl	Day07NoC1	Day07NoC2	Day07NoC3	Day07LowCrysWater1	Day07LowCrysWater2	Day07LowCrysWater3	Day07LowCrys1	Day01NoC1	Day07LowCrys2	Day07LowCrys3	Day07PET1	Day07PET2	Day07PET3	Day07WeatherPET1	Day07WeatherPET2	Day07WeatherPET3	Day07BHET1	Day07BHET2	Day01NoC2	Day07BHET3	Day07ExtractionControl	Day14NoC1	Day14NoC2	Day14NoC3	Day14LowCrysWater1	Day14LowCrysWater2	Day14LowCrysWater3	Day14LowCrys1	Day14LowCrys2	Day01NoC3	Day14LowCrys3	Day14PET1	Day14PET2	Day14PET3	Day14WeatherPET1	Day14WeatherPET2	Day14WeatherPET3	Day14BHET1	Day14BHET2	Day14BHET3	Day01LowCrysWater1	Day14ExtractionControl	Day21NoC1	Day21NoC2	Day21NoC3	Day21LowCrysWater1	Day21LowCrysWater2	Day21LowCrysWater3	Day21LowCrys1	Day21LowCrys2	Day21LowCrys3	Day01LowCrysWater2	Day21PET1	Day21PET2	Day21PET3	Day21WeatherPET1	MiSeqControl1	MiSeqControl2	MiSeqControl3	Day21WeatherPET2	Day21WeatherPET3	Day21BHET1]

name = 'path_abun_unstrat.csv'
with open(name, 'rU') as f:
    rows = []
    for a in csv.reader(f):
        rows.append(a)
    
def transpose(rows):
    cols = []
    for a in range(len(rows[0])):
        col = []
        for b in range(len(rows)):
            col.append(rows[b][a])
        cols.append(col)
    return cols

cols = transpose(rows)
names, new_cols, controls = [], [], []
new_cols_ordered = []
for a in range(len(cols)):
    if a == 0:
        new_cols_ordered.append(cols[a])
    else:
        if cols[a][0][:3] != 'Day':
            controls.append(cols[a])
        else:
            if cols[a][0][5:] == 'ExtractionControl':
                controls.append(cols[a])
            else:
                new_cols.append(cols[a])
                names.append(cols[a][0][5:-1])
Z = [x for _,x in sorted(zip(names,new_cols))]

new_cols_ordered = new_cols_ordered+Z+controls
new_cols_ordered = transpose(new_cols_ordered)

with open(name[:-4]+'_ordered'+name[-4:], 'w') as f:
    writer = csv.writer(f)
    for a in new_cols_ordered:
        writer.writerow(a)