from math import pi, sqrt
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.special import factorial
import scipy.stats as stat
import math

NSTA_data = 'UDQ-27292_NSTQ%.csv'

if os.path.isfile(NSTA_data):

    NSTA = pd.read_csv(NSTA_data)
    NSTA_df = pd.DataFrame(NSTA)
    NSTA_df = NSTA_df.dropna()

else:
    print("no data found!")
    exit()


print(NSTA_df.columns)

#input()

maxwell = stat.maxwell

data_nord = NSTA_df[NSTA_df.columns[1]].to_numpy()
data_sud = NSTA_df[NSTA_df.columns[4]].to_numpy()
data_est = NSTA_df[NSTA_df.columns[7]].to_numpy()
data_ideal = maxwell.rvs(loc=0, scale=4.7, size=10000)


params_nord = maxwell.fit(data_nord, floc=0)
params_sud = maxwell.fit(data_sud, floc=0)
params_est = maxwell.fit(data_est, floc=0)
params_ideal = maxwell.fit(data_ideal, floc=0)

mean = [params_nord[1]*2*sqrt(2/math.pi), params_sud[1]*2*sqrt(2/math.pi), params_est[1]*2*sqrt(2/math.pi)]
mode = [params_nord[1]*sqrt(2), params_sud[1]*sqrt(2), params_est[1]*sqrt(2)]

plt.figure(figsize=(8,6))
plt.hist(data_nord, bins=100, density=True, alpha=0.5, label='A02 North', color="cyan")
plt.hist(data_sud, bins=100, density=True, alpha=0.5, label='A03 North', color="silver")
plt.hist(data_est, bins=100, density=True, alpha=0.5, label='A04 North', color="pink")
plt.hist(data_ideal, bins=100, density=True, alpha=0.4, label='Benchmark limit', color="black")

plt.xlabel("NSTA %", size=14)
plt.ylabel("Count", size=14)

x = np.linspace(0, 100, 1000)
plt.plot(x, maxwell.pdf(x, *params_nord), lw=1.5, label='A02 north fit', color="darkcyan")
plt.plot(x, maxwell.pdf(x, *params_sud), lw=1.5, label='A03 north fit', color="dimgrey")
plt.plot(x, maxwell.pdf(x, *params_est), lw=1.5, label='A04 north fit', color="red")
#plt.plot(x, maxwell.pdf(x, *params_ideal), lw=1.5, label='benchmark limit fit', color='k')
plt.legend(loc='upper right')

print(mode)

plt.show()