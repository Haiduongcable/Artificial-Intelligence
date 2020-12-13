import sklearn 
import numpy as np 
import os 
import time
import pandas
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing

class Evaluation():
    def __init__(self):
        self.metric = "MSE"
    
    def eval(self, Ypred, Ygroundtruth):
        MSE = mean_squared_error(Ygroundtruth, Ypred)
        return MSE