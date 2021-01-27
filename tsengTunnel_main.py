from engines import std_dev_engine
from engines import logarithm_engine
from engines import slope_intercept_engine
from array import *
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
    print(dataModels.TT_DataModel.head())
    std_dev_engine.start()
    slope_intercept_engine.start()

#Core Step
# 1. Trigger Standard Deviation Engine
main()
