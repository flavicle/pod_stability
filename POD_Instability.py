import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

A02_data = 'AMZN_BLQ1_paKivaA02.csv'
A03_data = 'AMZN_BLQ1_paKivaA03.csv'
A04_data = 'AMZN_BLQ1_paKivaA04.csv'

print ("importing data...")

if os.path.isfile('AMZN_BLQ1_paKivaA02.csv') and os.path.isfile('AMZN_BLQ1_paKivaA04.csv'):
    
    A02 = pd.read_csv(A02_data, header=0)
    A03 = pd.read_csv(A03_data, header=0)
    A04 = pd.read_csv(A04_data, header=0)

    df02 = pd.DataFrame(A02)
    df03 = pd.DataFrame(A03)
    df04 = pd.DataFrame(A04)

else:
    print("file doesn't exist! Please try again.")
    exit()


cols = [0,2,4,6]
df02 = df02[df02.columns[cols]]
df03 = df03[df03.columns[cols]]
df04 = df04[df04.columns[cols]]

A02_ID = df02[df02.columns[0]].to_numpy()
A02_mass = df02[df02.columns[1]].to_numpy()
A02_height = df02[df02.columns[2]].to_numpy()
A02_horiz = df02[df02.columns[3]].to_numpy()

A03_ID = df03[df03.columns[0]].to_numpy()
A03_mass = df03[df03.columns[1]].to_numpy()
A03_height = df03[df03.columns[2]].to_numpy()
A03_horiz = df03[df03.columns[3]].to_numpy()

A04_ID = df04[df04.columns[0]].to_numpy()
A04_mass = df04[df04.columns[1]].to_numpy()
A04_height = df04[df04.columns[2]].to_numpy()
A04_horiz = df04[df04.columns[3]].to_numpy()

print("plotting relevant data")

fig, ((ax1, ax2, ax3),(ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3,3)

fig.tight_layout(pad=1.5)

ax1.hist(A02_mass, bins=100, range=(0,100))
ax2.hist(A02_height, bins=100, range=(50,100))
ax3.hist(A02_horiz, bins=100, range=(0,100))
ax4.hist(A03_mass, bins=100, range=(0,100))
ax5.hist(A03_height, bins=100, range=(50,100))
ax6.hist(A03_horiz, bins=100, range=(0,100))
ax7.hist(A04_mass, bins=100, range=(0,100))
ax8.hist(A04_height, bins=100, range=(50,100))
ax9.hist(A04_horiz, bins=100, range=(0,100))

ax1.set_title('A02 Pod mass as % of limit', fontdict={'fontsize': 10, 'fontweight': 'medium'})
ax2.set_title('A02 CM height as % of limit', fontdict={'fontsize': 10, 'fontweight': 'medium'})
ax3.set_title('A02 CM horizontal displacement as % of limit', fontdict={'fontsize': 10, 'fontweight': 'medium'})
ax4.set_title('A03 Pod mass as % of limit', fontdict={'fontsize': 10, 'fontweight': 'medium'})
ax5.set_title('A03 CM height as % of limit', fontdict={'fontsize': 10, 'fontweight': 'medium'})
ax6.set_title('A03 CM horizontal displacement as % of limit', fontdict={'fontsize': 10, 'fontweight': 'medium'})
ax7.set_title('A04 Pod mass as % of limit', fontdict={'fontsize': 10, 'fontweight': 'medium'})
ax8.set_title('A04 CM height as % of limit', fontdict={'fontsize': 10, 'fontweight': 'medium'})
ax9.set_title('A04 CM horizontal displacement as % of limit', fontdict={'fontsize': 10, 'fontweight': 'medium'})

plt.show()

input()

print("execution: COMPLETED")