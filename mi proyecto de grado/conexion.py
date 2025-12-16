#=======================================================================
# ARCHIVO: crud_clientes_botones.py
# OBJETIVO: CRUD con botones (TKINTER + MYSQL)
# ======================================================================= 

import mysql.connector      # Librería para conectar Python con Mysql
import tkinter as tk
from tkinter import messagebox

#=======================================================================
# 1. CONEXION ABIERTA A MYSQL (NO SE CIERRA)
# ======================================================================= 
conexion = mysql.connector.connect(
    host="localhost",                                  # Servidor Mysql
    user="root",                                       # Usuario de Mysql
    password="",                                       # Contraseña (vacía si no tiene)
    database="sistema_ventas"                          # Base de datos a conectar
)

if conexion.is_connected():
    print("Conexión a la base de datos establecida y ABIERTA")


#=======================================================================
# 2. FUNCIONES CRUD
# =======================================================================    

