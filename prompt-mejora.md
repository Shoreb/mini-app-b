## 1. Rol
Actúa como un desarrollador backend y frontend con experiencia en FastAPI, Jinja2, HTML, CSS, JavaScript y pruebas automatizadas con pytest. Tu responsabilidad es implementar la mejora solicitada respetando la arquitectura y el funcionamiento actual del proyecto.

## 2. Objetivo
Implementar un indicador de fuerza de contraseña en la mini-aplicación web Generador de contraseñas.

La mejora debe cumplir las siguientes condiciones:

**Backend:**

- Modificar la respuesta de `GET /api/contrasena` para incluir un nuevo campo llamado `fuerza`.
- El campo `fuerza` debe calcularse de acuerdo con estas reglas:
  - **Fuerte:** cuando la contraseña tenga una longitud de 16 caracteres o más e incluya números y símbolos.
  - **Débil:** cuando la contraseña tenga menos de 12 caracteres o no incluya números ni símbolos (es decir, que no incluya ninguno de los dos).
  - **Media:** en todos los demás casos.
- La respuesta JSON debe conservar los campos originales `contrasena` y `longitud`, agregando `fuerza` sin cambiar sus nombres ni eliminar información.

**Frontend:**

- La página principal debe mostrar la fuerza de la contraseña generada.
- El indicador debe actualizarse cada vez que se genere una nueva contraseña.
- Mostrar el indicador con los siguientes colores:
  - Rojo para fuerza débil.
  - Amarillo para fuerza media.
  - Verde para fuerza fuerte.
- El indicador debe ser fácil de identificar y comprender para el usuario.

## 3. Contexto
La aplicación existente se encuentra en la carpeta `mini-app-b`.

Antes de realizar cualquier cambio:

- Lee el archivo `AGENTS.md`.
- Revisa la estructura y el funcionamiento actual del proyecto.
- Examina `app/main.py`, `app/servicios.py` y los archivos de la interfaz.
- Revisa `tests/test_aceptacion.py` para conocer el contrato original de la API.

La mejora debe integrarse sobre la aplicación existente, conservando sus funcionalidades y respetando los requisitos originales.

## 4. Restricciones
- Utiliza únicamente las dependencias declaradas en `requirements.txt`.
- Mantén las rutas de FastAPI en `app/main.py`.
- Mantén la lógica de generación y cálculo de fuerza en `app/servicios.py`, sin importar FastAPI en este archivo.
- No utilices bases de datos ni almacenamiento externo.
- No modifiques, elimines ni reemplaces `tests/test_aceptacion.py`.
- Crea una nueva prueba en `tests/test_mejora.py` para comprobar la funcionalidad solicitada.
- No elimines ni alteres las funcionalidades originales del generador de contraseñas.
- La interfaz debe utilizar HTML, CSS y JavaScript sin librerías externas.
- No realices cambios innecesarios en archivos que no estén relacionados con la mejora.

## 5. Formato de salida
Antes de escribir o modificar cualquier código, debes presentar un plan de implementación.

El plan debe incluir:

1. Una explicación de cómo implementarás el cálculo de la fuerza en el backend.
2. Cómo mostrarás y actualizarás el indicador de fuerza en la página principal.
3. Los archivos que crearás o modificarás, indicando sus rutas absolutas y completas.
4. La función específica que cumplirá cada archivo.
5. Las pruebas que ejecutarás para comprobar la mejora.

Después de presentar el plan, detente y espera mi aprobación explícita. No debes crear, modificar ni eliminar archivos antes de recibirla.

Una vez aprobada la implementación, realiza los cambios y, al finalizar, presenta un resumen de una línea por cada archivo creado o modificado, explicando su función.

## 6. Ejemplo
Una petición a la API:

`GET /api/contrasena?longitud=16&numeros=true&simbolos=true`

Debe devolver una respuesta con esta estructura:

`{"contrasena": "q7G!mR2-xW9a#Lp4", "longitud": 16, "fuerza": "fuerte"}`

En este caso, la contraseña tiene 16 caracteres e incluye números y símbolos, por lo tanto, su fuerza es fuerte.

Otro ejemplo:

`GET /api/contrasena?longitud=10&numeros=false&simbolos=false`

Debe devolver una respuesta donde el campo `fuerza` tenga el valor `débil`, porque la longitud es menor de 12 caracteres.

## 7. Criterio de éxito
La mejora se considerará terminada cuando se cumplan todas las condiciones siguientes:

- La API devuelve el nuevo campo `fuerza` junto con los campos originales `contrasena` y `longitud`.
- El cálculo de fuerza respeta exactamente las tres condiciones establecidas en el anexo.
- La página principal muestra el indicador con el color correspondiente: rojo, amarillo o verde.
- El indicador se actualiza correctamente al generar una nueva contraseña.
- Existe una nueva prueba en `tests/test_mejora.py` que comprueba los tres niveles de fuerza y sus condiciones.
- El archivo `tests/test_aceptacion.py` permanece sin modificaciones.
- Las funcionalidades originales de la aplicación continúan funcionando.

Para verificar la implementación, ejecuta:

`python -m pytest -v`

También ejecuta:

`ruff check .`

Ambos comandos deben finalizar sin errores.

Tienes un máximo de 3 intentos para corregir los errores encontrados. Si después del tercer intento las pruebas o Ruff siguen fallando, debes detenerte, informar los errores pendientes y explicar qué archivos necesitan atención. No debes continuar modificando el proyecto indefinidamente.