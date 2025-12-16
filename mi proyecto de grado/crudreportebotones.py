#=======================================================================
# ARCHIVO: crud_reportes_botones.py
# OBJETIVO: CRUD con botones (TKINTER + MYSQL) para tabla reportes
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


def crear_reporte():
    id_producto = entry_id_producto.get()
    tipo = entry_tipo.get()
    fecha_generacion = entry_fecha.get()
    ruta_archivo = entry_ruta.get()

    cursor = conexion.cursor()
    sql = """
        INSERT INTO reportes (id_producto, tipo, fecha_generacion, ruta_archivo)
        VALUES (%s,%s,%s,%s);
    """
    valores = (id_producto, tipo, fecha_generacion, ruta_archivo)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Reporte creado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))



def consultar_reportes():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM reportes;")

    text_salida.delete("1.0", tk.END)

    text_salida.insert(tk.END, "CAMPOS:\n")
    for c in cursor.column_names:
        text_salida.insert(tk.END, f"{c}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")
    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")



def actualizar_reporte():
    id_reporte = entry_id_reporte.get()
    nuevo_tipo = entry_tipo.get()
    nueva_fecha = entry_fecha.get()
    nueva_ruta = entry_ruta.get()

    cursor = conexion.cursor()
    sql = """
        UPDATE reportes 
        SET tipo=%s, fecha_generacion=%s, ruta_archivo=%s
        WHERE id_reporte=%s;
    """
    valores = (nuevo_tipo, nueva_fecha, nueva_ruta, id_reporte)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Reporte actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def eliminar_reporte():
    id_reporte = entry_id_reporte.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM reportes WHERE id_reporte = %s;"
    try:
        cursor.execute(sql, (id_reporte,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Reporte eliminado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))


ventana = tk.Tk()
ventana.title("CRUD Reportes")
ventana.geometry("700x600")

tk.Label(ventana, text="ID Reporte").pack()
entry_id_reporte = tk.Entry(ventana)
entry_id_reporte.pack()

tk.Label(ventana, text="ID Producto").pack()
entry_id_producto = tk.Entry(ventana)
entry_id_producto.pack()

tk.Label(ventana, text="Tipo ").pack()
entry_tipo = tk.Entry(ventana)
entry_tipo.pack()

tk.Label(ventana, text="Fecha Generación)").pack()
entry_fecha = tk.Entry(ventana)
entry_fecha.pack()

tk.Label(ventana, text="Ruta Archivo").pack()
entry_ruta = tk.Entry(ventana)
entry_ruta.pack()


tk.Button(ventana, text="Crear Reporte", command=crear_reporte, bg="#CBEC0B", fg="black").pack(pady=5)
tk.Button(ventana, text="Consultar Reportes", command=consultar_reportes, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar Reporte", command=actualizar_reporte, bg="#FFC107", fg="black").pack(pady=5)
tk.Button(ventana, text="Eliminar Reporte", command=eliminar_reporte, bg="#F44336", fg="white").pack(pady=5)


text_salida = tk.Text(ventana, height=15, width=80)
text_salida.pack(pady=10)

ventana.mainloop()