import requests
import pandas as pd
from io import StringIO

def made_currency_data(currency_data):
    for date in dates:
        da = str(date.strftime('%d/%m/%Y'))
        response = requests.get(f'{url}?date_req={da}').text
        if response.startswith('<'):
            month_df = pd.read_xml(StringIO(response))
            month_df['VunitRate'] = (month_df["Value"].str.replace(",", ".").astype(float) / month_df["Nominal"]).round(
                10)
            curr_df = month_df[month_df["CharCode"].isin(currency_data.columns)][["CharCode", "VunitRate"]].groupby(
                'CharCode').sum().T.rename_axis(None, axis=1).reset_index().drop("index", axis=1)
            curr_df["date"] = date.strftime('%Y-%m')
            currency_data = pd.concat([currency_data, curr_df])
    return currency_data


if __name__ == '__main__':
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    df = pd.read_csv('vacancies.csv')
    currency = df['salary_currency'].dropna().unique().tolist()
    currency.remove('RUR')
    currency_data = pd.DataFrame(columns=['date'] + currency)
    start_date = '01' + pd.to_datetime(df['published_at'].min()).strftime('/%m/%Y')
    end_date = '01' + pd.to_datetime(df['published_at'].max()).strftime('/%m/%Y')
    dates = pd.date_range(start=start_date, end=end_date, freq='MS')
    currency_data = made_currency_data(currency_data)
    currency_data.to_csv('currency.csv', index=False)