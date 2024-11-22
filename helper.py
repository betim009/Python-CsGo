import pandas as pd

file = pd.read_excel('./weapons.xlsx')
new_file = file.to_csv('./weapons.csv')