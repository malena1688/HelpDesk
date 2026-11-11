
# HelpDesk - Gestión de Incidencias Técnicas

## 1. Descripción
Aplicación web desarrollada con Python y Django para gestionar incidencias técnicas de una empresa.

## 2. Tecnologías utilizadas
- Python 3.9
- Django 4.2
- SQLite
- HTML
- Bootstrap 5
- Git y GitHub

## 3. Instalación

Clonar el repositorio:

    git clone https://github.com/malena1688/HelpDesk.git

Entrar en la carpeta:

    cd HelpDesk

Crear entorno virtual:

    python3 -m venv venv

Activar entorno virtual:

    source venv/bin/activate

Instalar dependencias:

    pip install -r requirements.txt

Aplicar migraciones:

    python3 manage.py migrate

Crear superusuario:

    python3 manage.py createsuperuser

Iniciar servidor:

    python3 manage.py runserver

## 4. Arquitectura del proyecto

- UF2404: Programación orientada a objetos mediante core_modelos.py.
- UF2405: Desarrollo web con Django, modelos, ORM, vistas, formularios y plantillas.
- UF2406: Control de versiones Git, documentación y pruebas.

## 5. Funcionalidades
- Registro de técnicos.
- Registro de incidencias.
- Asignación de técnicos.
- Gestión de estados.
- Gestión de prioridades.
- Consulta de incidencias.
- Panel de administración.
