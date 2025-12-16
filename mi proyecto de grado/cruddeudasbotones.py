#=======================================================================
# ARCHIVO: crud_deudas_botones.py
# OBJETIVO: CRUD con botones (TKINTER + MYSQL) para tabla deudas
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

#=======================================================================
# 2. FUNCIONES CRUD
# =======================================================================

# CREATE
def crear_deuda():
    id_proveedor = entry_id_proveedor.get()
    monto = entry_monto.get()
    fecha_emision = entry_fecha_emision.get()
    fecha_vencimiento = entry_fecha_vencimiento.get()
    estado = entry_estado.get()
    descripcion = entry_descripcion.get()
    metodo_pago = entry_metodo_pago.get()
    fecha_pago = entry_fecha_pago.get()
    observaciones = entry_observaciones.get("1.0", tk.END)

    cursor = conexion.cursor()
    sql = """
        INSERT INTO deudas (id_proveedor, monto, fecha_emision, fecha_vencimiento, estado, descripcion, metodo_pago, fecha_pago, observaciones)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);
    """
    valores = (id_proveedor, monto, fecha_emision, fecha_vencimiento, estado, descripcion, metodo_pago, fecha_pago, observaciones)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Deuda creada correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# READ
def consultar_deudas():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM deudas;")

    text_salida.delete("1.0", tk.END)

    text_salida.insert(tk.END, "CAMPOS:\n")
    for c in cursor.column_names:
        text_salida.insert(tk.END, f"{c}\n")

    text_salida.insert(tk.END, "\nREGISTROS:\n")
    for fila in cursor.fetchall():
        text_salida.insert(tk.END, f"{fila}\n")


# UPDATE
def actualizar_deuda():
    id_deuda = entry_id_deuda.get()
    nuevo_estado = entry_estado.get()
    nuevo_metodo = entry_metodo_pago.get()
    nueva_fecha_pago = entry_fecha_pago.get()
    nuevas_obs = entry_observaciones.get("1.0", tk.END)

    cursor = conexion.cursor()
    sql = """
        UPDATE deudas 
        SET estado=%s, metodo_pago=%s, fecha_pago=%s, observaciones=%s
        WHERE id_deuda=%s;
    """
    valores = (nuevo_estado, nuevo_metodo, nueva_fecha_pago, nuevas_obs, id_deuda)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Deuda actualizada correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# DELETE
def eliminar_deuda():
    id_deuda = entry_id_deuda.get()

    cursor = conexion.cursor()
    sql = "DELETE FROM deudas WHERE id_deuda = %s;"
    try:
        cursor.execute(sql, (id_deuda,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Deuda eliminada correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))



ventana = tk.Tk()
ventana.title("CRUD Deudas")
ventana.geometry("700x600")


tk.Label(ventana, text="ID Deuda (para Update/Delete)").pack()
entry_id_deuda = tk.Entry(ventana)
entry_id_deuda.pack()

tk.Label(ventana, text="ID Proveedor").pack()
entry_id_proveedor = tk.Entry(ventana)
entry_id_proveedor.pack()

tk.Label(ventana, text="Monto").pack()
entry_monto = tk.Entry(ventana)
entry_monto.pack()

tk.Label(ventana, text="Fecha Emisión ").pack()
entry_fecha_emision = tk.Entry(ventana)
entry_fecha_emision.pack()

tk.Label(ventana, text="Fecha Vencimiento ").pack()
entry_fecha_vencimiento = tk.Entry(ventana)
entry_fecha_vencimiento.pack()

tk.Label(ventana, text="Estado (Pendiente/Pagada/Vencida)").pack()
entry_estado = tk.Entry(ventana)
entry_estado.pack()

tk.Label(ventana, text="Descripción").pack()
entry_descripcion = tk.Entry(ventana)
entry_descripcion.pack()

tk.Label(ventana, text="Método Pago (Transferencia/Cheque/Efectivo/Otro)").pack()
entry_metodo_pago = tk.Entry(ventana)
entry_metodo_pago.pack()

tk.Label(ventana, text="Fecha Pago").pack()
entry_fecha_pago = tk.Entry(ventana)
entry_fecha_pago.pack()

tk.Label(ventana, text="Observaciones").pack()
entry_observaciones = tk.Text(ventana, height=4, width=50)
entry_observaciones.pack()


tk.Button(ventana, text="Crear Deuda", command=crear_deuda, bg="#CBEC0B", fg="black").pack(pady=5)
tk.Button(ventana, text="Consultar Deudas", command=consultar_deudas, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(ventana, text="Actualizar Deuda", command=actualizar_deuda, bg="#FFC107", fg="black").pack(pady=5)
tk.Button(ventana, text="Eliminar Deuda", command=eliminar_deuda, bg="#F44336", fg="white").pack(pady=5)


text_salida = tk.Text(ventana, height=15, width=80)
text_salida.pack(pady=10)

ventana.mainloop()