import pandas as pd
import matplotlib.pyplot as plt


def salary_by_area_without_prof(csv):
    vacancies_count = len(csv)
    vacancies_group_by_city = (csv.groupby("area_name").agg({'middle_salary_to_rub': "mean", "name": "count"})
                               .sort_values(by=['middle_salary_to_rub', 'area_name'], ascending=(False, True)))
    vacancies_group_by_city['middle_salary_to_rub'] = vacancies_group_by_city['middle_salary_to_rub'].apply(lambda x: int(x))
    dict_salary = pd.DataFrame(vacancies_group_by_city[vacancies_group_by_city['name'] / vacancies_count * 100 >= 1]
                               ['middle_salary_to_rub'].head(20)) # Учивываю только те города, в которых больше 1 процента от общего числа вакансий
    dict_salary.reset_index(inplace=True, names=['area_name'])
    return dict_salary


def create_plot(csv_name):
    csv = pd.read_csv(csv_name)
    labelsize1 = 8
    rotation = 90
    salary_by_area = salary_by_area_without_prof(csv)
    xlabel1 = salary_by_area['area_name'].apply(lambda x: x.replace(' ', '\n').replace('-', '\n')).tolist()
    ylabel1 = salary_by_area['middle_salary_to_rub'].tolist()

    plt.barh(xlabel1, ylabel1)
    plt.title('Уровень зарплат по городам')
    plt.gca().invert_yaxis()
    plt.tick_params(axis='x', rotation=rotation, labelsize=labelsize1)
    plt.tick_params(axis='y', labelsize=6)
    plt.grid(axis='x')
    salary_by_area.columns = ['Город', 'Средний оклад']
    salary_by_area.to_csv(r'salary_by_area.csv', index=False)
    plt.savefig('salary_by_area')
    return plt


if __name__ == '__main__':
    create_plot('vac_with_years.csv')