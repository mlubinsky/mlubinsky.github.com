# https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/
# https://realpython.com/pandas-plot-python/

import sys
import pandas as pd
import numpy as np

# import matplotlib 
# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import seaborn as sns

fname="05-3116.csv"
fname=sys.argv[1]

df=pd.read_csv(fname, sep='\t' )
df.info()
print("Head")
print(df.head())

print("Transform:")
df['Date']=pd.to_datetime(df['timebin'], unit='s')
print("Head")
print( df.head() )

print("Set index")

df = df.set_index('Date')
print( df.head() )

# print( df.loc['2020-05-03'] )
print("bytes max_index=",df['bytes'].idxmax(), "  max_value=", df['bytes'].max() )

print("PLOT")
sns.set(rc={'figure.figsize':(11, 4)})
df['bytes'].plot(linewidth=0.5)
plt.show()

bytes_col=df['bytes']
bytes_col.plot(kind="hist")

top_5 = df.sort_values(by="bytes", ascending=False).head()
print(" TOP 5 bytest ")
print(top_5["bytes"])

