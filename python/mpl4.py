import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "name": ["Joe", "Sally", "Ananya"],
    "score": np.random.randint(0,100,size=3)
})

df.set_index("name",drop=True,inplace=True)
df.plot.bar()
plt.show()

