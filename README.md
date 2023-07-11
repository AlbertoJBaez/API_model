# API_model
En este ejercicio se ha desarrollado una API utilizando Flask para consumir un modelo de machine learning que realiza predicciones de ventas a partir de los gastos en publicidad en televisión, radio y periódicos. La API permite obtener predicciones, almacenar nuevos registros en la base de datos y reentrenar el modelo con nuevos datos.

# Endpoints de la API
La API proporciona los siguientes endpoints:

GET /v2/predict: Permite obtener la predicción de ventas a partir de los valores de gastos en publicidad. Los parámetros tv, radio y newspaper deben ser proporcionados en la URL. Ejemplo: http://localhost:5000/v2/predict?tv=100&radio=50&newspaper=75.

POST /v2/ingest_data: Permite almacenar nuevos registros de gastos en publicidad en la base de datos. Los parámetros tv, radio, newspaper y sales deben ser proporcionados en el cuerpo de la solicitud.

PUT /v2/retrain: Permite reentrenar el modelo utilizando los registros de gastos en publicidad almacenados en la base de datos.

Notas adicionales
El modelo de machine learning utilizado se encuentra en el archivo model.pkl. Si deseas utilizar otro modelo, debes reemplazar ese archivo con tu propio modelo entrenado.

La base de datos SQLite se encuentra en el archivo database.db. Puedes utilizar herramientas como SQLite Browser para ver y gestionar los datos almacenados en la base de datos.

Asegúrate de tener los permisos adecuados para leer y escribir archivos en el directorio donde se encuentra la aplicación Flask.

Si deseas realizar pruebas adicionales, puedes utilizar herramientas como Postman para enviar solicitudes HTTP a la API y verificar las respuestas.

¡Gracias por revisar este trabajo! Si tienes alguna pregunta o problema, no dudes en hacérmelo saber.
