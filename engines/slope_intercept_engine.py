import pandas as pd
import dataModels
from scipy.stats import linregress


def start():
    TT_stats = linregress(dataModels.TT_DataModel["number"],dataModels.TT_DataModel["logarithm"])
    dataModels.slope = TT_stats.slope
    dataModels.intercept = TT_stats.intercept    
    print("Slope ", dataModels.slope)
    print("Intercept ", dataModels.intercept)