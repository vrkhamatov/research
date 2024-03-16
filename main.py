import time
import seaborn as sns
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
def yes_no_frames(df):
        # Создайте DataFrame, содержащий только строки со значением 'Yes' в колонке N+1
        df_yes = df.loc[df[df.columns[-1]] == 1]

        # Создайте DataFrame, содержащий только строки со значением 'No' в колонке N+1
        df_no = df.loc[df[df.columns[-1]] == 0]

        plt.figure(figsize=(12, 8))

        sns.distplot(df['Age'], hist=True, kde=True,
                     color='blue',
                     hist_kws={'edgecolor': 'black'},
                     kde_kws={'linewidth': 2})

        # Построение графика для 'Yes'
        #plt.hist(df_yes['Age'], bins=10, alpha=0.5, label=f'{"Age"} (Yes)', edgecolor='black')

        # Построение графика для 'No'
        #plt.hist(df_no['Age'], bins=10, alpha=0.5, label=f'{"Age"} (No)', edgecolor='black')

        # Настройка графика
        plt.title('Distribution of Parameters (Yes/No)')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.legend()
        plt.grid(True)



        # Отображение графика
        plt.show()

        print("Yes")
        print(df_yes)
        print("No")
        print(df_no)
        # Вычисление медианы параметра Age
        all_age_median = df['Age'].median()
        print("Медиана возраста всей выборки:", all_age_median)
        WFH_age_median = df_yes['Age'].median()
        print("Медиана возраста для WFH:", WFH_age_median)
        WFO_age_median = df_no['Age'].median()
        print("Медиана возраста WFO:", WFO_age_median)

        # Вычисление медианы параметра RM_productive
        all_rm_productive_median = df['RM_productive'].median()
        print("Продуктивность всей выборки:", all_rm_productive_median)
        WFH_prod_median = df_yes['RM_productive'].median()
        print("Продуктивность для WFH:", WFH_prod_median)
        WFO_prod_median = df_no['RM_productive'].median()
        print("Продуктивность для WFO:", WFO_prod_median)



        # Создание DataFrame для объектов выше медианного значения RM_productivity
        above_median_rm_productivity = df[df['RM_productive'] > all_rm_productive_median]

        # Создание DataFrame для объектов ниже медианного значения RM_productivity
        below_median_rm_productivity = df[df['RM_productive'] <= all_rm_productive_median]

        above_median_age = df[df['Age'] > all_age_median]

        below_median_age = df[df['Age'] <=  all_age_median]

        # Построение графика распределения параметров
        plt.figure(figsize=(12, 6))

        # График для Age
        plt.subplot(2, 1, 1)
        sns.distplot(above_median_age['Age'], hist=False, kde=True,
                      color='blue',
                     hist_kws={'edgecolor': 'black'},
                     kde_kws={'linewidth': 2})
        plt.title('Distribution of Age (Above Median)')
        plt.subplot(2, 1, 2)
        sns.distplot(below_median_age['Age'], hist=False, kde=True,
                     color='blue',
                     hist_kws={'edgecolor': 'black'},
                     kde_kws={'linewidth': 2})
        plt.title('Distribution of Age (Below Median)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # Построение графика распределения параметров
        plt.figure(figsize=(12, 6))

        # График для Age
       # plt.subplot(2, 1, 1)
#        print("productive")
 #       print(above_median_rm_productivity)
  #      sns.distplot(above_median_rm_productivity['RM_productive'], hist=False, kde=True,
   #                  color='blue',
    #                 hist_kws={'edgecolor': 'black'},
     #                kde_kws={'linewidth': 2})
      #  plt.title('Distribution of RM_productive (Above Median)')

       # plt.subplot(2, 1, 2)
        sns.distplot(below_median_rm_productivity['RM_productive'], hist=False, kde=True,
                     color='blue',
                     hist_kws={'edgecolor': 'black'},
                     kde_kws={'linewidth': 2})
        plt.title('Distribution of RM_productive (Below Median)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        plt.hist(df['Age'], bins=10, alpha=0.5, edgecolor='black')

        plt.title('Histogram')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # Рассчет среднего значения и стандартного отклонения для всей выборки
        mean_age_all = df['Age'].mean()
        std_dev_age_all = df['Age'].std()

        # Рассчет среднего значения и стандартного отклонения для каждого класса отдельно
        grouped = df.groupby('Occupation')
        mean_age_grouped = grouped['Age'].mean()
        std_dev_age_grouped = grouped['Age'].std()

        print("Средний возраст для всей выборки:", mean_age_all)
        print("Стандартное отклонение для всей выборки:", std_dev_age_all)
        print("\nСредний возраст для каждого класса:")
        print(mean_age_grouped)
        print("\nСтандартное отклонение для каждого класса:")
        print(std_dev_age_grouped)

        # Рассчет среднего значения и стандартного отклонения для всей выборки
        mean_age_all = df_yes['Age'].mean()
        std_dev_age_all = df_yes['Age'].std()

        # Рассчет среднего значения и стандартного отклонения для каждого класса отдельно
        grouped = df_yes.groupby('Occupation')
        mean_age_grouped = grouped['Age'].mean()
        std_dev_age_grouped = grouped['Age'].std()

        print("Средний возраст для WFH:", mean_age_all)
        print("Стандартное отклонение для WFH:", std_dev_age_all)
        print("\nСредний возраст для каждого класса:")
        print(mean_age_grouped)
        print("\nСтандартное отклонение для каждого класса:")
        print(std_dev_age_grouped)

        # Рассчет среднего значения и стандартного отклонения для всей выборки
        mean_age_all = df_no['Age'].mean()
        std_dev_age_all = df_no['Age'].std()

        # Рассчет среднего значения и стандартного отклонения для каждого класса отдельно
        grouped = df_no.groupby('Occupation')
        mean_age_grouped = grouped['Age'].mean()
        std_dev_age_grouped = grouped['Age'].std()

        print("Средний возраст для WFO:", mean_age_all)
        print("Стандартное отклонение для WFO:", std_dev_age_all)
        print("\nСредний возраст для каждого класса:")
        print(mean_age_grouped)
        print("\nСтандартное отклонение для каждого класса:")
        print(std_dev_age_grouped)

        # Рассчет среднего значения и стандартного отклонения для всей выборки
        mean_age_all = df_no['Age'].mean()
        std_dev_age_all = df_no['Age'].std()

        # Рассчет среднего значения и стандартного отклонения для каждого класса отдельно
        grouped = df_no.groupby('Occupation')
        mean_age_grouped = grouped['Age'].mean()
        std_dev_age_grouped = grouped['Age'].std()

        print("Средний возраст для WFO:", mean_age_all)
        print("Стандартное отклонение для WFO:", std_dev_age_all)
        print("\nСредний возраст для каждого класса:")
        print(mean_age_grouped)
        print("\nСтандартное отклонение для каждого класса:")
        print(std_dev_age_grouped)


        #####

        # Рассчет среднего значения и стандартного отклонения для всей выборки
        mean_age_all = df_no['RM_productive'].mean()
        std_dev_age_all = df_no['RM_productive'].std()

        # Рассчет среднего значения и стандартного отклонения для каждого класса отдельно
        grouped = df_no.groupby('Occupation')
        mean_age_grouped = grouped['RM_productive'].mean()
        std_dev_age_grouped = grouped['RM_productive'].std()

        print("Средний показатель продуктивности для WFO:", mean_age_all)
        print("Стандартное отклонение для WFO:", std_dev_age_all)
        print("\nСредний показатель продуктивности для каждого класса:")
        print(mean_age_grouped)
        print("\nСтандартное отклонение для каждого класса:")
        print(std_dev_age_grouped)

        ###

        # Рассчет среднего значения и стандартного отклонения для всей выборки
        mean_age_all = df_yes['RM_productive'].mean()
        std_dev_age_all = df_yes['RM_productive'].std()

        # Рассчет среднего значения и стандартного отклонения для каждого класса отдельно
        grouped = df_yes.groupby('Occupation')
        mean_age_grouped = grouped['RM_productive'].mean()
        std_dev_age_grouped = grouped['RM_productive'].std()

        print("Средний показатель продуктивности для WFH:", mean_age_all)
        print("Стандартное отклонение для WFH:", std_dev_age_all)
        print("\nСредний показатель продуктивности для каждого класса:")
        print(mean_age_grouped)
        print("\nСтандартное отклонение для каждого класса:")
        print(std_dev_age_grouped)

        # Рассчет среднего значения и стандартного отклонения для всей выборки
        mean_age_all = df['RM_productive'].mean()
        std_dev_age_all = df['RM_productive'].std()

        # Рассчет среднего значения и стандартного отклонения для каждого класса отдельно
        grouped = df.groupby('Occupation')
        mean_age_grouped = grouped['RM_productive'].mean()
        std_dev_age_grouped = grouped['RM_productive'].std()

        print("Средний показатель продуктивности для всей выборки:", mean_age_all)
        print("Стандартное отклонение для всей выборки:", std_dev_age_all)
        print("\nСредний показатель продуктивности для каждого класса:")
        print(mean_age_grouped)
        print("\nСтандартное отклонение для каждого класса:")
        print(std_dev_age_grouped)




table = pd.read_csv("WFH_WFO_dataset.csv")
yes_no_frames(table)