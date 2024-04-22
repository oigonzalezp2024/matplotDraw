#Three lines to make our compiler able to draw:
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

class MatplotDraw:

    def __init__(self, data={}):
        self.data = data

    def title(self, titleStr:str):
        self.data['title'] = titleStr

    def suptitle(self, suptitleStr:str):
        self.data['suptitle'] = suptitleStr
        
    def varX(self, nameVarX:str, scaleX:list):
        self.data['xlabel'] = nameVarX
        self.data['x'] = np.array(scaleX)

    def varY(self, nameVarY:str, scaleY:list):
        self.data['ylabel'] = nameVarY
        self.data['y'] = np.array(scaleY)

    def pathEnd(self, path:str):
        self.data['path'] = path

    def getLineChart(self, i):
        matplotlib.use('Agg')
        plt.title(i['title'])
        plt.suptitle(i['suptitle'])
        plt.xlabel(i['xlabel'])
        plt.ylabel(i['ylabel'])
        plt.plot(i['x'], i['y'])
        plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
        plt.savefig(i['path'])
        plt.close('all')

    def getLineCharts(self, data):
        for i in data:
            self.getLineChart(i)
    
    def readFile():
        f = open("./data/data.json","r")
        content = f.read()
        f.close()
        return content