import pandas as pd

TT_DataModel = ""
slope = 0.0
intercept = 0.0
def init_dataModel():
    global TT_DataModel
    TT_DataModel = pd.read_csv("data/HSI_closing.csv")
