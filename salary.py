import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('Salary_Data.csv')
X=df.iloc[:,:-1].values
Y=df.iloc[:,-1].values
from sklearn.model_selection import trrain_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=42)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title("CTC vs years of experience")
plt.xlabel("Experience in years")
plt.ylabel("CTC")
plt.show()
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title("CTC vs years of experience")
plt.xlabel("Experience in years")
plt.ylabel("CTC")
plt.show()