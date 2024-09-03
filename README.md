# Pipeline de Integración Continua

Este proyecto utiliza GitHub Actions para asegurarse de que todo funcione bien cada vez que se hagan cambios. Aquí te explicamos cómo funciona y cómo configurarlo.


## ¿Qué Hace Este Pipeline?

Este pipeline automatiza algunas tareas importantes cuando se hacen cambios en el proyecto:

1. **Ejecuta Pruebas**: Se asegura de que las pruebas que escribimos para nuestro código se ejecuten y pasen correctamente.
2. **Instala Dependencias**: Instala todas las herramientas y librerías que nuestro proyecto necesita para funcionar.

## Cómo Configurarlo

1. **Configura GitHub Actions**: GitHub Actions debería estar habilitado en tu repositorio. Esto es lo que se encarga de ejecutar nuestro pipeline automáticamente.
2. **Prepara el Archivo de Dependencias**: Asegúrate de que el archivo `requirements.txt` esté en la raíz del proyecto. Este archivo enumera todas las librerías que nuestro proyecto necesita.

## Cómo Funciona

Aquí está lo que hace cada parte del pipeline:

- **Cuando se hace un `push` o un `pull request` a la rama `uat`**: GitHub Actions activará el pipeline para verificar que todo esté en orden.
- **Paso 1: Checkout del Código**: Obtiene la última versión del código desde tu repositorio.
- **Paso 2: Configura Python**: Usa la versión 3.8 de Python para ejecutar las pruebas.
- **Paso 3: Instala Dependencias**: Actualiza `pip` e instala las librerías listadas en `requirements.txt`.
- **Paso 4: Ejecuta las Pruebas**: Corre todas las pruebas que tienes en la carpeta `tests` para asegurarse de que todo funcione correctamente.