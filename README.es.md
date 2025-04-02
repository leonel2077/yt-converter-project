[English Version](README.md)

# Convertidor de YouTube a MP3

Este proyecto es una aplicación web desarrollada con Django que permite convertir videos de YouTube a formato MP3. Utiliza FFmpeg para el procesamiento de audio y proporciona una interfaz intuitiva para los usuarios.

## Características

- **Conversión de YouTube a MP3**: Convierte videos de YouTube al formato de audio MP3 de manera eficiente.
- **Vista previa del video**: Muestra la miniatura y el título del video antes de la conversión.

## Requisitos previos

Antes de instalar y ejecutar este proyecto, asegúrate de tener instalados los siguientes componentes:

- [Python 3.x](https://www.python.org/downloads/)
- [FFmpeg](https://ffmpeg.org/download.html): Asegúrate de que FFmpeg esté instalado y accesible desde la línea de comandos. Puedes verificarlo ejecutando `ffmpeg -version` en tu terminal.

## Instalación

1. **Clona el repositorio**:

    ```bash
    git clone https://github.com/leonel2077/yt-converter-project.git
    ```

2. **Navega al directorio del proyecto**:

    ```bash
    cd yt-converter-project
    ```

3. **Crea y activa un entorno virtual**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa 'venv\Scripts\activate'
    ```

4. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Configura las variables de entorno**:

    Crea un archivo `.env` en el directorio raíz del proyecto y define las variables necesarias, como las claves de API o configuraciones específicas.

6. **Realiza las migraciones de la base de datos**:

    ```bash
    python manage.py migrate
    ```

7. **Ejecuta el servidor de desarrollo**:

    ```bash
    python manage.py runserver
    ```

    La aplicación estará disponible en `http://127.0.0.1:8000/`.

## Uso

1. **Ingresa la URL del video de YouTube**: En la página principal, introduce el enlace del video que deseas convertir.

2. **Vista previa**: La aplicación mostrará la miniatura y el título del video para confirmación.

3. **Inicia la conversión**: Haz clic en el botón "Convertir" para comenzar el proceso. 

4. **Descarga el MP3**: Una vez completada la conversión, podrás descargar el archivo MP3 resultante.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
