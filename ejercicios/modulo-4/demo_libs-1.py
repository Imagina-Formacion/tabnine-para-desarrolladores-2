import pandas as pd

data = { 'col1': [1,2], 'col2': [3,4], 'col3': [5,6] }

df = pd.DataFrame(data)

print(df.head(), df.describe(), df.info())



