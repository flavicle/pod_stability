from math import pi, sqrt
import os
from matplotlib import axes
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.special import factorial
import scipy.stats as stat
import math

maxwell = stat.maxwell

NSTA_0607 = 'UDQ-0607-late.csv'; NSTA_0608 = 'UDQ-0608-late.csv'
NSTA_0609 = 'UDQ-0609-late.csv'; NSTA_0610 = 'UDQ-0610-late.csv'
NSTA_0611 = 'UDQ-0611-late.csv'; NSTA_0613 = 'UDQ-0613-late.csv'

NSTA_07 = pd.read_csv(NSTA_0607); NSTA_08 = pd.read_csv(NSTA_0608)
NSTA_09 = pd.read_csv(NSTA_0609); NSTA_10 = pd.read_csv(NSTA_0610)
NSTA_11 = pd.read_csv(NSTA_0611); NSTA_13 = pd.read_csv(NSTA_0613)

NSTA_data = [NSTA_07, NSTA_08, NSTA_09, NSTA_10, NSTA_11, NSTA_13]
dates=['06-07-2021', '06-08-2021', '06-09-2021', '06-10-2021', '06-11-2021', '06-13-2021']
floor = ['A02', 'A03', 'A04']
side = ['north, south, east']

params_north = list(); params_south = list(); params_east = list()

data_ideal = maxwell.rvs(loc=0, scale=4.7, size=100)
params_ideal = maxwell.fit(data_ideal, floc=0)

x = np.linspace(0, 100, 1000)

fig, ((ax1,ax2,ax3), (ax4,ax5,ax6))=plt.subplots(2,3)
fig.tight_layout(pad=1.5)

axi = [ax1,ax2,ax3,ax4,ax5,ax6]

counter=-1
for i in NSTA_data:
    counter=counter+1
    i=pd.DataFrame(i)
    i = i.dropna()

    axi[counter].hist(i[i.columns[7]],bins=25, range=(0,100), density=1, alpha=0.5, label='A04 north', color='cyan')
    axi[counter].hist(i[i.columns[8]],bins=25, range=(0,100), density=1, alpha=0.5, label='A04 south', color='bisque')
    axi[counter].hist(i[i.columns[9]],bins=25, range=(0,100), density=1, alpha=0.5, label='A04 east', color='pink')
    #axi[counter].hist(data_ideal, bins=25, range=(0,100), density=1, alpha=0.2, label='Benchmark limit', color="black")

    params_north.append(maxwell.fit(i[i.columns[7]].to_numpy(), floc=0))
    params_south.append(maxwell.fit(i[i.columns[8]].to_numpy(), floc=0))
    params_east.append(maxwell.fit(i[i.columns[9]].to_numpy(), floc=0))

    axi[counter].plot(x, maxwell.pdf(x, *params_north[counter]), lw=1.5, label='A04 north fit', color="darkcyan")
    axi[counter].plot(x, maxwell.pdf(x, *params_south[counter]), lw=1.5, label='A04 south fit', color="orange")
    axi[counter].plot(x, maxwell.pdf(x, *params_east[counter]), lw=1.5, label='A04 east fit', color="red")
    #axi[counter].plot(x, maxwell.pdf(x, *params_ideal), lw=1.5, label='benchmark limit', color='k')

    axi[counter].set_title(dates[counter])

plt.legend(loc='upper right')
plt.show()


X=list(); Y_4N=list(); Y_4S=list(); Y_4E=list()

for i in range(0, len(params_north)):
    X.append(dates[i])
    Y_4N.append(params_north[i][1])
    Y_4S.append(params_south[i][1])
    Y_4E.append(params_east[i][1])
    

plt.plot(X, Y_4N, 'b--', label='A04 north')
plt.plot(X, Y_4S, 'r--', label='A04 south')
plt.plot(X, Y_4E, 'g--', label='A04 east')
plt.legend(loc='upper left')
plt.show()
