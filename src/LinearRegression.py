import sklearn 
import numpy as np 
import os 
import time
import pandas
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing

class Linear_Regression():
    def __init(self):
        pass

    def fit(self,Xtrain, Ytrain):
        regression = LinearRegression().fit(Xtrain, Ytrain)
        return regression

    def predict(self, Xtest, regression):
        #Model linear regression predict
        Ypred = regression.predict(Xtest)
        #Postprocessing
        Ypred = np.where(Ypred < 0, 0, Ypred)
        return Ypred

