#=======================================================================
# ARCHIVO: crud_categorias_botones.py
# OBJETIVO: CRUD con botones (TKINTER + MYSQL) para tabla categorias
# =======================================================================

import mysql.connector
import tkinter as tk
from tkinter import messagebox

#=======================================================================
# 1. CONEXION ABIERTA A MYSQL
# =======================================================================
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inventario_esmeralda"
)


# CREATE
def crear_categoria():
    nombre = entry_nombre.get()
    descripcion = entry_descripcion.get()
    estado = entry_estado.get()

    cursor = conexion.cursor()
    sql = """
        INSERT INTO categorias (nombre, descripcion, estado)
        VALUES (%s, %s, %s);
    """
    valores = (nombre, descripcion, estado)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Categoría creada correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# READ
def consultar_categorias():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM categorias;")

    text_salida.delete("1.0", tk.END)

    text_salida.insert(tk.END, "CAMPOS:\n")
    for c in cursor.column_names:
        text_salida.insert(tk.END, f"{c}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")
    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")


# UPDATE
def actualizar_categoria():
    id_categoria = entry_id_categoria.get()
    nuevo_nombre = entry_nombre.get()
    nueva_descripcion = entry_descripcion.get()
    nuevo_estado = entry_estado.get()

    cursor = conexion.cursor()
    sql = """
        UPDATE categorias 
        SET nombre = %s, descripcion = %s, estado = %s
        WHERE id_categoria = %s;
    """
    valores = (nuevo_nombre, nueva_descripcion, nuevo_estado, id_categoria)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Categoría actualizada correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# DELETE
def eliminar_categoria():
    id_categoria = entry_id_categoria.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM categorias WHERE id_categoria = %s;"
    try:
        cursor.execute(sql, (id_categoria,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Categoría eliminada correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))



ventana = tk.Tk()
ventana.title("CRUD Categorías")
ventana.geometry("600x500")

tk.Label(ventana, text="ID Categoría (para Update/Delete)").pack()
entry_id_categoria = tk.Entry(ventana)
entry_id_categoria.pack()

tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Descripción").pack()
entry_descripcion = tk.Entry(ventana)
entry_descripcion.pack()

tk.Label(ventana, text="Estado (Activa/Inactiva)").pack()
entry_estado = tk.Entry(ventana)
entry_estado.pack()


tk.Button(ventana, text="Crear Categoría", command=crear_categoria, bg="#CBEC0B", fg="black").pack(pady=5)
tk.Button(ventana, text="Consultar Categorías", command=consultar_categorias, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar Categoría", command=actualizar_categoria, bg="#FFC107", fg="black").pack(pady=5)
tk.Button(ventana, text="Eliminar Categoría", command=eliminar_categoria, bg="#F44336", fg="white").pack(pady=5)

text_salida = tk.Text(ventana, height=10, width=60)
text_salida.pack(pady=10)

ventana.mainloop()