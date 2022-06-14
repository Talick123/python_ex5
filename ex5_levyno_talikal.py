'''
Written by: Noga Levy (ID: 315260927, login: levyno)
             and Tali Kalev (ID: 208629691, login: talikal)

Goal of the Program:
    Implement different actions on a data table from a csv files.
'''


import pandas as pd
import matplotlib.pyplot as plt

# QUESTION 1
df = pd.read_csv('project_data.csv')
print(df.head(20))

# QUESTION 2
print(pd.unique(df["marital_status"]))

# QUESTION 3
df = df.replace('Widowed', 'Widow')

# QUESTION 4
print(df["educational_level"].value_counts(normalize = True))

# QUESTION 5
ls = ["Single"]
singles = df.loc[df["marital_status"].isin(ls)]
singles = singles.sort_values("annual_income", ascending=False)
print(singles)

# QUESTION 6
df['total_purchases'] = df.apply(lambda row: row.online_purchases + row.store_purchases, axis=1)
print(df)

# QUESTION 7
def get_total(value):
    if value < 10:
        return "Low"
    elif 10 <= value < 20:
        return "Medium"
    elif value >= 20:
        return "High"
df['low/medium/high Purchases'] = df.apply(lambda row: get_total(row["total_purchases"]), axis=1)
print(df)

# QUESTION 8
ls1 = df["low/medium/high Purchases"].value_counts()
plt.pie(ls1, labels=ls1.index)
plt.show()

# QUESTION 9
ls2 = df.groupby('total_purchases')
print(ls2[['online_purchases', 'store_purchases', 'annual_income']].mean())


# QUESTION 10
def convertToNum(name):
    if name == 'Basic':
        return 0
    if name == 'High School':
        return 1
    elif name == 'Graduation':
        return 2
    elif name == 'PhD':
        return 3
    elif name == 'Master':
        return 4
for x in df.index:
    df.loc[x, 'educational_level'] = convertToNum(df.loc[x, 'educational_level'])

df.plot(kind='scatter', x='educational_level', y='annual_income', color='blue')
df.plot(kind='scatter', x='educational_level', y='total_purchases', color='purple')
plt.show()
