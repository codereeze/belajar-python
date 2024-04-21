import pandas as pd

# default 60
pd.options.display.max_rows = 9999

df = pd.read_csv('coffee.csv')
print(df)