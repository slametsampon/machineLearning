#
# densityPPL.py
# Input data form csv file
# Output to ploting
# Author : sam April 02, 2020
# 
from csv import reader
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import numpy

fileCsv = 'D711dens16_04_20.csv'
plotTitle = 'Machine Learning' + '\n' + fileCsv
polyOrde = 3
sampLevel = 200

level = []#level data
dens = []#raw density
densDelta = []#Compensated density
densComp = []#Compensated density
densCrr = []#Corrected density
errCrr = []#Error Corrected density

def plotDisplay():
    #plot decorative
    rawTxt = 'Raw Max - Min : ' + str(maxDens) + ' - ' + str(minDens)
    rawTxt = rawTxt + ' => ' + str(round(deltaDens,3))
    rawTxt = rawTxt + '\nAvg : ' + str(round(avgDens,3)) + ', StdDev : ' + str(round(stdDevDens,3))
    rawTxt = rawTxt + ', COV : ' + str(round(covDens,1)) + '%'

    densCrrTxt = 'Corrected Max - Min : ' + str(round(maxDensCrr,3)) + ' - ' + str(round(minDensCrr,3))
    densCrrTxt = densCrrTxt + ' => ' + str(round(deltaDensCrr,3))
    densCrrTxt = densCrrTxt + '\nAvg : ' + str(round(avgDensCrr,3)) + ', StdDev : ' + str(round(stdDevDensCrr,3))
    densCrrTxt = densCrrTxt + ', COV : ' + str(round(covDensCrr,1)) + '%'

    errCrrTxt = 'Error Corrected Max - Min : ' + str(round(maxErrCrr,3)) + ' - ' + str(round(minErrCrr,3))
    errCrrTxt = errCrrTxt + ' => ' + str(round(deltaErrCrr,3))
    errCrrTxt = errCrrTxt + '\nAvg : ' + str(round(avgErrCrr,3)) + ', StdDev : ' + str(round(stdDevErrCrr,3))
    numbDataTxt = "Data Numb : " + str(len(level))
    #errCrrTxt = errCrrTxt + ', COV : ' + str(round(covErrCrr,1)) + '%'

    allTxt = rawTxt + '\n\n' + densCrrTxt + '\n\n' + errCrrTxt + '\n' + numbDataTxt

    relTxt = 'Relations : ' + str(round(rel,1)) + '%'
    formulaTxt = 'Compensated Formula :\n' + str(densDeltaModel)
    formulaTxt = formulaTxt + '\n' + relTxt

    plt.title(plotTitle)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.text(4000,0.23,allTxt)
    plt.text(4000,0.1,formulaTxt,fontsize=10,color = 'b')

    #plot densDeltaModel
    plt.scatter(level, dens, label='raw', color='k',marker=".")
    plt.scatter(level, densCrr, label='Corrected', color='r',marker="x")
    plt.scatter(level, densDelta, label='densDelta', color='g',marker="+")
    plt.plot(levelLine, densDeltaModel(levelLine), color = 'k')#color black
    plt.plot(levelLine, densCrrModel(levelLine), color = 'g')#color green
    plt.grid(True)
    plt.legend()
    plt.show()

# read csv file as a list of lists
with open(fileCsv, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj, delimiter=";")
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

line = 0
for item in list_of_rows:
    if line == 0:
        xLabel = item[0]
        yLabel = item[1]
    else:
        level.append(int(item[0]))
        dens.append(float(item[1]))
    line +=1



#Calculate densDelta , Delta density from minimum value
maxDens = max(dens)
minDens = min(dens)
maxLevel = max(level)
minLevel = min(level)
for item in dens:
    densDelta.append(item - minDens)


#find out parameter for densDelta
#Build model
coefDensDelta = numpy.polyfit(level, densDelta, polyOrde)
densDeltaModel = numpy.poly1d(coefDensDelta)

#Calculate Dens Corrected
for x in range(len(level)):
    dc = densDeltaModel(level[x])
    densCrr.append(dens[x]-dc)

coefDensCrr = numpy.polyfit(level, densCrr, polyOrde)
densCrrModel = numpy.poly1d(coefDensCrr)
for x in range(len(level)):
    ec = densCrrModel(level[x])
    errCrr.append(densCrr[x]-ec)


rel = r2_score(densDelta, densDeltaModel(level))*100.0

levelLine = numpy.linspace(minLevel, maxLevel, sampLevel)

#Evaluation
deltaDens = maxDens-minDens
avgDens = numpy.mean(dens)
stdDevDens = numpy.std(dens)
covDens = (stdDevDens/avgDens)*100.0 #Coeficient of Variation

maxDensCrr = max(densCrr)
minDensCrr = min(densCrr)
deltaDensCrr = maxDensCrr - minDensCrr
avgDensCrr = numpy.mean(densCrr)
stdDevDensCrr = numpy.std(densCrr)
covDensCrr = (stdDevDensCrr/avgDensCrr)*100.0 #Coeficient of Variation

maxErrCrr = max(errCrr)
minErrCrr = min(errCrr)
deltaErrCrr = maxErrCrr - minErrCrr
avgErrCrr = numpy.mean(errCrr)
stdDevErrCrr = numpy.std(errCrr)

#Model parameter    
print("maxDens : ", maxDens)
print("minDens : ", minDens)
print("coefDensDelta : ", coefDensDelta)
print("Model Comp : \n", densDeltaModel)
print("coefDensCrr : ", coefDensCrr)
print("Model DensCrr : \n", densCrrModel)

#display plot
plotDisplay()

