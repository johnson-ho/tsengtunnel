import dataModels
from scipy.stats import norm

def start():
    print("5% pessimistic engine start")
    dataModels.TT_DataModel.insert(9,"5_pessimistic",norm.ppf(.05,dataModels.TT_DataModel["regression"],dataModels.stddev))
    print(dataModels.TT_DataModel.head())
    print("5% pessimistic engine finish")