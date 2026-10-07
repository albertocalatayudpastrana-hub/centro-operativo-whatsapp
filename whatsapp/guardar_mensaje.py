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
        SELECT id
        FROM mensajes_whatsapp
        WHERE remitente = %s
        AND mensaje = %s
        AND fecha_hora >= NOW() - INTERVAL '30 seconds'
        LIMIT 1
    """, (
        remitente,
        mensaje
    ))

    duplicado = cursor.fetchone()

    if duplicado:
        print("DUPLICADO IGNORADO")
        conn.close()
        return


    cursor.execute("""
        SELECT id
        FROM mensajes_whatsapp
        WHERE remitente = %s
        AND mensaje = %s
        LIMIT 1
    """, (
        remitente,
        mensaje
    ))

    duplicado = cursor.fetchone()

    if duplicado:
        print("DUPLICADO IGNORADO")
        conn.close()
        return

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