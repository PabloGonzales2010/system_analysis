import pandas as pd
print(pd.read_csv("example.csv", header=None).iloc[1].iloc[2])
#сверху подставить название файла, и координаты для получения значения
