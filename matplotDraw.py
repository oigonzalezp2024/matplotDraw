
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
        invalid_chars = '<>:"/\\|?*'
        clean_product = product
        for char in invalid_chars:
            clean_product = clean_product.replace(char, "")
        self.product = clean_product.strip()

    def chartName(self)->None:
        self.name = str(self.city)+str(self.product)

    def corePlt(self, i:object)->None:
        matplotlib.use('Agg')
        
        # --- Configuración de Colores Invertidos ---
        color_fondo = "#121212"        # Gris casi negro
        color_linea_contable = "#333333" # Gris oscuro para la cuadrícula
        color_tinta = "#E0E0E0"         # Blanco grisáceo para textos
        color_trazado = "#00FFC8"       # Un color que resalte (Cian neón) o usa "#FFFFFF"
        
        plt.figure(figsize=(10, 6), facecolor=color_fondo) 
        ax = plt.axes()
        ax.set_facecolor(color_fondo) 
        
        # Títulos
        plt.title(i['title'], color=color_tinta, fontsize=12, fontweight='bold', family='serif')
        plt.suptitle(i['suptitle'], color=color_tinta, fontsize=14, family='serif')
        
        # Ejes y etiquetas
        plt.xlabel(i['xlabel'], color=color_tinta, family='serif')
        plt.ylabel(i['ylabel'], color=color_tinta, family='serif')
        plt.xticks(rotation=50, fontsize=8, color=color_tinta, family='monospace')
        plt.yticks(fontsize=9, color=color_tinta, family='monospace')
        
        # El gráfico (la línea de datos)
        plt.plot(i['x'], i['y'], color=color_trazado, linewidth=2, marker='o', markersize=4, alpha=0.9)
        
        # Cuadrícula
        plt.grid(True, color=color_linea_contable, linestyle='-', linewidth=0.7)
        
        # Bordes del gráfico (spines)
        for spine in ax.spines.values():
            spine.set_edgecolor(color_tinta)
            spine.set_linewidth(1.2)

        plt.subplots_adjust(bottom=0.20)
        
        # Guardado (Asegúrate de incluir el facecolor aquí también para que el PNG no salga blanco)
        plt.savefig(self.path + "/" + str(self.name), facecolor=color_fondo)
        plt.close('all')
