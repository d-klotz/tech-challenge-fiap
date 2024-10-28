import os
import random
import logging
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score


def main():

    folder_list = ['data','TechChallenge']
    file_list = ['us-insurance-data.csv', 'TechChallenge.log']

    data_int= 1400
    gen_folder(folder_list, folder_list[1], file_list[1])

    logging.basicConfig(filename=f'{folder_list[1]}/{file_list[1]}', encoding='utf-8', level=logging.INFO)
    logging.info(f' As pastas {folder_list} foram criadas.')
    
    gen_database(data_int, folder_list[0], file_list[0])
    logging.info(f' A base de dados "{file_list[0]}" foi gerada com {data_int} pessoas fictícias.')

    data = pd.read_csv('data/us-insurance-data.csv')
    df = pd.read_csv('data/us-insurance-data-test.csv')

    #print(data.dtypes)
    #print(df.dtypes)

    #data_processing(data)
    data_processing(df)


def data_processing(data):

    for category in ['gender', 'smoker', 'region']:
        data[category] = LabelEncoder().fit_transform(data[category])

    x = data[['age', 'gender', 'bmi', 'children', 'smoker', 'region']]
    y = data[['charges']]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=7)
    

    #linear_regression(x_train, x_test, y_train, y_test)

    random_forest(x_train, x_test, y_train, y_test)


def linear_regression(x_train, x_test, y_train, y_test):

    cl_model = LinearRegression()
    cl_model.fit(x_train, y_train)

    y_predito = cl_model.predict(x_test)

    r_square = r2_score(y_test, y_predito)
    print(f'R² %: {r_square}')

    gen_graph(y_test, y_predito)


def random_forest(x_train, x_test, y_train, y_test):

    rf_model = RandomForestRegressor(y_est=2, random_state=7)
    rf_model.fit(x_train, y_train.values.ravel())

    y_predito = rf_model.predict(x_test)

    r_square = r2_score(y_test, y_predito)
    print(f'R² %: {r_square}')


def gen_graph(y_test, y_predito):
    
    plt.figure(figsize=(8,8))
    plt.scatter(y_test, y_predito, alpha=0.2)

    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()])
    plt.title('PREVISÕES DOS CUSTOS MÉDICOS INDIVIDUAIS')

    plt.show()


def gen_folder(folder_list, log_folder, log_file):

    for folder in folder_list:
        if not os.path.exists(folder):
            os.makedirs(folder)

    with open(f'{log_folder}/{log_file}', 'w'):
        pass


def gen_database(data_int, data_folder, data_file):
    
    data = []
    for _ in range(data_int):
        age = random.randint(18, 60)
        gender = random.choice(['male', 'female'])
        smoker = random.choice(['yes', 'no'])
        region = random.choice(['northeast', 'northwest', 'southeast', 'southwest'])
        
        if age <= 25:
            bmi = round(random.uniform(18.5, 40), 3)
            children = random.randint(0, 2)
            charges = round(random.uniform(0, 20000), 5)
        else:
            bmi = round(random.uniform(19.5, 40), 3)
            children = random.randint(0, 5)
            charges = round(random.uniform(0, 50000), 5)

        data.append([age, gender, bmi, children, smoker, region, charges])
    
    df = pd.DataFrame(data, columns=['age', 'gender', 'bmi', 'children', 'smoker', 'region', 'charges'])

    df.to_csv(f'{data_folder}/{data_file}', encoding='utf-8', index=False)


if __name__ == "__main__":
    main()