from engines import std_dev_engine
from engines import logarithm_engine
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
    std_dev_engine.start()

#Core Step
# 1. Trigger Standard Deviation Engine
main()
