# -*- coding: utf-8 -*-
"""StephenP_BurndownBurnup.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K98aI_CD0_8kL7j8XxUhVUN2pYgN13zD
"""

import pandas as pd
import numpy as mp
import matplotlib.pyplot as plt

from google.colab import drive

# read the data

myData = pd.read_csv('/content/drive/MyDrive/IT262 - IT Project Management/BDU.csv')

myData.shape
myData.head(2)

# plot data

fig , (ax1, ax2) = plt.subplots(1,2, figsize = (10,2))

ax1.set_xlabel('days')
ax2.set_xlabel('days')

ax1.plot(myData.Cideal, color='pink', label='work completed - ideal')
ax3 = ax1.twinx()
ax3.plot(myData.Cactual, color='green', label='work completed - actual')

ax2.plot(myData.Lideal, color='pink', label='work to be done - ideal')
ax4 = ax2.twinx()
ax4.plot(myData.Lactual, color='green', label='work to be done - actual')
ax1.set_title('burn up')
ax2.set_title('burn down')

h1, l1 = ax1.get_legend_handles_labels()
h3, l3 = ax3.get_legend_handles_labels()
ax3.legend(h1+h3, l1+l3, loc=2)

h2, l2 = ax2.get_legend_handles_labels()
h4, l4 = ax4.get_legend_handles_labels()
ax4.legend(h1+h3, l1+l3, loc=2)


plt.show()