import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": np.random.randint(1, 100, 10),
    "B": np.random.randint(1, 100, 10),
    "C": np.random.randint(1, 100, 10)
})
for i in ['A','B','C']:
    df.loc[np.random.randint(0,10,2),i] = np.nan

print(df)

df_filled = df.fillna(df.mean())

print(df_filled)
