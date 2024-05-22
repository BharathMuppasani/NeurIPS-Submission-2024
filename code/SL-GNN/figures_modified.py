import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Comparison/comparison_modified.csv')

# Grouping by budget and calculating average infection rate for each method
grouped = df.groupby('budget').mean()

# Plotting the results
ax = grouped[['gnn', 'random', 'max_degree_static', 'max_degree_dynamic']].plot(kind='bar', figsize=(10, 6))
ax.set_xlabel('Budget')
ax.set_ylabel('Average Infection Rate')
ax.set_title('Average Infection Rate by Budget and Method')
ax.legend(title="Methods")

plt.show()