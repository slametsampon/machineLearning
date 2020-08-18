import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import numpy

from model import Model
from view import View

class Controller:
    def __init__(self):
        self.view = View(self)
        self.model = Model()

    def main(self):
        data = self.model.readCsvFile('EXCEL',self.model.header['fileName'])
        #data = self.model.readCsvFile('CSV',self.model.header['fileName'])
        self.view.viewData(data)
        self.view.main()
        
if __name__ == '__main__':
    MachineLearning = Controller()
    MachineLearning.main()
