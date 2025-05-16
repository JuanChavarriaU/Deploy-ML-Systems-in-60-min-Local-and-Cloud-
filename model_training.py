#requires imports
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as LR
import pickle
import os

# load the dataset
data = fetch_california_housing(as_frame=True)
df = data['data']
target = data['target']

#select few features
selected_features = ['MedInc', 'AveRooms', 'AveOccup']
X = df[selected_features] #independent variables for the model
y = target

#Train-test split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#train the linear regression model 
model = LR()
model.fit(X_train, y_train)

#create a model folder to save the trained model
os.makedirs('model', exist_ok=True)


#save the trained model using pickle 
with open('model/linear_regression_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully.")

"""
This script load the california housing dataset, selects three features (medInc, Ave Rooms, Ave Occup). 
Trains a linear regression model, and saves in the model folder as
linear_regression_model.pkl. 
"""


