#=======================================================================
# ARCHIVO: crud_proveedores_botones.py
# OBJETIVO: CRUD con botones (TKINTER + MYSQL) para tabla proveedores
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


def crear_proveedor():
    nombre = entry_nombre.get()
    razon_social = entry_razon.get()
    nit = entry_nit.get()
    direccion = entry_direccion.get()
    ciudad = entry_ciudad.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()
    tipo_producto = entry_tipo.get()
    estado = entry_estado.get()

    cursor = conexion.cursor()
    sql = """
        INSERT INTO proveedores (nombre, razon_social, nit, direccion, ciudad, telefono, correo, tipo_producto, estado)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);
    """
    valores = (nombre, razon_social, nit, direccion, ciudad, telefono, correo, tipo_producto, estado)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Proveedor creado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))



def consultar_proveedores():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM proveedores;")

    text_salida.delete("1.0", tk.END)

    text_salida.insert(tk.END, "CAMPOS:\n")
    for c in cursor.column_names:
        text_salida.insert(tk.END, f"{c}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")
    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")



def actualizar_proveedor():
    id_proveedor = entry_id_proveedor.get()
    nuevo_nombre = entry_nombre.get()
    nueva_razon = entry_razon.get()
    nuevo_nit = entry_nit.get()
    nueva_direccion = entry_direccion.get()
    nueva_ciudad = entry_ciudad.get()
    nuevo_telefono = entry_telefono.get()
    nuevo_correo = entry_correo.get()
    nuevo_tipo = entry_tipo.get()
    nuevo_estado = entry_estado.get()

    cursor = conexion.cursor()
    sql = """
        UPDATE proveedores 
        SET nombre=%s, razon_social=%s, nit=%s, direccion=%s, ciudad=%s, telefono=%s, correo=%s, tipo_producto=%s, estado=%s
        WHERE id_proveedor=%s;
    """
    valores = (nuevo_nombre, nueva_razon, nuevo_nit, nueva_direccion, nueva_ciudad, nuevo_telefono, nuevo_correo, nuevo_tipo, nuevo_estado, id_proveedor)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Proveedor actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))



def eliminar_proveedor():
    id_proveedor = entry_id_proveedor.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM proveedores WHERE id_proveedor = %s;"
    try:
        cursor.execute(sql, (id_proveedor,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Proveedor eliminado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))


ventana = tk.Tk()
ventana.title("CRUD Proveedores")
ventana.geometry("700x600")


tk.Label(ventana, text="ID Proveedor").pack()
entry_id_proveedor = tk.Entry(ventana)
entry_id_proveedor.pack()

tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()


tk.Label(ventana, text="NIT").pack()
entry_nit = tk.Entry(ventana)
entry_nit.pack()

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

tk.Label(ventana, text="Tipo de Producto").pack()
entry_tipo = tk.Entry(ventana)
entry_tipo.pack()

tk.Label(ventana, text="Estado").pack()
entry_estado = tk.Entry(ventana)
entry_estado.pack()


tk.Button(ventana, text="Crear Proveedor", command=crear_proveedor, bg="#CBEC0B", fg="black").pack(pady=5)
tk.Button(ventana, text="Consultar Proveedores", command=consultar_proveedores, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar Proveedor", command=actualizar_proveedor, bg="#FFC107", fg="black").pack(pady=5)
tk.Button(ventana, text="Eliminar Proveedor", command=eliminar_proveedor, bg="#F44336", fg="white").pack(pady=5)


text_salida = tk.Text(ventana, height=15, width=80)
text_salida.pack(pady=10)

ventana.mainloop()