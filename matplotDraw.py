
import json
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

class MatplotDraw:

    def __init__(self, data:object={})->None:
        self.data = data
        self.name = "pathImg.png"

    def readFileJson(self, pathJson:str)->object:
        f = open(pathJson,"r")
        content = f.read()
        f.close()
        response = json.loads(content)
        return response

    def pathEnd(self, path:str)->None:
        self.path = path

    def getLineCharts(self, data:list)->None:
        for i in data:
            self.getLineChart(i)       

    def getLineChart(self, i:object)->None:
        self.setCity(i['city'])
        self.setDate(i['date'])
        self.setProduct(i['product'])
        self.chartName()
        self.corePlt(i)
    
    def setCity(self, city:str)->None:
        self.city = city

    def setDate(self, date:str)->None:
        self.date = date.replace("-", "")

    def setProduct(self, product:str)->None:
        self.product = product

    def chartName(self)->None:
        self.name = str(self.city)+str(self.product)

    def corePlt(self, i:object)->None:
        matplotlib.use('Agg')
        plt.figure(figsize=(10,6))
        plt.title(i['title'])
        plt.suptitle(i['suptitle'])
        plt.subplots_adjust(bottom=0.15)
        plt.xlabel(i['xlabel'])
        plt.xticks(rotation=50, fontsize=8)
        plt.ylabel(i['ylabel'])
        plt.plot(i['x'], i['y'])
        plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
        plt.savefig(self.path+"\/"+str(self.name))
        plt.close('all') 
