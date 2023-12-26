**Developer Guide - ToolSculpt**

# Indice

1. [Introducción](#introducción)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Instalación del Entorno de Desarrollo](#instalación-del-entorno-de-desarrollo)
4. [Contribución al Código](#contribución-al-código)
5. [Pruebas y Validación](#pruebas-y-validación)
6. [Integración Continua](#integración-continua)
7. [Despliegue](#despliegue)
8. [Documentación Adicional](#documentación-adicional)
9. [Contacto y Soporte](#contacto-y-soporte)
10. [Licencia](#licencia)

## Introducción

Bienvenido al desarrollo de *ToolSculpt*. Esta guía proporciona información esencial para que los desarrolladores contribuyan efectivamente al proyecto.

## Estructura del Proyecto

La estructura del proyecto está diseñada para ser modular y escalable. Asegúrate de entender la organización de los directorios antes de empezar.

Consulta el [README.md](../README.md) para obtener una visión general del proyecto y su funcionalidad.

## Instalación del Entorno de Desarrollo

Antes de comenzar, configura un entorno virtual e instala las dependencias necesarias. Utiliza el archivo `requirements.txt` para facilitar este proceso.

```bash
pip install -r requirements.txt
```

Asegúrate de que estás utilizando Python 3.x.

## Contribución al Código

1. **Branches:**
   - Crea una nueva branch para cada nueva característica o corrección de errores.
   - Utiliza nombres descriptivos para las branches.

```bash
git checkout -b feature/nueva-caracteristica
```

2. **Commits:**
   - Mantén commits pequeños y descriptivos.
   - Sigue las convenciones de mensajes de commit.

```bash
git commit -m "Añade nueva característica XYZ"
```

3. **Pull Requests:**
   - Abre un Pull Request para revisión antes de fusionar con la branch principal.
   - Describe detalladamente los cambios realizados.

## Pruebas y Validación

- Ejecuta las pruebas existentes antes de enviar un Pull Request.
- Añade nuevas pruebas para cualquier característica nueva.
- Asegúrate de que todas las pruebas pasan antes de fusionar.

```bash
pytest
```

## Integración Continua

*ToolSculpt* utiliza integración continua para validar cada Pull Request automáticamente. Asegúrate de que todas las pruebas pasen antes de solicitar la revisión.

## Despliegue

Las versiones se manejan a través de tags. Asegúrate de seguir una convención semántica de versionado al incrementar las versiones.

```bash
git tag -a v1.0.0 -m "Versión 1.0.0"
git push origin v1.0.0
```

## Documentación Adicional

Consulta la documentación en el directorio [docs/](docs/) para obtener más detalles sobre el uso y la arquitectura del sistema.

## Contacto y Soporte

Para preguntas, problemas o sugerencias, por favor contacta al equipo de desarrollo:

- [Correo Electrónico del Equipo](mailto:devteam@toolsculpt.com)
- [Foro de Desarrolladores](https://forums.toolsculpt.com)

## Licencia

Este proyecto está bajo la [Licencia Creative Commons Attribution 4.0 International](../LICENSE). Asegúrate de respetar los términos de la licencia al contribuir al proyecto.

¡Gracias por contribuir al desarrollo de *ToolSculpt*!
