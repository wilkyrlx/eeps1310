import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filepath1 = 'final-project\\data-depth\\penn-700.csv'
filepath2 = 'final-project\\data-depth\\penn-820.csv'
filepath3 = 'final-project\\data-depth\\penn-929.csv'

filepaths = [filepath1, filepath2, filepath3]

fig, ax = plt.subplots()
for filepath in filepaths:
    # Load the tab-delimited file into a dataframe
    df = pd.read_csv(filepath, sep='\t')
    df_month6 = df[(df['month_nu'] == 6) & (df['year_nu'] > 2002)]
    ax.scatter(df_month6['year_nu'], df_month6['mean_va'], label=f'{filepath}')

    slope, intercept = np.polyfit(df_month6['year_nu'], df_month6['mean_va'], 1)
    ax.plot(df_month6['year_nu'], slope*df_month6['year_nu'] + intercept, '--')


box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()