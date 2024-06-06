import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files
data = files.upload()
df = pd.read_csv('data.csv')
print(df)
df.describe()
df.info()
ages = df['age']

# Plotting the histogram
plt.figure(figsize=(10, 6))
plt.hist(ages, bins=20, color='lightgreen' , edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()