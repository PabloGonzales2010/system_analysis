import pandas as pd
a = pd.read_csv("task3.csv")
b = 8 #сюда подставить значение для поиска
if a.isin([str(b)]).any()[a.isin([str(b)]).any() == True].size > 0:
    print("родитель:")
    print(a.isin([str(b)]).any()[a.isin([str(b)]).any() == True].index[0])
if a.isin([b]).any()[a.isin([b]).any() == True].size > 0:
    print("родитель:")
    print(a.isin([b]).any()[a.isin([b]).any() == True].index[0])
if str(b) in a:
    print("дети:")
    for x in a[str(b)].values:
        print(x)
