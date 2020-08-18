import numpy
import math

#class squareSignal
class squareSignal:
    #initialisasi
    def __init__(self, cycle, numData, lowData, highData):
        self.cycle = cycle
        self.numData = numData
        self.lowData = lowData
        self.highData = highData
    #build signal/rawData
    def buildSignal(self):
        tempSig = []  
        for x in range(self.cycle):
                if(x % 2 != 0):
                    for i in range(self.numData):
                        tempSig.append(self.highData)
                else:
                    for i in range(self.numData):
                        tempSig.append(self.lowData)
        return tempSig
#end of class

#class sawTooth
class sawTooth:
    #initialisasi
    def __init__(self, cycle, numData, lowData, highData):
        self.cycle = cycle
        self.numData = numData
        self.lowData = lowData
        self.highData = highData
    #build signal/rawData
    def buildSignal(self):
        tempSig = []
        rampUp = (self.highData - self.lowData)/self.numData
        for x in range(self.cycle):
            for i in range(self.numData):
                if(i == 0):
                    prevData = self.lowData
                else:
                    prevData = (1+rampUp)*prevData
                    if prevData > self.highData:
                        prevData = self.highData
                tempSig.append(prevData)
        return tempSig
#end of class

#class triAngle
class triAngle:
    #initialisasi
    def __init__(self, cycle, numData, lowData, highData):
        self.cycle = cycle
        self.numData = numData
        self.lowData = lowData
        self.highData = highData
    #build signal/rawData
    def buildSignal(self):
        tempSig = []
        peekPoint = self.numData/2
        ramp = (self.highData - self.lowData)/peekPoint
        for x in range(self.cycle):
            for i in range(self.numData):
                if (i<peekPoint):
                    if(i == 0):
                        prevData = self.lowData
                    else:
                        prevData = (1+ramp)*prevData
                        if prevData > self.highData:
                            prevData = self.highData
                else:
                    prevData = (1-ramp)*prevData
                    if prevData < self.lowData:
                        prevData = self.lowData
                tempSig.append(prevData)
        return tempSig
#end of class

#class sinus
class sinus:
    #initialisasi
    def __init__(self, cycle, numData, lowData, highData):
        self.cycle = cycle
        self.numData = numData
        self.lowData = lowData
        self.highData = highData
    #build signal/rawData
    def buildSignal(self):
        tempSig = []
        ramp = (180)/self.numData
        for x in range(self.cycle*self.numData):
            sin = math.sin(math.radians(x*ramp))
            val = self.lowData + (self.highData-self.lowData)*sin
            tempSig.append(val)
        return tempSig
#end of class

#class randomSignal
class randomSignal:
    #initialisasi
    def __init__(self, cycle, numData, lowData, highData):
        self.cycle = cycle
        self.numData = numData
        self.lowData = lowData
        self.highData = highData
    #build signal/rawData
    def buildSignal(self):
        tempSig = numpy.random.uniform(self.lowData, self.highData, int(self.cycle*self.numData))
        return tempSig
#end of class
