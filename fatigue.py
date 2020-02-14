import rainflow
import pandas as pd
import numpy as np
import math as m
import matplotlib.pyplot as plt
import glob

path = r"C:\Users\Joe\PycharmProjects\rainflow\excel\*.csv"

appended_data = pd.DataFrame()
for fname in glob.glob(path):
   data = pd.read_csv(fname)
   #print(data)
   appended_data = appended_data.append(data, ignore_index=True)

#print(appended_data.head)

y = appended_data.to_numpy()
y = np.reshape(y,(1, len(y)))
y = y[0]

print(y)

result = rainflow.count_cycles(y)

print(result)
