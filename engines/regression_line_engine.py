import dataModels

def start():
    print("regression line engine start")
    dataModels.TT_DataModel.insert(4,"regression",(dataModels.slope*dataModels.TT_DataModel["number"])+dataModels.intercept)
    print(dataModels.TT_DataModel.head())
    print("regression line engine finish")
