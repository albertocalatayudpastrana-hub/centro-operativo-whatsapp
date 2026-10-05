from database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mensajes_whatsapp (
    id SERIAL PRIMARY KEY,
    fecha_hora TIMESTAMP NOT NULL,
    unidad VARCHAR(3) NOT NULL,
    mensaje TEXT NOT NULL,
    creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("TABLA mensajes_whatsapp CREADA")