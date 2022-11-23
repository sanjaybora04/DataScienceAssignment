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

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=101)

lm = LinearRegression()

lm.fit(x_train,y_train)

# coeff_df = pd.DataFrame(lm.coef_,x.columns,columns=['Coefficient'])
# print(coeff_df)

pred = lm.predict(x_train)
plt.scatter(y_train,pred)
plt.show()