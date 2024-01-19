import pandas as pd
import matplotlib.pyplot as plt


def part_vac_by_area(csv):
    vacancies_count = len(csv)
    vacancies_group_by_city = (csv.groupby("area_name").agg({"name": "count"})
                                .sort_values(by=['name', 'area_name'], ascending=(False, True))['name']
                                .apply(lambda x: round(x / vacancies_count*100, 1)))
    dict_percent = pd.DataFrame(vacancies_group_by_city[vacancies_group_by_city * 100 >= 1].head(10))# Учивываю только те города, в которых больше 1 процента от общего числа вакансий
    dict_percent.reset_index(inplace=True, names=['area_name'])
    p = round(100 - dict_percent['name'].sum(), 1)
    dict_percent.loc[len(dict_percent.index)] = ['Другие', p]
    return dict_percent.sort_values(by='name', ascending=False)


def create_plot(csv_name):
    csv = pd.read_csv(csv_name)
    vac_by_area = part_vac_by_area(csv)
    xlabel1 = vac_by_area['area_name'].tolist()
    ylabel1 = vac_by_area['name'].tolist()
    plt.figure(figsize=(6, 4))
    plt.pie(ylabel1, labels=xlabel1, textprops={'fontsize': 12})
    plt.subplots_adjust(left=0, top=1, bottom=0, right=0.863)
    vac_by_area.columns = ['Город', 'Процент вакансий']
    vac_by_area.to_csv(r'part_vac_by_area.csv', index=False)
    #plt.show()
    plt.savefig('part_vac_by_area')
    return plt


if __name__ == '__main__':
    create_plot('vac_with_years.csv')