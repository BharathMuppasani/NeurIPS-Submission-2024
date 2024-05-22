# Mitigating-MisInfoSpread

A brief description of what this project does and who it's for.

## Table of Contents

- [Folder Structure](#folder-structure)
- [Files Explanation](#files-explanation)

## Folder Structure

- `Comparison` contains the csv files for the comparison of the different models
- `Dataset` contains the dataset used for the comparison
- `Figures` contains the figures generated from the comparison
- `Models` contains the models weight files (case 1, case 2 and case 3) used for the comparison


## Files Explanation

- `comparison_dataset_v1.py` is the script used to compare the different models on Dataset V1
- `comparison_general.py` is the script used to compare the different models on Dataset V1
- `figure_combined.py` is the script used to generate the figures from the comparison
- `GNN.py` is the script used to define the GNN model.
- `graph_utils.py` is the script used to define the graph utilities like implementing ranking algorithm and evolving graph states
- `main.py` is the script used to train the GNN model
- `MisInfoSpread.py` is the script used to define the placeholder MisInfoSpread model, required to use the dataset
- `model_utils.py` is the script used to define different model utilities like selecting $k$-best nodes, selecting *k*-best nodes, etc.
- `params.py` is the script used to define the parameters used in the project
- `visualization_utils.py` is the script used to define the visualization utilities like plotting the graph, etc. Required to debug code
