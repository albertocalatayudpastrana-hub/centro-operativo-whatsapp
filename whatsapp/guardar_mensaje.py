from database import get_connection

def guardar_mensaje(
    fecha_hora,
    unidad,
    remitente,
    mensaje,
    origen
):
    print("GUARDANDO:")
    print(fecha_hora)
    print(unidad)
    print(mensaje)
    print(origen)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO mensajes_whatsapp
        (
            fecha_hora,
            unidad,
            remitente,
            mensaje,
            origen
        )
        VALUES (%s, %s, %s, %s, %s)
    """, (
        fecha_hora,
        unidad,
        remitente,
        mensaje,
        origen
    ))

    conn.commit()

    print("INSERT OK")

    conn.close()