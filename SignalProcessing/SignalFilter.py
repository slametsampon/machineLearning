#
# EmaFilter.py
# Output to ploting
# Author : sam April 05, 2020
# 
import matplotlib.pyplot as plt
import numpy

import libraries.signal as sg
import libraries.filterSig as flt

emaAlfa = 10 #percentage (0 - 100)
cvgTol = 0.5 #percentage Convergence Tolerance
seqType ='SQUARE'
rndType ='RANDOM'
sawType ='SAW_TOOTH'
triType ='TRI_ANGLE'
sinType ='SINUS'
signalType = sinType

highData = 0.5
lowData = 0.1 #avoid to put 0.0 value, since it's for divide operation
numData = 50
cycle = 4

rawData =[]
filterData =[]
xLine = []

emaTxt = 'Signal Type : ' + signalType + ", Ema Alfa : " + str(emaAlfa) + "%" 
titleTxt = "Exponential Moving Average\nEMA-Filter\n" + emaTxt

#plotting
def plotingResult():
    xLine = numpy.linspace(0, len(rawData), len(rawData))
    plt.plot(xLine, rawData, color = 'k')#color black
    plt.plot(xLine, filterData, color = 'r')#color red

    plt.title(titleTxt)
    plt.ylabel("Signal")
    plt.xlabel("Event")
    plt.grid(True)
    plt.legend()
    plt.show()

#display parameter
def printSummary():
    print('EMA Alfa :',emaAlfa)
    print('Convergence Tol(%) :',cvgTol)
    print('highData :',highData)
    print('lowData :',lowData)
    print('Cycle :',cycle)
    print('numdata/cycle :',numData)

#logic type for signal and processing
if signalType == seqType:
    rawData = sg.squareSignal(cycle, numData,lowData,highData).buildSignal()
    filterData = flt.emaFilter(emaAlfa, rawData).calculate()
    flt.convergence(cvgTol,rawData,filterData).findPoint()

elif signalType == rndType:
    rawData = sg.randomSignal(cycle,numData,lowData,highData).buildSignal()
    filterData = flt.emaFilter(emaAlfa, rawData).calculate()

elif signalType == sawType:
    rawData = sg.sawTooth(cycle,numData,lowData,highData).buildSignal()
    filterData = flt.emaFilter(emaAlfa, rawData).calculate()

elif signalType == triType:
    rawData = sg.triAngle(cycle,numData,lowData,highData).buildSignal()
    filterData = flt.emaFilter(emaAlfa, rawData).calculate()

elif signalType == sinType:
    rawData = sg.sinus(cycle,numData,lowData,highData).buildSignal()
    filterData = flt.emaFilter(emaAlfa, rawData).calculate()

else:
    print('No available process')

#display result
printSummary()
plotingResult()
