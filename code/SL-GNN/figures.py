import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FixedLocator

def generate_comparison_figures():
    df = pd.read_csv('Comparison/comparison.csv')
    grouped = df.groupby(['case', 'num_nodes'])

    for (case, num_nodes), group_data in grouped:
        fig, axes = plt.subplots(3, 3, figsize=(15, 15), sharey=True)
        fig.suptitle(f'Case {case}, Num Nodes {num_nodes}')

        for i, (num_sources, num_sources_data) in enumerate(group_data.groupby('num_sources')):
            for j, budget in enumerate(num_sources_data['budget'].unique()):
                budget_data = num_sources_data[num_sources_data['budget'] == budget]
                x = np.arange(len(budget_data))
                axes[i, j].bar(x - 0.2, budget_data['gnn'], width=0.2, label='GNN')
                axes[i, j].bar(x, budget_data['random'], width=0.2, label='Random')
                axes[i, j].bar(x + 0.2, budget_data['max_degree_static'], width=0.2, label='Max Degree Static')
                axes[i, j].bar(x + 0.4, budget_data['max_degree_dynamic'], width=0.2, label='Max Degree Dynamic')
                axes[i, j].set_title(f'Budget {budget}, Num Sources {num_sources}')
                axes[i, j].set_xlabel('Degree')
                axes[i, j].set_ylabel('Infection Rate')
                axes[i, j].xaxis.set_major_locator(FixedLocator(x))
                axes[i, j].set_xticklabels(x+1)
                axes[i, j].legend()

        plt.tight_layout()
        plt.savefig(f'Figures/case_{case}_num_nodes_{num_nodes}.pdf')

# generate_comparison_figures()