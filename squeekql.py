# %%
import pandas as pd
from progress.bar import Bar

# %%
import sqlite3

# %%
db = sqlite3.connect('bikedata.db')
bar = Bar('Loading', fill='~', max=5)

for i in range(4, 9):
    url = f'https://s3.amazonaws.com/tripdata/20170{i}-citibike-tripdata.csv.zip'
    df = pd.read_csv(url)
    df.to_sql('tripdata', db, if_exists='append')
    bar.next()

bar.finish()
db.close()

# %%
db = sqlite3.connect('bikedata.db')
db.execute('DROP TABLE tripdata')


# %%
import pandas as pd
from progress.bar import Bar
import sqlite3

filename = 'SN282E_LMRK005IMU-490-15-900_Atp_13Jul20_194404_summary.csv'
filename = filename.replace('-', '_')
filename = filename.replace(' ', '_')
print(filename)

# %%
db = sqlite3.connect('testdata.db')
df = pd.read_csv(filename, index_col=False)
df.rename(columns={'MSGCOUNT': 'ACTION'}, inplace=True)
df.drop('AHRS_STATUS', axis=1, inplace=True)
cols = df.columns

print(cols)
gyrs = []
accs = []
tmps = []
for c in cols:
    if 'GYR' in c and str(c[-1]).isnumeric():
        gyrs.append(c)
    elif 'ACC' in c and str(c[-1]).isnumeric():
        accs.append(c)
    if 'TEMP' in c and str(c[-1]).isnumeric():
        tmps.append(c)

print(gyrs)
print(accs)
print(tmps)

id_v = [c for c in cols if c not in gyrs and c not in accs and c not in tmps]
gyr_n = [c for c in cols if c not in accs and c not in tmps]
acc_n = [c for c in cols if c not in gyrs and c not in tmps]
tmp_n = [c for c in cols if c not in accs and c not in gyrs]

df_g = df.loc[:, gyr_n]
df_a = df.loc[:, acc_n]
df_t = df.loc[:, tmp_n]

df_g = df_g.melt(id_vars=id_v, value_vars=gyrs)
df_a = df_a.melt(id_vars=id_v, value_vars=accs)
df_t = df_t.melt(id_vars=id_v, value_vars=tmps)

df_g['AXIS'] = df_g.variable.str[0]
df_g['ELEM'] = df_g.variable.str[1:-1]
df_g['SENSNo'] = df_g.variable.str[-1]

df_a['AXIS'] = df_a.variable.str[0]
df_a['ELEM'] = df_a.variable.str[1:-1]
df_a['SENSNo'] = df_a.variable.str[-1]

df_t['AXIS'] = 'T'
df_t['ELEM'] = df_t.variable.str[0:-1]
df_t['SENSNo'] = df_t.variable.str[-1]

df = pd.concat([df_g, df_a, df_t])


# %%
df.to_sql('atpdata', db, if_exists='append')


# %%
