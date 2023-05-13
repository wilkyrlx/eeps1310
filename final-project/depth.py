import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

selector = 1               # 0 for New York and Pennsylvania, 1 for Maine and New Hampshire
filepath1 = ""      # aq1
filepathE = ""      #aq2
filepath2 = ""      #plant1
filepath3 = ""      #plant2
state = ""

if selector == 0:
    # files for Pennsylvania
    filepath1 = 'final-project\\data-depth\\penn-700.csv'
    filepathE = 'final-project\\data-depth\\penn-146.csv'
    filepath2 = 'final-project\\data-depth\\penn-820.csv'
    filepath3 = 'final-project\\data-depth\\penn-929.csv'
    state = "Pennsylvania"
else:
    # files for Maine
    filepath1 = 'final-project\\data-depth\\me-916.csv'
    filepathE = 'final-project\\data-depth\\me-887.csv'
    filepath2 = 'final-project\\data-depth\\me-1135.csv'
    filepath3 = 'final-project\\data-depth\\me-807.csv'
    state = "Maine"

filepaths = [filepath1, filepathE, filepath2, filepath3]
labels = ['Aquifer only 1', 'Aquifer only 2', 'Plant 1', 'Plant 2']

fig, ax = plt.subplots()
for i, filepath in enumerate(filepaths):
    # Load the tab-delimited file into a dataframe
    df = pd.read_csv(filepath, sep='\t')
    df_month6 = df[(df['month_nu'] == 6) & (df['year_nu'] > 2002)]
    ax.scatter(df_month6['year_nu'], df_month6['mean_va'], label=f'{labels[i]}')

    slope, intercept = np.polyfit(df_month6['year_nu'], df_month6['mean_va'], 1)
    ax.plot(df_month6['year_nu'], slope*df_month6['year_nu'] + intercept, '--')
    print(f"The {i+1} slope is {slope}")


box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.invert_yaxis()   # invert, since this measures depth to groundwater

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title(f'Average Depth to Groundwater in {state}')
plt.xlabel('Year')
plt.ylabel('Depth to Groundwater (ft)')
plt.show()