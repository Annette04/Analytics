import pandas as pd
import matplotlib.pyplot as plt

def dinamic_salary_without_prof(csv):
    csv = (csv.groupby(csv["year"]).agg({'middle_salary_to_rub': "mean"}))

    csv['middle_salary_to_rub'] = csv['middle_salary_to_rub'].apply(lambda x: int(x))
    dinamic_salary = csv[['middle_salary_to_rub']].to_dict()
    df = pd.DataFrame.from_dict(dinamic_salary)
    df.reset_index(inplace=True, names=['year'])
    return df

def create_plot(csv_name):
    csv = pd.read_csv(csv_name)
    labelsize1 = 8
    rotation = 90
    salary_by_years = dinamic_salary_without_prof(csv)
    xlabel1 = salary_by_years['year'].tolist()
    ylabel1 = salary_by_years['middle_salary_to_rub'].tolist()
    width = 0.8

    plt.bar(xlabel1, ylabel1, width=width)
    plt.title('Динамика уровня зарплат по годам')
    plt.tick_params(axis='x', rotation=rotation, labelsize=labelsize1)
    plt.xticks(xlabel1)
    plt.tick_params(axis='y', labelsize=labelsize1)
    plt.grid(axis='y')
    salary_by_years.columns = ['Год', 'Зарплата']
    salary_by_years.to_csv(r'salary_by_years.csv', index=False) #сохранение файла для таблицы
    plt.savefig('salary_by_years') #сохранение изображения
    return plt


if __name__ == '__main__':
    create_plot('vac_with_years.csv')