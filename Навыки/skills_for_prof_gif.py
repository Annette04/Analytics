import pandas as pd
import matplotlib.pyplot as plt

def create_plot():
    csv = pd.read_csv('prepare_vac_for_gif.csv')
    labelsize1 = 8
    rotation = 90
    years = csv['year'].unique()
    for year in years:
        df = csv[csv['year'] == year]
        xlabel1 = df['skill'].tolist()
        ylabel1 = df['count'].tolist()
        plt.figure(figsize=(10, 5))
        plt.barh(xlabel1, ylabel1, color='orchid')
        plt.title(f'ТОП-20 навыков в сфере IT за {year} год')
        plt.gca().invert_yaxis()
        plt.tick_params(axis='x', rotation=rotation, labelsize=labelsize1)
        plt.tick_params(axis='y', labelsize=9)
        plt.grid(axis='x')
        plt.subplots_adjust(left=0.29, right=0.95, top=0.95, bottom=0.14)
        plt.savefig(f'top_skills_for_prof_in_{year}')
        plt.close()
    return plt


if __name__ == '__main__':
    create_plot()