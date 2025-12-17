# WNS Challenge

¡Hola! Gracias por aplicar a WNS Asociados. A continuación verás un desafío técnico. Te pedimos que lo completes de acuerdo a los lineamientos aquí detallados:

## Lineamientos del Desafío
A la hora de entregar te pedimos que:

- Programes la lógica general de la solución en Python (la capa de UI/presentación puede estar en otro lenguaje como JavaScript).
- Subas todo el código producido a GitHub y nos envíes un link al repositorio.
- Incluyas un archivo README.md o similar detallando las decisiones tomadas y explicando la implementación, sus fortalezas y debilidades.
- Destaques las asunciones hechas a la hora de desarrollar la solución y expliques las limitaciones y condiciones de operación de la misma.
- Te asegures de que la explicación incluya pasos detallados para poder reproducir la solución (instalación de librerías, setup, etc.).
- Incluyas uno o dos párrafos explicando qué cambios harías a tu solución en caso de que se desee escalarla o desplegarla más allá de un entorno local.

Para resolver el desafío podés (aunque no es obligatorio):
- Usar librerías externas (recordá mencionarlas y proveer los pasos necesarios para instalarlas localmente).
- Usar ChatGPT, Google o cualquier otro servicio de búsqueda o IA para pensar y diagramar la solución.
- Empaquetar tu solución con Docker para facilitar que la repliquemos localmente (Recordá incluír los archivos necesarios como el Dockerfile y/o docker-compose.yml en el repo).

Para resolver el desafío NO podés:
- Llamar a servicios externos, más allá de los estipulados en la consigna.
- Utilizar código generado por IA que no seas capaz de comprender y explicar, vamos a preguntarte sobre tu implementación en la entrevista técnica.
- Modificar los archivos de Input que te vamos a dar. Tu solución tiene que funcionar con los archivos tal y cómo te los suministramos (aunque podés programar una capa de normalización previa como preprocesar los datos e ingestarlos en una base de datos y luego utilizar tus datos normalizados, en tal caso, incluí el código de normalización en tu respuesta y los pasos para ejecutarlo). 

## Consigna

El objetivo de este desafío es construir una pequeña aplicación que permita al usuario elegir un plato de los provistos en `inputs/Recetas.md` y una fecha dentro de los 30 días previos y ver el listado de ingredientes, sus cantidades y el costo total del plato en Pesos argentinos y Dólares estadounidenses.

A tal efecto, disponés de 2 archivos más:
- `inputs/verduleria.pdf` que contiene el precio de las verduras.
- `inputs/Carnes y Pescados.xslx` que contiene el precio de Carnes y pescados.

Podés asumir que estos precios NO cambian con el tiempo y son iguales en cualquier momento del mes.

Tanto las verduras como las carnes y pescados se venden de a múltiplos de 250 gramos, es decir, si un plato requiere de 800 gramos de Zapallo, es necesario cotizar la compra de 1 kilo del mismo (dado que 750 gramos sería menos de lo necesario y 1 kilo es el valor siguiente aceptable).

A efectos de obtener la cotización del Dólar estadounidense debés utilizar la siguiente API que te permitiría chequear la cotización de cualquier moneda vs el Dólar para una fecha dada:

`https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@[FECHA]/v1/currencies/usd.json`

La fecha se especifica en el formato YYYY-MM-DD dónde YYYY es el año, MM el mes arrancando con 0 en caso de ser menor a 10 y DD el día arrancando con 0 en caso de ser menor a 10. Es decir, para ver la cotización del Dólar en Pesos argentinos el 20 de Julio de 2025 deberás acceder a:

`https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@2025-07-20/v1/currencies/usd.json`

y observar el valor del mismo en Pesos Argentinos (el código ISO de la moneda es ARS).

La aplicación deberá solicitar el plato a cotizar y la fecha (dentro de los últimos 30 días) y devolver el costo total del mismo tanto en pesos como en dólares.

La capa de presentación/UI de esta aplicación depende de vos: puede ser un CLI, un GUI, una aplicación Web o lo que vos quieras mientras pueda ser corrido localmente. Es importante que la capa de backend/procesamiento de datos sea en Python.

¡Muchos éxitos y esperamos ver tu respuesta!