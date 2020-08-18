#class emaFilter
class emaFilter:
    #initialisasi
    def __init__(self, emaAlfa, rawData):
        self.emaAlfa = emaAlfa
        self.rawData = rawData
    def calculate(self):
        rslData=[]
        for x in range(len(self.rawData)):
            if x == 0 :
                rslData.append(((self.emaAlfa*self.rawData[x])+((100.0-self.emaAlfa)*self.rawData[x]))/100.0)
            else:
                rslData.append(((self.emaAlfa*self.rawData[x])+((100.0-self.emaAlfa)*rslData[x-1]))/100.0)
        return rslData
#end of class

#class emaFilter
class convergence:
    #initialisasi
    def __init__(self, cvgTol, rawData, filterData):
        self.cvgTol = cvgTol
        self.rawData = rawData
        self.filterData = filterData

    def findPoint(self):
        xCvg = 0
        xStart = 0
        for x in range(len(self.rawData)):
            if x >= 1:
                if self.rawData[x-1] != self.rawData[x]:
                    xStart = x
                if xStart > 1:
                    if self.rawData[x] > 0:
                        divPercent = 100*abs((self.filterData[x]-self.rawData[x])/self.rawData[x])
                    if divPercent <= self.cvgTol and xCvg == 0:
                        xCvg = x - xStart
                        headCvgTxt = 'Step\tRaw\tFilter\tDiv(%)' 
                        dataCvgTxt = str(x) + '\t' + str(round(self.rawData[x],3)) + '\t' + str(round(self.filterData[x],3))
                        dataCvgTxt = dataCvgTxt + '\t' + str(round(divPercent,3))
                        txtCvgAll = headCvgTxt + '\n' + dataCvgTxt
                        txtCvgAll = txtCvgAll + '\n' + 'Convg. at : ' + str(xCvg)
                        print(txtCvgAll)
                        break #take data for first occurance
