import sklearn 
import numpy as np 
import os 
import time
import pandas
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
import yaml
from Dataloader import LoadData
from LinearRegression import Linear_Regression
from FuzzyLogic import FIS
from evaluate import Evaluation
from Plot_Figure import Plot_Figure


with open("config.yaml", "r") as f:
    config = yaml.load(f)


if __name__ == "__main__":
    #Load model
    __Linear_Regression = Linear_Regression()
    __FIS = FIS()
    
    #Load dataset
    __LoadData = LoadData()
    (Xtest, Ytest), (Xtrain, Ytrain) = __LoadData.load()
    
    #Training Linear Regression
    regression = __Linear_Regression.fit(Xtrain, Ytrain)
    
    
    #predict Fuzzy
    Ypredict_Fuzzy = []
    sum = 0
    for index in range(np.shape(Xtest)[0]):
        evoparation, humidity, pressure, cloud, temp = Xtest[index][0], Xtest[index][1]\
                                                        ,Xtest[index][2], Xtest[index][3]\
                                                        , Xtest[index][4]
        result_predict = __FIS.predict(evoparation, humidity, pressure, cloud, temp)
        Ypredict_Fuzzy.append(result_predict)
        sum += (result_predict - Ytest[index]) ** 2
        
    #predict Linear Regression
    Ypredict_LinearRegression = regression.predict(Xtest)
        
    #eval 
    __Evaluation = Evaluation()
    MSE_Fuzzylogic = sum/ len(Ytest)
    
    MSE_LinearRegression = __Evaluation.eval(Ypredict_LinearRegression, Ytest)
    print(MSE_Fuzzylogic, MSE_LinearRegression)
    
    #Plot 
    # __Plot_Figure = Plot_Figure()
    # label = 'Fuzzy logic '
    # __Plot_Figure.plot(label, Ypredict_Fuzzy, Ytest)

    