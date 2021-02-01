import dataModels
from scipy.stats import norm

def start():
    print("25% pessimistic engine start")
    dataModels.TT_DataModel.insert(8,"25_pessimistic",norm.ppf(.25,dataModels.TT_DataModel["regression"],dataModels.stddev))
    print(dataModels.TT_DataModel.head())
    print("25% pessimistic engine finish")