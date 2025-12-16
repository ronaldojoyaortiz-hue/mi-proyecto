#=======================================================================
# ARCHIVO: crud_precios_botones.py
# OBJETIVO: CRUD con botones (TKINTER + MYSQL) para tabla precios
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


def crear_precio():
    id_categoria = entry_id_categoria.get()
    id_producto = entry_id_producto.get()
    precio = entry_precio.get()
    moneda = entry_moneda.get()
    tipo_precio = entry_tipo_precio.get()
    fecha_inicio = entry_fecha_inicio.get()
    fecha_fin = entry_fecha_fin.get()
    estado = entry_estado.get()

    cursor = conexion.cursor()
    sql = """
        INSERT INTO precios (id_categoria, id_producto, precio, moneda, tipo_precio, fecha_inicio, fecha_fin, estado)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
    """
    valores = (id_categoria, id_producto, precio, moneda, tipo_precio, fecha_inicio, fecha_fin, estado)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Precio creado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))



def consultar_precios():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM precios;")

    text_salida.delete("1.0", tk.END)

    text_salida.insert(tk.END, "CAMPOS:\n")
    for c in cursor.column_names:
        text_salida.insert(tk.END, f"{c}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")
    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")



def actualizar_precio():
    id_precio = entry_id_precio.get()
    nuevo_precio = entry_precio.get()
    nueva_moneda = entry_moneda.get()
    nuevo_tipo = entry_tipo_precio.get()
    nueva_fecha_inicio = entry_fecha_inicio.get()
    nueva_fecha_fin = entry_fecha_fin.get()
    nuevo_estado = entry_estado.get()

    cursor = conexion.cursor()
    sql = """
        UPDATE precios 
        SET precio=%s, moneda=%s, tipo_precio=%s, fecha_inicio=%s, fecha_fin=%s, estado=%s
        WHERE id_precio=%s;
    """
    valores = (nuevo_precio, nueva_moneda, nuevo_tipo, nueva_fecha_inicio, nueva_fecha_fin, nuevo_estado, id_precio)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Precio actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))



def eliminar_precio():
    id_precio = entry_id_precio.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM precios WHERE id_precio = %s;"
    try:
        cursor.execute(sql, (id_precio,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Precio eliminado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))



ventana = tk.Tk()
ventana.title("CRUD Precios")
ventana.geometry("700x600")


tk.Label(ventana, text="ID Precio ").pack()
entry_id_precio = tk.Entry(ventana)
entry_id_precio.pack()

tk.Label(ventana, text="ID Categoría").pack()
entry_id_categoria = tk.Entry(ventana)
entry_id_categoria.pack()

tk.Label(ventana, text="ID Producto").pack()
entry_id_producto = tk.Entry(ventana)
entry_id_producto.pack()

tk.Label(ventana, text="Precio").pack()
entry_precio = tk.Entry(ventana)
entry_precio.pack()

tk.Label(ventana, text="Moneda").pack()
entry_moneda = tk.Entry(ventana)
entry_moneda.pack()

tk.Label(ventana, text="Tipo Precio (Minorista/Mayorista)").pack()
entry_tipo_precio = tk.Entry(ventana)
entry_tipo_precio.pack()

tk.Label(ventana, text="Fecha Inicio ").pack()
entry_fecha_inicio = tk.Entry(ventana)
entry_fecha_inicio.pack()

tk.Label(ventana, text="Fecha Fin").pack()
entry_fecha_fin = tk.Entry(ventana)
entry_fecha_fin.pack()

tk.Label(ventana, text="Estado ").pack()
entry_estado = tk.Entry(ventana)
entry_estado.pack()


tk.Button(ventana, text="Crear Precio", command=crear_precio, bg="#CBEC0B", fg="black").pack(pady=5)
tk.Button(ventana, text="Consultar Precios", command=consultar_precios, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar Precio", command=actualizar_precio, bg="#FFC107", fg="black").pack(pady=5)
tk.Button(ventana, text="Eliminar Precio", command=eliminar_precio, bg="#F44336", fg="white").pack(pady=5)


text_salida = tk.Text(ventana, height=15, width=80)
text_salida.pack(pady=10)

ventana.mainloop()