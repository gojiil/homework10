import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

print(data)

# Transform the df into one-hot-encoding
df = data.melt(ignore_index=False).reset_index().pivot_table('variable', 'index', 'value', aggfunc='count').fillna(0)

print(df)
