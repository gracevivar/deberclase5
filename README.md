---
Requisitos Previos e Instalación
1. Crear el entorno virtual
Crea un entorno virtual para aislar las dependencias del proyecto:
```bash
python3 -m venv venv
```
2. Activar el entorno virtual
Activa el entorno según tu sistema operativo:
```bash
  source venv/bin/activate
  ```

3. Instalar las dependencias
Instala los paquetes requeridos ejecutando:
```bash
pip install -r requirements.txt
```
---
Ejecución de la Aplicación
Inicia el servidor en modo de desarrollo con el siguiente comando:
```bash
fastapi dev
```
Una vez en ejecución, podrás acceder a la documentación interactiva de la API (Swagger UI) para realizar tus pruebas en la siguiente dirección: http://127.0.0.1:8000/docs