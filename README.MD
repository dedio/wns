Prueba técnica WNS
==================

Ejecución del entorno virtual
-----------------------------
Abrir una consola, dirigirse al directorio del proyecto y ejecutar:
+ python3 -m venv venv
+ source venv/bin/activate
+ pip install -r requirements.txt

Consideraciones
===============
El domingo pasado comencé a ver el proyecto.  Asumí que se trataba un módulo parte de una aplicación principal como la de un supermercado, un restaurante o una casa de comidas.
Consideré entonces que debía ser sencilla y adaptable para poder ser integrada de manera fácil y opté por una API.  Elegí como respaldo un fichero json ya que este tipo de dato es soportado por motores como Postgresql o MySQL.  Esto facilitaría los cambios en desarrollo, las pruebas en QA y consecuentemente el despliegue en producción.
Sin embargo, la consigna de la fecha diferida para la cotización, el fraccionamiento del peso de los ingredientes y el cálculo del precio del plato me generaron dudas y confusión.  Esto derivó en varios re diseños del proyecto.  Finalmente, decidí desarrollar la aplicación como creí que pudiera ser funcional y luego plantear aquí mis consideraciones.
La fecha de cotización para un producto consumible como un plato de comida, debería ser la del momento en que se hace el pedido. De otra forma podría generar confusiones y divergencias sobre el monto final.  Por otro lado, el proceso de cálculo de costos y del precio del producto es independiente al proceso de toma de pedido y despacho.  Fraccionar el peso de cualquier ingrediente en rangos de 250 gramos no sólo tergiversa la preparación del producto en si, sino que también distorsiona los costos. Usualmente se utilizan los gramos como unidad de peso general. Por otro lado, el cálculo de los costos debe incluir además la amortización de los bienes de uso, los servicios, la mano de obra, todos los impuestos y tasas proporcionales considerando las cargas sociales, royalties si los hubiera y preferentemente se incluye un pequeño porcentaje de contingencia.  Luego para determinar el precio al consumidor a este monto se le agrega los márgenes de beneficios esperados y se lo ajusta al precio de mercado si esto fuera necesario.  Dejo de lado el contexto socio económico que, sin lugar a dudas, modificaría el procedimiento descrito.
Precisamente estos tres puntos controvertidos son los que bloquean una posible mejora de la aplicación que pudiera facilitar la experiencia al usuario.  Si estos cálculos fueran independientes, se podría agregar el precio en pesos, el índice del dólar y el precio en dólares de cada unidad en la misma lista del endpoint “recetas”, tal como ocurre en el menú de un restaurante, de una casa de comidas o en la lista de un supermercado.  De ese modo el endpoint “cotizar” no sería necesario y esto a su vez redundaría en mayores cierres de venta.
