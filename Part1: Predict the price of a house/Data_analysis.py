import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'House_data.xlsx'
path = os.path.join(pre, fname)

dataset = pd.read_excel(path)

x = dataset[["longitude","latitude","House Age","Distance from nearest Metro station (km)","Number of convenience stores","Number of bedrooms","House size (sqft)"]]
y = dataset["House price of unit area"]

# Ghraphs of variables with respect to the price

# plt.subplot(3,3,1)
# plt.scatter(x["longitude"],y)
# plt.title("longitude")
# plt.subplot(3,3,2)
# plt.scatter(x["latitude"],y)
# plt.title("latitude")
# plt.subplot(3,3,3)
# plt.scatter(x["House Age"],y)
# plt.title("House Age")
# plt.subplot(3,3,4)
# plt.scatter(x["Distance from nearest Metro station (km)"],y)
# plt.title("Destande from metro")
# plt.subplot(3,3,5)
# plt.scatter(x["Number of convenience stores"],y)
# plt.title("Number of conv. stores")
# plt.subplot(3,3,6)
# plt.scatter(x["Number of bedrooms"],y)
# plt.title("bedroom number")
# plt.subplot(3,3,7)
# plt.scatter(x["House size (sqft)"],y)
# plt.title("House size")
# plt.show()