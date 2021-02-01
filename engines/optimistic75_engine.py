import dataModels
from scipy.stats import norm

def start():
    print("75% optimistic engine start")
    dataModels.TT_DataModel.insert(7,"75_optimistic",norm.ppf(.75,dataModels.TT_DataModel["regression"],dataModels.stddev))
    print(dataModels.TT_DataModel.head())
    print("75% optimistic engine finish")
