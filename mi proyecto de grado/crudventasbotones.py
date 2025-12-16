#=======================================================================
# ARCHIVO: crud_ventas_botones.py
# OBJETIVO: CRUD con botones (TKINTER + MYSQL) para tabla ventas
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


def crear_venta():
    id_producto = entry_id_producto.get()
    cantidad_vendida = entry_cantidad.get()
    tipo_precio = entry_tipo_precio.get()
    precio_venta = entry_precio.get()
    fecha_venta = entry_fecha.get()
    id_deudor = entry_id_deudor.get()

    cursor = conexion.cursor()
    sql = """
        INSERT INTO ventas (id_producto, cantidad_vendida, tipo_precio, precio_venta, fecha_venta, id_deudor)
        VALUES (%s,%s,%s,%s,%s,%s);
    """
    valores = (id_producto, cantidad_vendida, tipo_precio, precio_venta, fecha_venta, id_deudor)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Venta creada correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))



def consultar_ventas():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM ventas;")

    text_salida.delete("1.0", tk.END)

    text_salida.insert(tk.END, "CAMPOS:\n")
    for c in cursor.column_names:
        text_salida.insert(tk.END, f"{c}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")
    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")



def actualizar_venta():
    id_venta = entry_id_venta.get()
    nueva_cantidad = entry_cantidad.get()
    nuevo_tipo = entry_tipo_precio.get()
    nuevo_precio = entry_precio.get()
    nueva_fecha = entry_fecha.get()
    nuevo_deudor = entry_id_deudor.get()

    cursor = conexion.cursor()
    sql = """
        UPDATE ventas 
        SET cantidad_vendida=%s, tipo_precio=%s, precio_venta=%s, fecha_venta=%s, id_deudor=%s
        WHERE id_venta=%s;
    """
    valores = (nueva_cantidad, nuevo_tipo, nuevo_precio, nueva_fecha, nuevo_deudor, id_venta)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Venta actualizada correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))



def eliminar_venta():
    id_venta = entry_id_venta.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM ventas WHERE id_venta = %s;"
    try:
        cursor.execute(sql, (id_venta,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Venta eliminada correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))



ventana = tk.Tk()
ventana.title("CRUD Ventas")
ventana.geometry("700x600")


tk.Label(ventana, text="ID Venta ").pack()
entry_id_venta = tk.Entry(ventana)
entry_id_venta.pack()

tk.Label(ventana, text="ID Producto").pack()
entry_id_producto = tk.Entry(ventana)
entry_id_producto.pack()

tk.Label(ventana, text="Cantidad Vendida").pack()
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()

tk.Label(ventana, text="Tipo Precio (MAYOR/UNIDAD)").pack()
entry_tipo_precio = tk.Entry(ventana)
entry_tipo_precio.pack()

tk.Label(ventana, text="Precio Venta").pack()
entry_precio = tk.Entry(ventana)
entry_precio.pack()

tk.Label(ventana, text="Fecha Venta").pack()
entry_fecha = tk.Entry(ventana)
entry_fecha.pack()

tk.Label(ventana, text="ID Deudor (opcional)").pack()
entry_id_deudor = tk.Entry(ventana)
entry_id_deudor.pack()


tk.Button(ventana, text="Crear Venta", command=crear_venta, bg="#CBEC0B", fg="black").pack(pady=5)
tk.Button(ventana, text="Consultar Ventas", command=consultar_ventas, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar Venta", command=actualizar_venta, bg="#FFC107", fg="black").pack(pady=5)
tk.Button(ventana, text="Eliminar Venta", command=eliminar_venta, bg="#F44336", fg="white").pack(pady=5)


text_salida = tk.Text(ventana, height=15, width=80)
text_salida.pack(pady=10)

ventana.mainloop()