# importar as bibliotecas
import pandas as pd
from joblib import load
import flask


def load_bairros():
    with open("data/bairros.joblib", 'rb') as file:
        bairros = load(file)

    return bairros


def load_model():
    with open("data/model.joblib", 'rb') as file:
        model = load(file)

    return model


def predict_price(user_input):
    # carregar modelo
    model = load_model()

    # importar nomes das features
    with open('data/features.names', 'rb') as file:
        features_names = load(file)

    # criar dataframe para prediction
    df = pd.DataFrame(index=[0], columns=features_names)
    df = df.fillna(value=0)

    # extrair valores do dicionario para o dataframe
    district = "District_" + user_input.pop('District')
    df[district] = 1

    for feature in user_input.items():
        df[feature[0]] = feature[1]

    # converter strings em floats
    df = df.astype(float)

    for i in df.columns:
       print(i)

    # prever o valor de venda do imovel usando XGBoost
    y_pred = model.predict(df)

    return y_pred