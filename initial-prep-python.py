# Imports
import pandas as pd
import plotly.express as px
import panel as pn
import re
from IPython.display import IFrame
import time
import random
#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import StandardScaler



url = "https://raw.githubusercontent.com/Lughaidh-w/Laptop-Prices/main/laptop_price1.csv"
df = pd.read_csv(url)
# Save original dataset for later use if needed.
df_original = df

print(df.info())
print(df.head())

# unique and null values
def unique_and_null(df):
    table = pd.DataFrame(columns=['Column', 'Entries', 'Nunique', 'Null values'])
    for col in df.columns:
        nunique = df[col].nunique()
        null_values = df[col].isnull().sum()
        entries = len(df[col])
        new_row = {'Column': col, 'Entries': entries, 'Nunique': nunique, 'Null values': null_values}
        table = pd.concat([table, pd.DataFrame([new_row])])
    print(table.to_string(index=False))

unique_and_null(df)  
