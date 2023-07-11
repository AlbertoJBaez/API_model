# Advertising Model API

Este proyecto es una API que proporciona funcionalidades relacionadas con un modelo de publicidad. Permite realizar predicciones de ventas y gestionar datos de publicidad.

## Funcionalidades

- Predicción de ventas: La API ofrece una ruta `/v2/predict` que permite hacer predicciones de ventas en función de los gastos de publicidad en TV, radio y periódicos.

- Ingesta de datos: La API proporciona rutas para ingresar datos de publicidad, ya sea a través de una solicitud POST en `/v2/ingest_data` o mediante una solicitud POST con formato JSON en `/v2/ingest_data_json`. Esto permite agregar nuevos registros a la base de datos de publicidad.

- Retraining del modelo: La API tiene una ruta `/v2/retrain` que permite reentrenar el modelo de publicidad utilizando los datos almacenados en la base de datos.

## Requisitos

- Python 3.11 o superior
- Flask
- scikit-learn
- pandas

## Instalación

1. Clona este repositorio en tu máquina local:
# Endpoints de la API
La API proporciona los siguientes endpoints:

GET /v2/predict: Permite obtener la predicción de ventas a partir de los valores de gastos en publicidad. Los parámetros tv, radio y newspaper deben ser proporcionados en la URL. Ejemplo: http://localhost:5000/v2/predict?tv=100&radio=50&newspaper=75.

POST /v2/ingest_data: Permite almacenar nuevos registros de gastos en publicidad en la base de datos. Los parámetros tv, radio, newspaper y sales deben ser proporcionados en el cuerpo de la solicitud.

PUT /v2/retrain: Permite reentrenar el modelo utilizando los registros de gastos en publicidad almacenados en la base de datos.

Notas adicionales
El modelo de machine learning utilizado se encuentra en el archivo model.pkl. Si deseas utilizar otro modelo, debes reemplazar ese archivo con tu propio modelo entrenado.

La base de datos SQLite se encuentra en el archivo database.db. Puedes utilizar herramientas como SQLite Browser para ver y gestionar los datos almacenados en la base de datos. También puedes acceder al archivo csv a partir del cual se ha creado la base de datos y el ejecutable para crearla.

Asegúrate de tener los permisos adecuados para leer y escribir archivos en el directorio donde se encuentra la aplicación Flask.

Si deseas realizar pruebas adicionales, puedes utilizar herramientas como Postman para enviar solicitudes HTTP a la API y verificar las respuestas.

¡Gracias por revisar este trabajo! Si tienes alguna pregunta o problema, no dudes en hacérmelo saber.

Si no deseas usar el despliegue con Docker o no tienes instalado Docker, también puedes ejecutarlo en tu ordenador local con el archivo app_model_db y ejecutarlo en tu ordenador local.
