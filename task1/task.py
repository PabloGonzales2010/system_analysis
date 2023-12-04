import pandas as pd
def task(a,b,c):
  return pd.read_csv(a, header=None).iloc[b].iloc[c]
