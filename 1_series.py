import pandas as pd

data = [100, 102, 104]

series = pd.Series(data, index=["a", "b", "c"])

series.loc["c"] = 200

# print(series.loc["a"]) 
print(series.iloc[0])