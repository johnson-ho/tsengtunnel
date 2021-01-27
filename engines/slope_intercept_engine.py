import pandas as pd
import dataModels
from scipy.stats import linregress


def start():
    TT_stats = linregress(dataModels.TT_DataModel["number"],dataModels.TT_DataModel["logarithm"])
    dataModels.TT_DataModel.slope = TT_stats.slope
    dataModels.TT_DataModel.intercept = TT_stats.intercept    
    print(dataModels.TT_DataModel.slope)
    print(dataModels.TT_DataModel.intercept)