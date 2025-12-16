#=======================================================================
# ARCHIVO: crud_deudores_botones.py
# OBJETIVO: CRUD con botones (TKINTER + MYSQL) para tabla deudores
# =======================================================================

import mysql.connector
import tkinter as tk
from tkinter import messagebox

#=======================================================================
# 1. CONEXIÓN ABIERTA A MYSQL
# =======================================================================
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inventario_esmeralda"
)




def crear_deudor():
    nombre = entry_nombre.get()
    identificacion = entry_identificacion.get()
    direccion = entry_direccion.get()
    ciudad = entry_ciudad.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()
    contacto = entry_contacto.get()
    estado = entry_estado.get()

    cursor = conexion.cursor()
    sql = """
        INSERT INTO deudores (nombre, identificacion, direccion, ciudad, telefono, correo, contacto, estado)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
    """
    valores = (nombre, identificacion, direccion, ciudad, telefono, correo, contacto, estado)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Deudor creado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))



def consultar_deudores():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM deudores;")

    text_salida.delete("1.0", tk.END)

    text_salida.insert(tk.END, "CAMPOS:\n")
    for c in cursor.column_names:
        text_salida.insert(tk.END, f"{c}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")
    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")



def actualizar_deudor():
    id_deudor = entry_id_deudor.get()
    nuevo_nombre = entry_nombre.get()
    nueva_direccion = entry_direccion.get()
    nueva_ciudad = entry_ciudad.get()
    nuevo_telefono = entry_telefono.get()
    nuevo_correo = entry_correo.get()
    nuevo_contacto = entry_contacto.get()
    nuevo_estado = entry_estado.get()

    cursor = conexion.cursor()
    sql = """
        UPDATE deudores 
        SET nombre=%s, direccion=%s, ciudad=%s, telefono=%s, correo=%s, contacto=%s, estado=%s
        WHERE id_deudor=%s;
    """
    valores = (nuevo_nombre, nueva_direccion, nueva_ciudad, nuevo_telefono, nuevo_correo, nuevo_contacto, nuevo_estado, id_deudor)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Deudor actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))



def eliminar_deudor():
    id_deudor = entry_id_deudor.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM deudores WHERE id_deudor = %s;"
    try:
        cursor.execute(sql, (id_deudor,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Deudor eliminado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))



ventana = tk.Tk()
ventana.title("CRUD Deudores")
ventana.geometry("700x600")


tk.Label(ventana, text="ID Deudor (para Actualizar/Eliminar)").pack()
entry_id_deudor = tk.Entry(ventana)
entry_id_deudor.pack()

tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Identificación").pack()
entry_identificacion = tk.Entry(ventana)
entry_identificacion.pack()

tk.Label(ventana, text="Dirección").pack()
entry_direccion = tk.Entry(ventana)
entry_direccion.pack()

tk.Label(ventana, text="Ciudad").pack()
entry_ciudad = tk.Entry(ventana)
entry_ciudad.pack()

tk.Label(ventana, text="Teléfono").pack()
entry_telefono = tk.Entry(ventana)
entry_telefono.pack()

tk.Label(ventana, text="Correo").pack()
entry_correo = tk.Entry(ventana)
entry_correo.pack()

tk.Label(ventana, text="Contacto").pack()
entry_contacto = tk.Entry(ventana)
entry_contacto.pack()

tk.Label(ventana, text="Estado (Activo/Inactivo)").pack()
entry_estado = tk.Entry(ventana)
entry_estado.pack()


tk.Button(ventana, text="Crear Deudor", command=crear_deudor, bg="#CBEC0B", fg="black").pack(pady=5)
tk.Button(ventana, text="Consultar Deudores", command=consultar_deudores, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar Deudor", command=actualizar_deudor, bg="#FFC107", fg="black").pack(pady=5)
tk.Button(ventana, text="Eliminar Deudor", command=eliminar_deudor, bg="#F44336", fg="white").pack(pady=5)


text_salida = tk.Text(ventana, height=15, width=80)
text_salida.pack(pady=10)

ventana.mainloop()
ventana.mainloop()