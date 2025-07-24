import pandas as pd
import os
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/araJ2/customer-database/master/Ecommerce%20Customers.csv')

df = df.iloc[:,3:]

df = df[df["Length of Membership"]>1]

df.drop(columns=["Avg. Session Length"], inplace=True)

df.to_csv('data/customers.csv', index=False)