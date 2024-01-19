import pandas as pd
def made_table_for_vac():
    vac_names = 'Android|android|андроид|andorid|andoroid|andriod|andrind|xamarin'
    table = pd.read_csv('vac_with_years.csv')
    table = table[table['name'].str.contains(vac_names)]
    table.to_csv('resultTable.csv', index=False)

made_table_for_vac()