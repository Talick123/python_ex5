import pandas as pd
import matplotlib.pyplot as plt

# QUESTION 1
df = pd.read_csv('project_data.csv')
#data_table = pd.DataFrame(csv_file)
#print(data_table.head(20))
print(df.head(20))

# QUESTION 2
print(pd.unique(df["marital_status"]))

# QUESTION 3
df = df.replace('Widowed', 'Widow')

# QUESTION 4
