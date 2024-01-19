import pandas as pd
import matplotlib.pyplot as plt


def top_skills(csv):
    csv = csv.dropna(subset=['key_skills'])
    csv['skills_count'] = csv['key_skills'].apply(lambda x: x.replace(', ', '\n')
                                                        .replace('#', '\n')
                                                        .split('\n'))

    df = (csv.apply(lambda x: pd.Series(x['skills_count']), axis=1).stack().reset_index(level=1, drop=True)
          .apply(lambda x: x.strip().lower()))
    df.name = 'skill'
    df_new = csv.join(df)

    df_new = df_new[df_new['skill'] != '']
    top_skills_by_year = (df_new.groupby(['year', 'skill']).size().reset_index(name='count')
                          .sort_values(by=['year', 'count'], ascending=[True, False]).groupby('year').head(20))
    top_skills_by_year2 = (df_new.groupby('skill').agg({"skills_count": "count"}).reset_index(names='skill')
                            .sort_values(by='skills_count', ascending=False).head(20))
    return top_skills_by_year2, top_skills_by_year


def create_plot():
    csv = pd.read_csv('vac_with_years.csv')
    labelsize1 = 8
    rotation = 90
    skills, file_to_save = top_skills(csv)
    xlabel1 = skills['skill'].tolist()
    ylabel1 = skills['skills_count'].tolist()

    plt.barh(xlabel1, ylabel1)
    plt.title(f'ТОП-20 навыков')
    plt.gca().invert_yaxis()
    plt.tick_params(axis='x', rotation=rotation, labelsize=labelsize1)
    plt.tick_params(axis='y', labelsize=6)
    plt.grid(axis='x')
    skills.columns = ['Навык', 'Частота появления навыка в вакансиях']
    skills.to_csv(r'top_skills_for_all.csv', index=False)
    file_to_save.to_csv(r'prepare_for_gif.csv', index=False)
    #plt.show()
    plt.savefig('top_skills_for_prof')
    return plt


if __name__ == '__main__':
    create_plot()