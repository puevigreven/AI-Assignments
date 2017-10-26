import pandas as pd
import numpy as np
# data = pd.read_csv('train.txt', sep=":")

df = pd.read_table('train.txt', delimiter=':', names=('A', 'B', 'C'))

print df['C']

df['C'].to_csv("trainC.csv", index = False , index_label = None)

