# ---
# title: Post With Code
# author: Huayu Liang
# date: now
# categories:
#   - news
#   - code
#   - analysis
# image: image.jpg
# jupyter:
#   jupytext:
#     formats: qmd:quarto,py:percent,md,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# Here is some sample R code
#
# ```{r}
# 1 + 1
# ```
#
# But we also want to run Python

# %%
for i in range(9):
  print(i)

# %%
x = 5

# %%
#| echo: false
#| output: false
# Testing a change in Jupyter notebook
# I'm writing this now in Jupyterlab
import warnings

warnings.filterwarnings("ignore")

# %% [markdown]
# The plot below is from the [Seaborn Python library documentation](https://seaborn.pydata.org/examples/horizontal_boxplot.html)

# %%
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks")
# Initialize the figure with a logarithmic x axis
f, ax = plt.subplots(figsize=(7, 6))
ax.set_xscale("log")
# Load the example planets dataset
planets = sns.load_dataset("planets")
# Plot the orbital period with horizontal boxes
sns.boxplot(
    planets, x="distance", y="method", hue="method",
    whis=[0, 100], width=.6, palette="vlag"
)
# Add in points to show each observation
sns.stripplot(planets, x="distance", y="method", size=4, color=".3")
# Tweak the visual presentation
ax.xaxis.grid(True)
ax.set(ylabel="")
sns.despine(trim=True, left=True)

# %% [markdown]
# The plot below is from the [Yellowbrick Python library documentation](https://www.scikit-yb.org/en/latest/api/features/jointplot.html?highlight=joint%20plot#joint-plot-visualization):

# %%
import numpy as np
from yellowbrick.datasets import load_concrete
from yellowbrick.features import JointPlotVisualizer

# Load the dataset
X, y = load_concrete()

# Instantiate the visualizer
visualizer = JointPlotVisualizer(columns="cement")

visualizer.fit_transform(X, y)        # Fit and transform the data
visualizer.show()                     # Finalize and render the figure
