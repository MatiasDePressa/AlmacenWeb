# AlmacenWeb

AlmacenWeb es una aplicación de escritorio desarrollada en Python utilizando Tkinter y SQLite. Su propósito es gestionar una base de datos de páginas web, permitiendo agregar, visualizar y eliminar registros de manera sencilla.

## Requisitos

- Python 3.x
- Tkinter (incluido en la mayoría de las instalaciones de Python)
- SQLite3 (incluido en la mayoría de las instalaciones de Python)

## Instalación

1. Clona este repositorio o descarga los archivos.

2. Asegúrate de tener Python instalado en tu sistema. Puedes verificarlo ejecutando `python --version` o `python3 --version` en tu terminal.

3. No necesitas instalar dependencias adicionales ya que Tkinter y SQLite3 vienen incluidos con Python.

## Uso

1. Ejecuta el script principal para iniciar la aplicación:

    ```bash
    python AlmacenWeb.py
    ```

2. La aplicación se abrirá con una interfaz gráfica.

3. También puedes utilizar el ejecutable dentro de la carpeta `dist` para iniciar la aplicación directamente sin necesidad de Python:

    - Navega a la carpeta `dist`.
    - Ejecuta el archivo `AlmacenWeb.exe`.

### Funcionalidades

- **Agregar Página:** Ingresa el nombre, descripción y URL de la página que deseas almacenar y haz clic en "Almacenar".
- **Mostrar URL Seleccionada:** Haz doble clic en una fila del Treeview para mostrar la URL en el campo de texto correspondiente.
- **Eliminar Registro:** Selecciona una fila en el Treeview y haz clic en "Eliminar" para borrar el registro de la base de datos.

## Crear un Acceso Directo

Para mayor comodidad, puedes crear un acceso directo al ejecutable de la aplicación:

1. Navega a la carpeta `dist`.
2. Haz clic derecho en el archivo `AlmacenWeb.exe`.
3. Selecciona "Crear acceso directo".
4. Mueve el acceso directo a una ubicación de tu preferencia, como el escritorio.

## Estructura del Proyecto

- `AlmacenWeb.py`: Archivo principal que contiene la lógica de la aplicación.
- `AlmacenWeb.db`: Archivo de base de datos SQLite3 donde se almacenan los registros.
- `dist/`: Carpeta que contiene el ejecutable del proyecto.

## Descripción del Código

### Conexión a la Base de Datos

El proyecto se conecta a una base de datos SQLite3 llamada `AlmacenWeb.db`. Si la base de datos no existe, se crea automáticamente. Dentro de la base de datos, se maneja una única tabla llamada `paginas` con las siguientes columnas:

- `id`: Identificador único de cada registro (tipo entero y clave primaria).
- `nombre`: Nombre de la página (tipo texto, no nulo).
- `descripcion`: Descripción de la página (tipo texto).
- `url`: URL de la página (tipo texto).

### Funciones Principales

- **`insertar_datos()`**: Inserta un nuevo registro en la tabla `paginas` con los valores proporcionados en los campos de entrada (nombre, descripción y URL). Luego, limpia los campos de entrada y actualiza el grid.
- **`limpiar_campos()`**: Limpia los campos de entrada para nombre, descripción y URL.
- **`actualizar_grid()`**: Obtiene todos los registros de la tabla `paginas` y los muestra en el Treeview. Primero limpia el Treeview y luego inserta los nuevos datos.
- **`mostrar_url(event)`**: Muestra la URL del registro seleccionado en el Treeview en el campo de texto correspondiente para URL seleccionada.
- **`eliminar_dato()`**: Elimina el registro seleccionado en el Treeview de la tabla `paginas`.

### Eventos

- **Doble Clic en Treeview**: Al hacer doble clic en una fila del Treeview, se ejecuta la función `mostrar_url` para mostrar la URL seleccionada en el campo de texto.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork de este repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios al repositorio (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.
