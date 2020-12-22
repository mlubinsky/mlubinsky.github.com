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

print("bytes max_index=",df['bytes'].idxmax(), "  max_value=", df['bytes'].max() )

print("PLOT ALL")
sns.set(rc={'figure.figsize':(11, 4)})

# df['bytes'].plot(linewidth=0.5)
#df.plot.scatter(x=df.index, y='bytes')
df['bytes'].plot(style='.', title='all')
plt.show()

filtered=df.query('bytes  < 1000')
filtered['bytes'].plot(style='.', title=' bytes  < 1000')
#filtered['bytes'].plot(linewidth=0.5)
#filtered.plot.scatter(x=df.index, y='bytes')
plt.show()

bytes_col=df['bytes']
print ( type(bytes_col))
print( bytes_col.head() )

# bytes < 100
filtered_bytes = bytes_col[ bytes_col < 100]
filtered_bytes.plot(kind="hist", bins=80, title=' bytes  < 100 bins=80' )
plt.show()

filtered_bytes.plot.hist(bins=20, alpha=0.4, title=' bytes  < 100 bins=20  alpha=0.4')
plt.show()

filtered_bytes2 = bytes_col[ lambda x: x < 3000]
filtered_bytes2.plot(kind="hist", title=' bytes  < 3000' )
plt.show()

filtered_bytes2.plot.hist(bins=40, alpha=0.4,  title='bins=40, alpha=0.4 ')
plt.show()
filtered_bytes2.plot.hist(bins=80, alpha=0.8, title='bins=80, alpha=0.8 ' )
plt.show()
## one day slicing:
starts=['2020-06-22' , '2020-06-23', '2020-06-24' ,  '2020-06-25', '2020-06-26'  ]
for i, start in  enumerate(starts):
 if i < len(starts) - 1:
   #end = starts[i+1]
   #one_day=bytes_col[start : end]
   one_day=bytes_col.loc[start]
   one_day.plot(style='.', title=start)
   plt.show()
#exit(1)

#bytes_col.plot(kind="hist")
#plt.show()

top_5 = df.sort_values(by="bytes", ascending=False).head()
print(" TOP 5 bytes ")
print(top_5["bytes"])

print(df['bytes'].describe())

