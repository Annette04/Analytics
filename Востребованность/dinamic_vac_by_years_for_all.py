import pandas as pd
import matplotlib.pyplot as plt


def dinamic_count_vac_without_prof(csv):
    csv = (csv.groupby(csv["year"]).agg({'name': "count"}))
    dinamic_vacancies = csv[['name']].to_dict()
    df = pd.DataFrame.from_dict(dinamic_vacancies)
    df.reset_index(inplace=True, names=['year'])
    return df


def create_plot(csv_name):
    csv = pd.read_csv(csv_name)
    labelsize1 = 8
    rotation = 90
    vac_by_years = dinamic_count_vac_without_prof(csv)
    xlabel1 = vac_by_years['year'].tolist()
    ylabel1 = vac_by_years['name'].tolist()
    width = 0.8

    plt.bar(xlabel1, ylabel1, width=width)
    plt.title('Динамика количества вакансий по годам')
    plt.tick_params(axis='x', rotation=rotation, labelsize=labelsize1)
    plt.xticks(xlabel1)
    plt.tick_params(axis='y', labelsize=labelsize1)
    plt.grid(axis='y')
    vac_by_years.columns = ['Год', 'Количество вакансий']
    vac_by_years.to_csv(r'vac_count_by_years.csv', index=False)
    plt.savefig('vac_count_by_years')
    return plt


if __name__ == '__main__':
    create_plot('vac_with_years.csv')