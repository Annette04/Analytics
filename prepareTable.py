import pandas as pd
import numpy as np

def convert_currency(salary, exchange_rate):
    if not(np.isnan(salary)) and not(np.isnan(exchange_rate)):
        return salary * exchange_rate
    else:
        return float('nan')

def made_table(file):
    table = pd.read_csv(file)
    currency_table = pd.read_csv('currency.csv')

    table['year'] = table['published_at'].apply(lambda x: int(x[:4]))
    table['koef'] = table.apply(lambda i: float(currency_table[i['salary_currency']][currency_table.index[
        currency_table['date'] == i['published_at'][:7]]].values)
    if i['salary_currency'] in currency_table.columns and i['published_at'][:7] in currency_table['date'].to_list()
    else 1 if i['salary_currency'] == "RUR" else float('nan'), axis=1)
    table['published_at'] = pd.to_datetime(table['published_at'])
    table['middle_salary'] = table[['salary_from', 'salary_to']].mean(axis=1)
    table['middle_salary_to_rub'] = table.apply(lambda row: convert_currency(row['middle_salary'], row['koef']), axis=1)
    table_res = table[(table['middle_salary_to_rub'] < 500000) & (table['middle_salary'] > 100)] # Обрезание нереальных зарплат

    table_res.to_csv(r'vac_with_years.csv', index=False)

made_table('vacancies.csv')