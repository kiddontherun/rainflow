import pandas as pd
import numpy as np
import math as m
import matplotlib.pyplot as plt
import glob
import rainflow as rn

path = r"C:\Users\Joe\PycharmProjects\rainflow\excel\*.csv"

appended_data = pd.DataFrame()
for fname in glob.glob(path):
   data = pd.read_csv(fname)
   #print(data)
   appended_data = appended_data.append(data, ignore_index=True)

#print(appended_data.head)

y = appended_data.to_numpy()

print(y)

rain = rn.count_cycles(y)

print(rain)