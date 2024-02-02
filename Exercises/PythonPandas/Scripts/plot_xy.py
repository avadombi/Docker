# import
import pandas as pd
import matplotlib.pyplot as plt

# read the xlsx file
path_container_data = '/app/data/data.xlsx'
data = pd.read_excel(path_container_data)

# plot
data.plot(x='x', y='y', kind='line')
plt.show()
