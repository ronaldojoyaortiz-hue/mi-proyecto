#=======================================================================
# ARCHIVO: crud_alertas_botones.py
# OBJETIVO: CRUD con botones (TKINTER + MYSQL) para tabla alertas
# =======================================================================

import mysql.connector      # Librería para conectar Python con Mysql
import tkinter as tk
from tkinter import messagebox

#=======================================================================
# 1. CONEXION ABIERTA A MYSQL (NO SE CIERRA)
# =======================================================================
conexion = mysql.connector.connect(
    host="localhost",             # Servidor Mysql
    user="root",                  # Usuario de Mysql
    password="",                  # Contraseña (vacía si no tiene)
    database="inventario_esmeralda"   # Base de datos a conectar
)

#=======================================================================
# 2. FUNCIONES CRUD
# =======================================================================

# CREATE
def crear_alerta():
    id_producto = entry_id_producto.get()
    fecha_alerta = entry_fecha_alerta.get()
    dias_restantes = entry_dias_restantes.get()

    cursor = conexion.cursor()
    sql = """
        INSERT INTO alertas (id_producto, fecha_alerta, dias_restantes)
        VALUES (%s, %s, %s);
    """
    valores = (id_producto, fecha_alerta, dias_restantes)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Alerta creada correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# READ
def consultar_alertas():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM alertas;")

    text_salida.delete("1.0", tk.END)  # Limpiar pantalla

    text_salida.insert(tk.END, "CAMPOS:\n")
    for c in cursor.column_names:
        text_salida.insert(tk.END, f"{c}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")

    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")


# UPDATE
def actualizar_alerta():
    id_alerta = entry_id_alerta.get()
    nueva_fecha = entry_fecha_alerta.get()
    nuevos_dias = entry_dias_restantes.get()

    cursor = conexion.cursor()
    sql = """
        UPDATE alertas 
        SET fecha_alerta =dias_restantes = 
        WHERE id_alerta = ;
    """
    valores = (nueva_fecha, nuevos_dias, id_alerta)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Alerta actualizada correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# DELETE
def eliminar_alerta():
    id_alerta = entry_id_alerta.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM alertas WHERE id_alerta = %s;"
    try:
        cursor.execute(sql, (id_alerta,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Alerta eliminada correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))


#=======================================================================
# 3. INTERFAZ GRAFICA TKINTER
# =======================================================================
ventana = tk.Tk()
ventana.title("CRUD Alertas")
ventana.geometry("600x500")

#ENTRADA========================================================
tk.Label(ventana, text="ID Alerta (para Update/Delete)").pack()
entry_id_alerta = tk.Entry(ventana)
entry_id_alerta.pack()

tk.Label(ventana, text="ID Producto").pack()
entry_id_producto = tk.Entry(ventana)
entry_id_producto.pack()

tk.Label(ventana, text="Fecha Alerta (YYYY-MM-DD)").pack()
entry_fecha_alerta = tk.Entry(ventana)
entry_fecha_alerta.pack()

tk.Label(ventana, text="Días Restantes").pack()
entry_dias_restantes = tk.Entry(ventana)
entry_dias_restantes.pack()

#============BOTONES===========#
tk.Button(ventana, text="Crear Alerta", command=crear_alerta, bg="#CBEC0B", fg="black").pack(pady=5)
tk.Button(ventana, text="Consultar Alertas", command=consultar_alertas, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar Alerta", command=actualizar_alerta, bg="#FFC107", fg="black").pack(pady=5)
tk.Button(ventana, text="Eliminar Alerta", command=eliminar_alerta, bg="#F44336", fg="white").pack(pady=5)

#=========CAJA DE TEXTO PARA MOSTRAR RESULTADOS =========#
text_salida = tk.Text(ventana, height=10, width=60)
text_salida.pack(pady=10)

ventana.mainloop()