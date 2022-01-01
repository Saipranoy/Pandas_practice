import pandas as pd
import numpy as np  

df = pd.read_excel(r'C:\Users\Sai Praneeth S\Desktop\SaleData.xlsx')
#print(df.head())

df = pd.pivot_table(df, index = ["Item"], values = ['Sale_amt'], aggfunc = [np.min, np.max])
print(df)
