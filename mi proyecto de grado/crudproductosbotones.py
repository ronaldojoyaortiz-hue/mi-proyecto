#=======================================================================
# ARCHIVO: crud_productos_botones.py
# OBJETIVO: CRUD con botones (TKINTER + MYSQL) para tabla productos
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


def crear_producto():
    nombre = entry_nombre.get()
    descripcion = entry_descripcion.get()
    precio = entry_precio.get()
    cantidad = entry_cantidad.get()
    unidad = entry_unidad.get()
    estado = entry_estado.get()
    id_proveedor = entry_id_proveedor.get()
    id_categoria = entry_id_categoria.get()

    cursor = conexion.cursor()
    sql = """
        INSERT INTO productos (nombre, descripcion, precio, cantidad_disponible, unidad_medida, estado, id_proveedor, id_categoria)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
    """
    valores = (nombre, descripcion, precio, cantidad, unidad, estado, id_proveedor, id_categoria)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Producto creado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))



def consultar_productos():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos;")

    text_salida.delete("1.0", tk.END)

    text_salida.insert(tk.END, "CAMPOS:\n")
    for c in cursor.column_names:
        text_salida.insert(tk.END, f"{c}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")
    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")



def actualizar_producto():
    id_producto = entry_id_producto.get()
    nuevo_nombre = entry_nombre.get()
    nueva_descripcion = entry_descripcion.get()
    nuevo_precio = entry_precio.get()
    nueva_cantidad = entry_cantidad.get()
    nueva_unidad = entry_unidad.get()
    nuevo_estado = entry_estado.get()
    nuevo_proveedor = entry_id_proveedor.get()
    nueva_categoria = entry_id_categoria.get()

    cursor = conexion.cursor()
    sql = """
        UPDATE productos 
        SET nombre=%s, descripcion=%s, precio=%s, cantidad_disponible=%s, unidad_medida=%s, estado=%s, id_proveedor=%s, id_categoria=%s
        WHERE id_producto=%s;
    """
    valores = (nuevo_nombre, nueva_descripcion, nuevo_precio, nueva_cantidad, nueva_unidad, nuevo_estado, nuevo_proveedor, nueva_categoria, id_producto)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Producto actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))



def eliminar_producto():
    id_producto = entry_id_producto.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM productos WHERE id_producto = %s;"
    try:
        cursor.execute(sql, (id_producto,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Producto eliminado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))


ventana = tk.Tk()
ventana.title("CRUD Productos")
ventana.geometry("700x600")


tk.Label(ventana, text="ID Producto").pack()
entry_id_producto = tk.Entry(ventana)
entry_id_producto.pack()

tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Descripción").pack()
entry_descripcion = tk.Entry(ventana)
entry_descripcion.pack()

tk.Label(ventana, text="Precio").pack()
entry_precio = tk.Entry(ventana)
entry_precio.pack()

tk.Label(ventana, text="Cantidad Disponible").pack()
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()

tk.Label(ventana, text="Unidad de Medida").pack()
entry_unidad = tk.Entry(ventana)
entry_unidad.pack()

tk.Label(ventana, text="Estado (Disponible/Agotado)").pack()
entry_estado = tk.Entry(ventana)
entry_estado.pack()

tk.Label(ventana, text="ID Proveedor").pack()
entry_id_proveedor = tk.Entry(ventana)
entry_id_proveedor.pack()

tk.Label(ventana, text="ID Categoría").pack()
entry_id_categoria = tk.Entry(ventana)
entry_id_categoria.pack()


tk.Button(ventana, text="Crear Producto", command=crear_producto, bg="#CBEC0B", fg="black").pack(pady=5)
tk.Button(ventana, text="Consultar Productos", command=consultar_productos, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar Producto", command=actualizar_producto, bg="#FFC107", fg="black").pack(pady=5)
tk.Button(ventana, text="Eliminar Producto", command=eliminar_producto, bg="#F44336", fg="white").pack(pady=5)


text_salida = tk.Text(ventana, height=15, width=80)
text_salida.pack(pady=10)

ventana.mainloop()