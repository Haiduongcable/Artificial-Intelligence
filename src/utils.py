import sklearn 
import numpy as np 
import os 
import time
import pandas
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing

def convert_Date(Nplist_date):
    converted_list = []
    for date in Nplist_date:
        date = str(date)
        converted_date = date.split('-')[1]
        if (converted_date[0] == '0'):
            converted_date = converted_date[1]
            converted_date = int(converted_date)
        converted_list.append(converted_date)
    return converted_list

def direct_Degree(i):
    switcher={'E':90, 'ENE': 67.5, 'NE': 45, 'WNW':292.5,
                'N': 0,'NW':315, 'SE': 135, 'NNW': 337.5,
              'SSE': 157.5,'NNE': 22.5, 'S': 180, 'W': 270,
              'SSW': 202.5, 'SW': 225, 'WSW': 247.5, 'ESE': 112.5
            }
    return switcher.get(i,0)

def convert_wind_direction(Nplist_direct):
    converted_list = []
    for direct in Nplist_direct:
        degree = direct_Degree(direct)
        converted_list.append(degree)
    return converted_list

