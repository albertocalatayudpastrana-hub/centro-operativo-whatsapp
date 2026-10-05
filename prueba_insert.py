from database import get_connection
from datetime import datetime

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
INSERT INTO mensajes_whatsapp
(fecha_hora, unidad, mensaje)
VALUES (%s, %s, %s)
""", (
    datetime.now(),
    "180",
    "180 parado en Córdoba"
))

conn.commit()
conn.close()

print("REGISTRO GUARDADO")