
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

class Plot_Figure():
    def __init__(self):
        pass
    
    def plot(self,label, Ypredict, Ygroundtruth):
        '''
        :param str label: string label of data plot 
        :param np.array Ypredict: numpy array of value predicted from model
        :param np.array Ygroundtruth: numpy array of value rainfall in dataset 
        '''
        fig = plt.figure(figsize=(12, 6), dpi=80)
        ax = plt.subplot(111)
        plt.ylabel('Rain fall')
        plt.xlabel(label)
        ax.plot(Ygroundtruth, label="GroundTruth")
        ax.plot(Ypredict, label = "Predict")
        ax.legend()
        