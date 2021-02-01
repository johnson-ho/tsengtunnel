import dataModels

def start():
    print("Different of regression and logarithm engine start")
    dataModels.TT_DataModel.insert(5,"diff",dataModels.TT_DataModel["regression"]-dataModels.TT_DataModel["logarithm"])
    print(dataModels.TT_DataModel.head())
    print("Different of regression and logarithm engine finish")
