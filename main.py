import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def main():
    data = pd.read_csv('data/us-insurance-data.csv')

    linear_regression(data)


def linear_regression(data):
    flt_columns = ['age', 'bmi', 'children']
    str_columns = ['sex', 'smoker', 'region']

    data[flt_columns] = SimpleImputer().fit_transform(data[flt_columns])

    for column in str_columns:
        data[column] = LabelEncoder().fit_transform(data[column])

    x = data.drop('charges', axis=1)
    y = data['charges']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=7)

    lnr_reg = LinearRegression().fit(x_train, y_train).predict(x_test)

    crt_graph(y_test, lnr_reg)


def crt_graph(y_test, lnr_reg):
    plt.figure(figsize=(8,8))
    plt.scatter(y_test, lnr_reg, color='green', alpha=0.2)

    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()])
    plt.title('PREVISÕES DOS CUSTOS MÉDICOS INDIVIDUAIS')

    plt.show()


if __name__ == "__main__":
    main()