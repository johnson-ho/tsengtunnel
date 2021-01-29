import numpy as np
import dataModels

def start():
    print("Calculate Standard Deviation started")
    dataModels.stddev = np.std(dataModels.TT_DataModel["diff"])
    print("Standard deviation",dataModels.stddev)
    print("Calculate Standard Deviation finish")