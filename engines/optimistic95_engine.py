import dataModels
from scipy.stats import norm

def start():
    print("95% optimistic engine start")
    dataModels.TT_DataModel.insert(6,"95_optimistic",norm.ppf(.95,dataModels.TT_DataModel["regression"],dataModels.stddev))
    print(dataModels.TT_DataModel.head())
    print("95% optimistic engine finish")
