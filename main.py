import pandas as pd
from matplotlib import pyplot as plt

data=pd.read_csv("/Users/vishnu/Downloads/Video_Games.csv")
dataframe=pd.DataFrame(data)
dfh=dataframe.head(100)
dfh.plot(x="Genre",y="Other_Sales",kind="line",title="Video_games")
plt.show()