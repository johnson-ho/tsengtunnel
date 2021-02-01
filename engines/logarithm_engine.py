import pandas as pd
import numpy as np
import dataModels

def start():
    print("Log engine started")
    dataModels.TT_DataModel.insert(3,"logarithm",np.log(dataModels.TT_DataModel["close_index"]))
    print(dataModels.TT_DataModel.head())
    print("Log engine finished")