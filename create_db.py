import sqlite3
import pandas as pd

def create_database_from_csv(csv_file, db_file, table_name):
    # Leer el archivo CSV y realizar las transformaciones necesarias
    df = pd.read_csv(csv_file)
    df['newpaper'] = df['newpaper'].replace('s', '', regex=True)
    df['newpaper'] = df['newpaper'].astype(float)
    
    # Establecer la conexión a la base de datos
    connection = sqlite3.connect(db_file)
    
    # Crear la tabla en la base de datos a partir del DataFrame
    df.to_sql(table_name, connection, if_exists='replace', index=False)
    
    # Cerrar la conexión a la base de datos
    connection.close()

# Llamar a la función para crear la base de datos a partir del archivo CSV
create_database_from_csv('data/Advertising.csv', 'data/advertising.db', 'Advertising')

import sqlite3

# Establecer la conexión a la base de datos
connection = sqlite3.connect('data/advertising.db')
cursor = connection.cursor()

# Ejecutar una sentencia ALTER TABLE para eliminar la columna "Unnamed: 0"
alter_query = "ALTER TABLE Advertising DROP COLUMN 'Unnamed: 0'"
cursor.execute(alter_query)

# Confirmar los cambios y cerrar la conexión a la base de datos
connection.commit()
connection.close()

