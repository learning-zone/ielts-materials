import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('bands.txt', sep=",", skipinitialspace=True,
                 dtype={'Part': str, 'Test': str, 'Band': float})

read = df[df['Part'] == 'R']
listening = df[df['Part'] == 'L']

fig, axes = plt.subplots(nrows=1, ncols=2)
Bands = list(map(str, np.arange(7, 9.5, 0.5)))
read.plot(x='Test', y='Band', ax=axes[0], kind='line', ylim=[6.5, 9], label='Reading')
listening.plot(x='Test', y='Band', ax=axes[1], kind='line', ylim=[6, 8.5], label='Listening')

axes[0].set_xlabel("Test No.")
axes[1].set_xlabel("Test No.")
axes[0].set_ylabel("Band")
# axes[0].set_xticks(read['Test'].index)
axes[0].set_xticklabels(read['Test'].values)
axes[1].set_xticklabels(listening['Test'].values)

plt.tight_layout()
plt.savefig('band.png')
# plt.show()