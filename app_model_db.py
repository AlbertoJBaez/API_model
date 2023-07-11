from flask import Flask, request, jsonify
import os
import pickle
from sklearn.model_selection import cross_val_score
import pandas as pd
import sqlite3


os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def hello():
    return "Bienvenido a mi API del modelo advertising"

@app.route('/v2/predict', methods=['GET'])
def predict():
    model = pickle.load(open('data/advertising_model','rb'))

    tv = request.args.get('tv', None)
    radio = request.args.get('radio', None)
    newspaper = request.args.get('newspaper', None)

    if tv is None or radio is None or newspaper is None:
        return "Missing args, the input values are needed to predict"
    else:
        prediction = model.predict([[int(tv),int(radio),int(newspaper)]])
        return "The prediction of sales investing that amount of money in TV, radio and newspaper is: " + str(round(prediction[0],2)) + 'k €'

@app.route('/v2/ingest_data', methods=['POST'])
def ingest_data():
    tv = request.args.get('TV')
    radio = request.args.get('radio')
    newspaper = request.args.get('newspaper')
    sales = request.args.get('sales')

    if tv is None or radio is None or newspaper is None or sales is None or tv == '' or radio == '' or newspaper == '' or sales == '':
        return 'Missing parameters. All fields (TV, radio, newspaper, sales) are required.'

    try:
        # Establecer la conexión a la base de datos
        connection = sqlite3.connect('data/advertising.db')
        cursor = connection.cursor()

        # Insertar el nuevo registro en la tabla
        insert_query = '''
            INSERT INTO Advertising (TV, radio, newpaper, sales)
            VALUES (?, ?, ?, ?)
        '''
        cursor.execute(insert_query, (float(tv), float(radio), float(newspaper), float(sales)))

        # Confirmar los cambios y cerrar la conexión a la base de datos
        connection.commit()
        connection.close()

        return 'Data ingested successfully'
    except ValueError:
        return 'Invalid parameter values. The values of TV, radio, newspaper, and sales must be numbers.'
    except Exception as e:
        return f'An error occurred: {str(e)}'
    
@app.route('/v2/ingest_data_json', methods=['POST'])
def ingest_data_json():
    data = request.get_json()
    
    # Aquí puedes realizar las operaciones necesarias para almacenar los datos
    # en tu base de datos o en cualquier otro lugar
    
    # Por ejemplo, si deseas almacenar los datos en una base de datos SQLite:
    connection = sqlite3.connect('data/advertising.db')
    cursor = connection.cursor()
    for record in data:
        # Supongamos que cada registro tiene tres campos: 'tv', 'radio', 'newspaper'
        tv = record.get('tv')
        radio = record.get('radio')
        newspaper = record.get('newspaper')
        sales = record.get('sales')
        # Realiza la inserción del registro en tu tabla de base de datos
        cursor.execute("INSERT INTO Advertising (TV, radio, newpaper, sales) VALUES (?, ?,?, ?)", (tv, radio, newspaper, sales))
    connection.commit()
    connection.close()

    # Retorna una respuesta indicando que los datos han sido ingestados correctamente
    return 'Data ingested successfully'


@app.route('/v2/retrain', methods=['PUT'])
def retrain_model():
    # Obtener los datos de la base de datos
    connection = sqlite3.connect('data/advertising.db')
    query = "SELECT TV, radio, newpaper, sales FROM Advertising"
    df = pd.read_sql_query(query, connection)
    connection.close()

    X = df[['TV', 'radio', 'newpaper']]
    y = df['sales']

    # Reentrenar el modelo con los nuevos datos
    model = pickle.load(open('data/advertising_model', 'rb'))
    model.fit(X, y)  # Reemplaza X e y con tus datos de entrenamiento

    # Guardar el modelo actualizado
    updated_model_file = 'data/updated_advertising_model'
    pickle.dump(model, open(updated_model_file, 'wb'))

    return 'Model retrained and updated successfully'

app.run()

