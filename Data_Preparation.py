import pandas as pd
import numpy as np
import random

data = pd.read_csv('/home/clytius/Documents/ML temp codes/Project/Data/m33p1.dat', header=None)
dat = data.to_numpy()
data_array = []
for i in range(18394):
    data_array.append(dat[i+6][0].split('|'))
    data_array[i].pop(1)
    for j in range(3):
        data_array[i].pop(7)
    if (float(data_array[i][11]) > 4):
        data_array[i].append(1)
    else:
        data_array[i].append(0)

for p in range(18394):
    for q in range(18393):
        if(float(data_array[q][11]) < float(data_array[q+1][11])):
            temp = data_array[q]
            data_array[q] = data_array[q+1]
            data_array[q+1] = temp

final_data = []

random_var_list = []
random_non_var_list = []
for m in range(750):
    r_v = random.randint(0,811)
    if r_v not in random_var_list: random_var_list.append(r_v)
    final_data.append(data_array[r_v])
for n in range(4000):
    r_n_v = random.randint(812,18394)
    if r_n_v not in random_non_var_list: random_non_var_list.append(r_n_v)
    final_data.append(data_array[r_n_v])

index_list = []
for t in range(4750):
    index_list.append(t+1)
columns = ['seq', 'Jmag', 'e_Jmag', 'Hmag', 'e_Hmag', 'Kmag', 'e_Kmag', 'chi', 'sharp', 'Jvar', 'Kvar', 'Lvar', 'Kamp', 'Var_Status']
df = pd.DataFrame(final_data, index_list, columns)
df.to_csv('Data.csv')