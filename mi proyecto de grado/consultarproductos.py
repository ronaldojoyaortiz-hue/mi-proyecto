#=======================================================================
# ARCHIVO: consultar_clientes.py
# OBJETIVO: Conectar a Mysql y mantener
#           la conexion abierta y consultar la tabla clientes
# ======================================================================= 


import mysql.connector      # Librería para conectar Python con Mysql

#Creamos la conexión sin cerrarla
conexion = mysql.connector.connect(
    host="localhost",                                  # Servidor Mysql
    user="root",                                       # Usuario de Mysql
    password="",                                       # Contraseña (vacía si no tiene)
    database="inventario_esmeralda"                          # Base de datos a conectar
)

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="inventario_esmeralda"
    )

    if conexion.is_connected():
        print("Conexión establecida correctamente\n")

    cursor = conexion.cursor()
    consulta_sql = "SELECT * FROM productos;"
    cursor.execute(consulta_sql)

    print("CAMPOS DE LA TABLA productos:")
    for campo in cursor.column_names:
        print(f"- {campo}")

    print("\nREGISTROS DE productos:\n")
    for fila in cursor.fetchall():
        print(fila)

except mysql.connector.Error as e:
    print(f"Error al conectar o consultar: {e}")

finally:
    if conexion.is_connected():
        cursor.close()
        conexion.close()
        print("\nConexión cerrada.")