import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('AlmacenWeb.db')
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS paginas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    url TEXT
)
''')

# Función para insertar datos en la base de datos
def insertar_datos():
    nombre = entry_nombre.get()
    descripcion = entry_descripcion.get()
    url = entry_url.get()
    cursor.execute('''
    INSERT INTO paginas (nombre, descripcion, url) VALUES (?, ?, ?)
    ''', (nombre, descripcion, url))
    conn.commit()
    limpiar_campos()
    actualizar_grid()

# Función para limpiar los campos de entrada
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)
    entry_url.delete(0, tk.END)

# Función para actualizar el grid con los datos de la base de datos
def actualizar_grid():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute('SELECT * FROM paginas')
    rows = cursor.fetchall()
    for row in rows:
        tree.insert('', tk.END, values=row)

# Función para mostrar una URL seleccionada
def mostrar_url(event):
    selected_item = tree.selection()[0]
    url = tree.item(selected_item, 'values')[3]
    entry_seleccionada.delete(0, tk.END)
    entry_seleccionada.insert(0, url)

# Función para eliminar un dato seleccionado en el grid
def eliminar_dato():
    selected_item = tree.selection()[0]
    id_dato = tree.item(selected_item, 'values')[0]
    cursor.execute('DELETE FROM paginas WHERE id = ?', (id_dato,))
    conn.commit()
    actualizar_grid()

# Crear la ventana principal
root = tk.Tk()
root.title("AlmacenWeb")

# Estilos
style = ttk.Style()

# Tema oscuro
root.configure(bg='#2e2e2e')  # Fondo de la ventana principal

# Configuración del estilo de los botones
style.configure('TButton', font=('Palatino', 12), foreground='black', background='#3e3e3e', borderwidth=2, relief='solid')
style.map('TButton', background=[('active', '#3e3e3e')], foreground=[('active', 'black')], bordercolor=[('active', '#8B0000')])

# Configuración del estilo de las etiquetas
style.configure('TLabel', font=('Palatino', 12), foreground='white', background='#2e2e2e')

# Configuración del estilo de las entradas
style.configure('TEntry', font=('Palatino', 12), foreground='black', fieldbackground='#3e3e3e', borderwidth=2, relief='solid')
style.map('TEntry', fieldbackground=[('active', '#4e4e4e')], foreground=[('active', 'white')], bordercolor=[('active', '#8B0000')])

# Configuración del estilo del Treeview
style.configure('Treeview', background='#3e3e3e', foreground='white', fieldbackground='#3e3e3e', borderwidth=2, relief='solid')
style.configure('Treeview.Heading', background='#2e2e2e', foreground='black', borderwidth=2, relief='solid')
style.map('Treeview', background=[('selected', '#4e4e4e')], foreground=[('selected', 'white')], bordercolor=[('selected', '#8B0000')])

# Aplicar el estilo a todos los widgets hijos de la ventana principal
for widget in root.winfo_children():
    widget.configure(background='#2e2e2e')

# Aplicar estilos adicionales para asegurar que todo se vea bien en oscuro
for child in root.winfo_children():
    if isinstance(child, ttk.Entry):
        child.configure(foreground='white', background='#3e3e3e')
    elif isinstance(child, ttk.Button):
        child.configure(foreground='white', background='#3e3e3e')
    elif isinstance(child, ttk.Treeview):
        child.tag_configure('odd', background='#3e3e3e')
        child.tag_configure('even', background='#2e2e2e')



# Crear y colocar los widgets
ttk.Label(root, text="Nombre:").grid(column=0, row=0, padx=10, pady=5)
entry_nombre = ttk.Entry(root)
entry_nombre.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(root, text="Descripción:").grid(column=0, row=1, padx=10, pady=5)
entry_descripcion = ttk.Entry(root)
entry_descripcion.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(root, text="URL:").grid(column=0, row=2, padx=10, pady=5)
entry_url = ttk.Entry(root)
entry_url.grid(column=1, row=2, padx=10, pady=5)

boton_almacenar = ttk.Button(root, text="Almacenar", command=insertar_datos)
boton_almacenar.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

ttk.Label(root, text="URL Seleccionada:").grid(column=0, row=4, padx=10, pady=5)
entry_seleccionada = ttk.Entry(root, width=100)  # Ajusta el ancho según necesites
entry_seleccionada.grid(column=1, row=4, padx=10, pady=5)

# Crear el Treeview para mostrar los datos
tree = ttk.Treeview(root, columns=("id", "nombre", "descripcion", "url"), show='headings')
tree.heading("id", text="ID")
tree.heading("nombre", text="Nombre")
tree.heading("descripcion", text="Descripción")
tree.heading("url", text="URL")
tree.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

# Botón para eliminar el dato seleccionado
boton_eliminar = ttk.Button(root, text="Eliminar", command=eliminar_dato)
boton_eliminar.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

# Conectar evento de selección de fila
tree.bind("<Double-1>", mostrar_url)

# Llamar a la función para cargar los datos en el grid
actualizar_grid()

# Ejecutar la aplicación
root.mainloop()

# Cerrar la conexión a la base de datos al finalizar la aplicación
conn.close()
