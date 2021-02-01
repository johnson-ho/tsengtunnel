from engines import std_dev_engine
from engines import logarithm_engine
from engines import slope_intercept_engine
from engines import regression_line_engine
from engines import diff_regression_logarithm_engine
from engines import std_dev_engine
from engines import optimistic95_engine
from engines import optimistic75_engine
from engines import pessimistic25_engine
from engines import pessimistic5_engine
import matplotlib.pyplot as plt

import dataModels
import pandas as pd
import numpy as np

TT_DataModel = ""

def init():
    print("Initialize")
    print("Prepare data model")
    dataModels.init_dataModel()
    print("Data model ready")


def main():
    print ("Tseng Tunel Program Started")
    init()
    logarithm_engine.start()
    slope_intercept_engine.start()
    regression_line_engine.start()
    diff_regression_logarithm_engine.start()
    std_dev_engine.start()
    optimistic95_engine.start()
    optimistic75_engine.start()
    pessimistic25_engine.start()
    pessimistic5_engine.start()
    dataModels.TT_DataModel.plot(x="date", y=["logarithm","regression","95_optimistic","75_optimistic","25_pessimistic","5_pessimistic"])
    plt.show()

#Core Step
# 1. Trigger Standard Deviation Engine
main()
