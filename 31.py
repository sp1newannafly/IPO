import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Grossmend/CSV/master/titanic/data.csv', nrows=10, usecols=['Name', 'Sex', 'Survived'])
print(df)