# import
import pandas as pd
import matplotlib.pyplot as plt

# read the xlsx file. Our working dir is /app
path_container_data = 'data.xlsx'
data = pd.read_excel(path_container_data)

# plot
# plot using a non-interactive backend
plt.switch_backend('agg')
plt.plot(data['x'], data['y'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('x vs y')
plt.savefig('/app/figure.png')  # Enregistrer la figure dans un fichier

# Terminer le script
plt.close()
