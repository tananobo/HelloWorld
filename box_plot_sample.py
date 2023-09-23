import matplotlib.pyplot as plt                                               
import numpy as np 

np.random.seed(0)                                                             
data = [np.random.normal(0, 1, 100), np.random.normal(1, 1, 100),             
np.random.normal(2, 1, 100)] 

fig, ax = plt.subplots()            
ax.boxplot(data, widths=0.5, patch_artist=True, showfliers=False, boxprops={'alpha':0.5})

for i, d in enumerate(data):                                
    jitter = np.random.normal(0, 0.1, len(d)) 
    ax.scatter(np.repeat(i+1, len(d)) + jitter, d, color='black', alpha=0.5, s=1, zorder=10)

ax.set_xticklabels(['Level 1', 'Level 2', 'Level 3'])
ax.set_ylabel('Value')
ax.set_title('Boxplot with Jitter Plot')

plt.show()