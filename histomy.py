import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('b.csv', header = None)

data.hist(bins='auto')
plt.xlabel("EPI (kWh/Sqm)", fontsize=28)
plt.ylabel("Number of Solutions (N)",fontsize=28)
plt.tick_params(axis='x',labelsize=26)
plt.tick_params(axis='y',labelsize=26)
plt.show()
plt.save()
