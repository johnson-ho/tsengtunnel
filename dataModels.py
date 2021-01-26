import pandas as pd

TT_DataModel = ""
def init_dataModel():
    global TT_DataModel
    TT_DataModel = pd.read_csv("data/HSI_closing.csv")
