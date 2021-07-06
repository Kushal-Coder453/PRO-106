import csv
import plotly.express as ps
import numpy as np
def plotFigure(dataPath):
    with open(dataPath) as f:
        df=csv.DictReader(f)
        fig=ps.scatter(df, x="Days Present", y="Marks In Percentage")
        fig.show()
def getDataSource(dataPath):
    marksInPersentage=[]
    daysPresent=[]
    with open(dataPath) as f:
        csvReader=csv.DictReader(f)
        for row in csvReader:
            marksInPersentage.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
    return {"x":marksInPersentage, "y":daysPresent}
def findCoRelation(dataSource):
    coRelation=np.corrcoef(dataSource["x"], dataSource["y"])
    print("coRelation=", coRelation[0, 1])
def setUp():
    dataPath="C:/Users/KAMBLE/Desktop/coRelation/Student Marks vs Days Present2.csv"
    dataSource=getDataSource(dataPath)
    findCoRelation(dataSource)
    plotFigure(dataPath)
setUp()