import pandas as pd
import numpy as np
# data = pd.read_csv('train.txt', sep=":")

df = pd.read_table('train.txt', delimiter=':', names=('A', 'B', 'C'))

# print df['C']

grp = df.groupby(['A', 'C']).count().reset_index()
df1 = df[df['A'] == "ABBR"]
df2 = df[df['A'] == "HUM"]
df3 = df[df['A'] == "DESC"]
df4 = df[df['A'] == "LOC"]
df5 = df[df['A'] == "NUM"]
df6 = df[df['A'] == "ENTY"]

# df2 = df[]
print df1


# print grp
# data = data.set_index(['name','take'])

# a =  grp.get_group('A')
# print a
# print grp
df1['C'].to_csv("ABBR-Group.txt", index = False , index_label = None)
df2['C'].to_csv("HUM-Group.txt", index = False , index_label = None)
df3['C'].to_csv("DESC-Group.txt", index = False , index_label = None)
df4['C'].to_csv("LOC-Group.txt", index = False , index_label = None)
df5['C'].to_csv("NUM-Group.txt", index = False , index_label = None)
df6['C'].to_csv("ENTY-Group.txt", index = False , index_label = None)

