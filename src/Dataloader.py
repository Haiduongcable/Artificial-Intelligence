import sklearn 
import numpy as np 
import os 
import time
import pandas
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
from utils import convert_Date, convert_wind_direction
import gdown
import yaml

with open("config.yaml", "r") as f:
    config = yaml.load(f)

class LoadData():
    def __init__(self):
        self.path_data = config['path_save_data']
    
    
    def load(self):
        dataset = dataset= pandas.read_csv(self.path_data)
        dataset.dropna()
        dataset = dataset.to_numpy()
        #split train,test
        data_test = dataset[:500]
        data_train = dataset[500:]
        Xtrain, Ytrain  = data_train[:,0:5], data_train[:,5]
        Xtest, Ytest = data_test[:,0:5], data_test[:,5]
        return (Xtest, Ytest), (Xtrain, Ytrain)