from csv import reader
import pandas as pd
from pandas import ExcelFile

class Model:
    def __init__(self):
        self.__level = []
        self.__density = []
        self.__label ={}
        self.header ={
            'Title':'Machine Learning',
            'fileName':'Density.xlsx',
            'Order':3,
            'SampNbr':200
        }

    def readCsvFile(self,fileType, fileName):
        if fileType=='CSV':
            # read csv file as a list of lists
            dataRead = pd.read_csv(fileName, sep=';')
        if fileType=='EXCEL':
            # read csv file as a list of lists
            dataRead = pd.read_excel(fileName,sheet_name='D-711')
        return dataRead

    def splitDataCsv(self,listData):
        isLabel = True
        for item in listData:
            if isLabel:
                isLabel = False
                self.__label['x'] = item[0]
                self.__label['y'] = item[1]
            else:
                self.__level.append(int(item[0]))
                self.__density.append(float(item[1]))
    
    def getLevel(self):
        return self.__level

    def getDensity(self):
        return self.__density

    def getLabel(self):
        return self.__label

    
    

