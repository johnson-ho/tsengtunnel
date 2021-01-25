from engines import std_dev_engine
from engines import logarithm_engine
from array import *
import pandas as pd

TT_DataModel = ""

def init():
    print("Initialize")
    print("Prepare data model")
    global dataFrame
    TT_DataModel = pd.read_csv("/Users/Johnson/tsengtunnel/data/HSI_closing.csv")
    print("Data model ready")


def main():
    print ("Tseng Tunel Program Started")
    init()
    logarithm_engine.start()
    std_dev_engine.start()

#Core Step
# 1. Trigger Standard Deviation Engine
main()
