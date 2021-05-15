import pickle
import re
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error

# get the dataset
dataset = pd.read_csv('datasets/final_dataset.csv')

# split the features and target
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
# print(X)
# print(y)

# preparing train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# pfobj = PolynomialFeatures(degree=2)
# X_poly_train = pfobj.fit_transform(X)


# training the model
reg = LinearRegression()
reg.fit(X_train, y_train)

# running predictions on test set
pred = reg.predict(X_test)

print(reg.predict([[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]]))


print(pred)

# metrics
rmse = np.sqrt(mean_squared_error(y_test, pred))
r2_score = r2_score(y_test, pred)

print(rmse, r2_score)

# storing the model
pickle.dump(reg, open('model/model.pkl', 'wb'))

