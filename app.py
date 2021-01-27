# importar bibliotecas
import flask
from flask import Flask
from joblib import load, dump
import sigmoidal

# carregar nomes dos bairros de Sao Paulo
bairros = sigmoidal.load_bairros()

# instanciar aplicacao
app = Flask(__name__, template_folder='templates')

@app.route("/", methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return flask.render_template('home.html', bairros=bairros)

    if flask.request.method == "POST":
        # pegar os inputs do formulario
        user_input = {
            'Condo': flask.request.form['condo'],
            'Size': flask.request.form['size'],
            'Rooms': flask.request.form['rooms'],
            'Toilets': flask.request.form['toilets'],
            'Suites': flask.request.form['suites'],
            'Parking': flask.request.form['parking'],
            'District': flask.request.form['district'],
            'Elevator': flask.request.form.get('elevator') == 'on',
            'Furnished': flask.request.form.get('furnished') == 'on',
            'Swimming Pool': flask.request.form.get('swimming_pool') == 'on',
            'New': flask.request.form.get('new') == 'on'
        }

        price = sigmoidal.predict_price(user_input)
        print(price)

        return flask.render_template('home.html', bairros=bairros, price=price, user_input=user_input)


if __name__ == '__main__':
    app.run(debug=True)
