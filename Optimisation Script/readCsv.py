import csv
import pandas as pd

def sampleFunction(doc):
    return doc

def readCSV():
    csv_file = "data.csv"
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        df.loc[index,'ActualOutput'] = sampleFunction(row['givenInput'])
        df.loc[index,'Results'] = (sampleFunction(row['givenInput']) == row['expectedOutput'])
    print(df)
    df.to_csv('out.csv')   


readCSV()
