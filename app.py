from flask import Flask, request
from datetime import datetime

from whatsapp.guardar_mensaje import guardar_mensaje

from unidades import UNIDADES_VALIDAS
import re

def detectar_unidad(remitente, mensaje):

    texto = f"{remitente} {mensaje}"

    numeros = re.findall(r"\b\d{2,3}\b", texto)

    for numero in numeros:

        numero = numero.zfill(3)

        if numero in UNIDADES_VALIDAS:
            return numero

    return "000"

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Centro Operativo funcionando"

@app.route("/mensaje", methods=["POST"])
def recibir_mensaje():

    datos = request.json

    unidad_detectada = detectar_unidad(
        datos["remitente"],
        datos["mensaje"]
    )

    guardar_mensaje(
        datetime.now(),
        unidad_detectada,
        datos["remitente"],
        datos["mensaje"],
        datos["origen"]
    )

    return {
        "status": "ok"
    }

if __name__ == "__main__":
    app.run(
    host="0.0.0.0",
    port=5000,
    debug=True
    )