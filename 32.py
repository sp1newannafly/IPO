import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Grossmend/CSV/master/titanic/data.csv', nrows=10)

# Формат каждого столбца
print('\n', 'Формат столбцов:')
print(df.dtypes)

# Размерность DataFrame
print('\n', 'Размерность:')
print(df.shape)

# Общая статистика
print('\n', 'Общая статистика')
print(df.describe())