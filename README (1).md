# Proyecto Sprint 7 12vo Grupo Arturo Zarazua
#  Introducción a la automatización de pruebas

## Descripción del proyecto
El proyecto tiene la intención de introducirnos en los principios básicos de la programación de pruebas automatizadas en python

## Instalación
Para instalar y configurar el proyecto, sigue estos pasos:

1. Instala Python 3.12 desde [python.org](https://www.python.org/downloads/release/python-3120/).
2. Instala los recursos necesarios:
    ```bash
    pip install pytest - requests
    ```
    
## Uso
El proyecto incluye varias funciones y pruebas. Aquí hay un resumen de las funciones principales:

- `post_new_client`: Función para crear un nuevo cliente.
- `post_new_client_kit`: Función para crear un nuevo kit de cliente.
- `authtoken_new_kit`: Función para autenticar un nuevo kit.
- `positive_assert`: Función para realizar aserciones positivas.
- `negative_assert_code_400`: Función para realizar aserciones negativas con código de error 400.
- `get_kit_body`: Función que cambia el contenido del cuerpo de la solicitud.
- 
Se tienen 9 pruebas en este proyecto, se deben de correr todas estas para encontrar las que cuentan con un error

Si se desea contribuir en el proyecto, favor de  revisar la documentación fuente en la página de proyecto y con la documentación en el [apiDoc].