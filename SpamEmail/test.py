import pandas as pd
import numpy as np

dataset = pd.read_csv('spambase/spambase.data')
dataset = dataset.values
cols = dataset.shape[1]-1
X = dataset[:,0:cols]
Y = dataset[:,cols]
print(X)
print(Y)
