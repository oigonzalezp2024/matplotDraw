
from matplotDraw import MatplotDraw

matplotDraw1 = MatplotDraw()
data = matplotDraw1.readFileJson("./data/data.json")
matplotDraw1.pathEnd("./images/")
matplotDraw1.getLineCharts(data)
